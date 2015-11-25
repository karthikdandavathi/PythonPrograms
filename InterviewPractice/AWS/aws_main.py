import boto.ec2
import sys
import logging
import argparse
import configparser
from configparser import ConfigParser
import time
import os

"""!    
    logging module for the program
"""
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class AWSLogic:
    def __init__(self):
        self.requests = []
        self.reservations = []
        self.failed_req_ids = []
        self.AWS_ACCESS_KEY_ID = 'AKIAISUOPF7QCQJ2USDQ'
        self.AWS_SECRET_ACCESS_KEY = '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'
        #self.sir_id = None
        #self.given_requests = []
        #self.sir_ids =[]
        self.reservations =[]
        #self.spot_reqs =[]
        self.spot_req_ids =[]
        self.instance_ids =[]
        #self.inst_id =[]
        self.ip_dict = {}
        self.rev_ip_dict = {}
        self.region=''
        self.request_status_dict = {}
        self.resv_inst_status_dict = {}
        self.terminated_ids = []   ### tracks instance ids until their corresponding SIR is closed or cancelled
        self.user_data_str = None
        self.user_data_file = None
        self.eip_obj_dict = {}   ### because of boto bug in releasing public ips (as of boto 2.34)
        self.use_private_ips = False
        #self.elastic_ips = set()
        #self.elastic_ip_dict = []

    def read_config_file(self,args):
        """"!
        reads input config file
        """
        config = configparser.ConfigParser()
        
        path = os.path.abspath(args)
        
        success = config.read(path)

        if not success:
            logger.error("Could not open file {}".format(path))
            ### might need to be raise
            return
        
        self.AMI_ID = config.get('DEFAULT', 'AMI_ID')
        self.number_of_machines_to_spawn = int(config.get('DEFAULT','number_of_machines_to_spawn'))
        self.max_spot_bid_price = config.get('DEFAULT', 'max_spot_bid_price')
        self.security_group = config.get('DEFAULT','security_group')
        self.keyname_login_to_instances = config.get('DEFAULT', 'keyname_login_to_instances')
        self.instance_type = config.get('DEFAULT', 'instance_type')
        self.weight = config.get('DEFAULT', 'weight')
        self.security_group_id = config.get('DEFAULT', 'security_group_id')
        self.user_name = config.get('DEFAULT', 'user_name')
        self.region = config.get('DEFAULT','region')

        new_akey = config.get('DEFAULT', 'aws_access_key_id', fallback=None)
        if new_akey is not None:
            self.AWS_ACCESS_KEY_ID = new_akey

        new_sakey = config.get('DEFAULT', 'aws_secret_access_key', fallback=None)
        if new_sakey is not None:
            self.AWS_SECRET_ACCESS_KEY = new_sakey

        use_private_ips = int(config.get('DEFAULT', 'use_private_ips', fallback=0))
        if use_private_ips:
            self.use_private_ips = True
        else:
            self.use_private_ips = False

        self.user_data_file = config.get('DEFAULT','user_data_file', fallback=None)
        if self.user_data_file is not None:
            self.user_data_file = os.path.expanduser(self.user_data_file)
            udf = open(self.user_data_file, "rb")
            self.user_data_file = udf
            self.user_data_str = udf.read()
            udf.close()

     
    def create_ec2_connection(self):
        """"!
        sets up a new ec2 connection
        """ 
        logger.info("connecting to EC2 cluster")
        self.conn = boto.ec2.connect_to_region(self.region,aws_access_key_id = self.AWS_ACCESS_KEY_ID,aws_secret_access_key =self.AWS_SECRET_ACCESS_KEY)
        logger.info("connection successful")
    


    def create_standard_instances(self):
        """
            creates standard instances from ec2
        """
        security_groups = self.conn.get_all_security_groups(groupnames= [self.security_group])
        logger.debug(security_groups)
        # conn.request_spot_instances returns a list of SpotInstanceRequests
        new_reservation = self.conn.run_instances( image_id=self.AMI_ID, 
                                                min_count=self.number_of_machines_to_spawn,
                                                max_count=self.number_of_machines_to_spawn,
                                                key_name=self.keyname_login_to_instances,
                                                security_groups=security_groups,
                                                instance_type = self.instance_type,
                                                user_data = self.user_data_str,
                                                dry_run= False)
        self.reservations.append(new_reservation)
        #self.get_request_ids()
        time.sleep(3)
        return [ i.id for i in new_reservation.instances ]


    def check_terminated_instance_request_consistency(self):
        """ check that if a given spot instance is terminated, the associated 
        spot request instance is terminated
        return True if we had to issue a cancel (so the caller can pause for a bit)
        """

        ret=False
        ### check consistency of supposedly active instances.
        if len(self.instance_ids) > 0:
            instances = self.conn.get_only_instances(instance_ids = self.instance_ids)
            for inst in instances:
                if inst.state == 'terminated':
                    self.terminate_instance(inst.id)

        ### check consistency of sirs related to terminated instances.
        if len(self.terminated_ids) > 0:
            removed_from_terminated=list()
            for inst_id in self.terminated_ids:
                try:
                    inst = self.conn.get_only_instances(instance_ids = [ inst_id] )[0]
                except:
                    ### means the instance is no longer tracked in aws so we can delete from terminated
                    removed_from_terminated.append(inst_id)
                    continue

                sir_id=inst.spot_instance_request_id
                if sir_id:
                    sir = self.conn.get_all_spot_instance_requests(request_ids = [sir_id])[0]
                    if not (sir.state == 'canceled' or sir.state =='closed'):
                        ### forcibly send a cancel.
                        self.conn.cancel_spot_instance_requests( request_ids = [sir_id])
                        ret=True
                    else:
                        ### we can stop tracking the instance
                        removed_from_terminated.append(inst_id)
                else:
                    ### not an instances generated from spot request. so it got added here by mistake
                    ### so do the same stop tracking
                    removed_from_terminated.append(inst_id)


            for r in removed_from_terminated:
                self.terminated_ids.remove(r)

        return ret

    def create_spot_instances(self): 
        """"!
        creates spot instances by reading values fromobject
        config file
        """

        ### do a consistency check
        if self.check_terminated_instance_request_consistency():
            time.sleep(15)
        security_groups = self.conn.get_all_security_groups(groupnames= [self.security_group])
        logger.debug(security_groups)
        # conn.request_spot_instances returns a list of SpotInstanceRequests
        done = False
        retries = 0
        # implement retry loop to deal with latency of AWS state transitions
        while not done and retries < 10:
            try:
                new_requests = self.conn.request_spot_instances(price=self.max_spot_bid_price, 
                                                                image_id=self.AMI_ID, 
                                                                count=self.number_of_machines_to_spawn, 
                                                                type='one-time',
                                                                key_name=self.keyname_login_to_instances,
                                                                security_groups=security_groups,
                                                                instance_type = self.instance_type,
                                                                user_data = self.user_data_str,
                                                                dry_run= False)
            except:
                retries+=1
                self.check_terminated_instance_request_consistency()
                time.sleep(600)
            else:
                done=True

        if not done:
            return []

        self.requests.extend(new_requests)
        self.get_request_ids()
        time.sleep(3)
        return [ r.id for r in new_requests ]
    
    """"!
        returns the request ids of spot instances
        created
    """    
    def get_request_ids(self):
        self.spot_req_ids = [ sir.id for sir in self.requests ] 
        return self.spot_req_ids


    def get_instance_ids_from_reservations(self):
        return [ i.id for r in self.reservations for i in r.instances ]
    
    def wait_for_reservations_fullfillment(self, timeout=50, instance_ids=None):

        if instance_ids is None:
            instance_ids = self.get_instance_ids_from_reservations()

        loop_count = 0
        instance_ready = { i:False for i in instance_ids }
        while not all ( instance_ready.values()) and loop_count <= timeout:
            loop_count+=1
            instances = self.conn.get_only_instances(instance_ids = instance_ids)
            for inst in instances:
                if inst.state != 'pending':
                    instance_ready[inst.id] = True
            
            if not all (instance_ready.values()):
                time.sleep(15)
        
        ### get final dispositions of instances
        good_instances =0
        instances = self.conn.get_only_instances(instance_ids = instance_ids)
        for inst in instances:
            if inst.state != 'running':
                if inst.state == 'pending':
                    self.resv_inst_status_dict[inst.id] = 'timed out'
                else:
                    self.resv_inst_status_dict[inst.id] = 'post-fulfillment premature instance termination'
            else:
                if self.use_private_ips:
                    ipaddr=inst.private_ip_address
                else:
                    ipaddr=inst.ip_address
                self.instance_ids.append(inst.id)
                self.ip_dict[inst.id] = ipaddr
                self.rev_ip_dict[ipaddr] = inst.id
                self.resv_inst_status_dict[inst.id] = 'running'
                good_instances+=1

        time.sleep(30)

        return (len (instance_ids), good_instances) 


    def wait_for_fulfillment(self, timeout=50, request_ids=None):
        """ wait for spot requests to be fulfilled or otherwise
        Total redesign by BYeh to add some error checking and a timeout

        returns tuple:
          (number of requests waited for, number of good instances created)

        """
        logger.debug("waiting for requests to be fulfilled") 

        if request_ids is None:
            spot_req_ids = self.spot_req_ids
        else:
            spot_req_ids = request_ids

        processed_dict=dict()
        for sir_id in spot_req_ids:
            processed_dict[sir_id] = False
            #status_dict[sir_id] = None

        ### wait for a disposition for each spot request (basically when sir.state is not open)
        loop_count=0
        while not all( processed_dict.values()) and loop_count <= timeout:
            loop_count+=1
            try:
                spot_reqs = self.conn.get_all_spot_instance_requests(request_ids = spot_req_ids)
            except boto.exception.EC2ResponseError:
                ### need to wait a little time for AWS to register the requests, if this function called
                ### right after create_spot_instances
                time.sleep(3)
                continue
            for sir in spot_reqs:
                if sir.state != 'open':
                    processed_dict[sir.id] = True

            if not all ( processed_dict.values()):
                time.sleep(15)


        ### get disposition of each spot instance request
        spot_reqs = self.conn.get_all_spot_instance_requests(request_ids = spot_req_ids)
        instance_ids = list()
        instance_ready = dict()
        for sir in spot_reqs:
            if sir.state == 'open':
                self.request_status_dict[sir.id] = 'timed out'
            else:
                self.request_status_dict[sir.id] = sir.status.code

            if sir.status.code == 'fulfilled':
                instance_ids.append(sir.instance_id)
                instance_ready[sir.instance_id] = False
            else:
                self.failed_req_ids.append(sir.id)
                
        ### wait for ready states in the fulfilled instances
        while not all ( instance_ready.values()) and loop_count <= timeout:
            loop_count+=1
            instances = self.conn.get_only_instances(instance_ids = instance_ids)
            for inst in instances:
                if inst.state != 'pending':
                    instance_ready[inst.id] = True
            
            if not all (instance_ready.values()):
                time.sleep(15)

        ### get final dispositions of instances
        good_instances =0
        instances = self.conn.get_only_instances(instance_ids = instance_ids)
        for inst in instances:
            if inst.state != 'running':
                sir_id = inst.spot_instance_request_id
                self.failed_req_ids.append(sir_id)
                if inst.state == 'pending':
                    self.request_status_dict[sir_id] = 'timed out'
                else:
                    self.request_status_dict[sir_id] = 'post-fulfillment premature instance termination'
            else:
                if self.use_private_ips:
                    ipaddr=inst.private_ip_address
                else:
                    ipaddr=inst.ip_address
                self.instance_ids.append(inst.id)
                self.ip_dict[inst.id] = ipaddr
                self.rev_ip_dict[ipaddr] = inst.id
                self.request_status_dict[sir_id] = 'running'
                good_instances+=1


        ###  might have to sleep a little bit after running status toggles before it can accept ssh connections
        # put a 30 second delay in
        time.sleep(30)

        return (len (spot_req_ids), good_instances) 

        ### to retrieve good instances: awsobj.instance_ids[-good_instances:]

    """"!
        returns the output in user requested format
    """    
    def create_instance_ids_file(self,args):
        path = os.path.abspath(args)
        with open(file=path , mode='w') as temp_file:
            for each_instance_id in self.instance_ids:
                temp_file.write("%s\n"%each_instance_id)


    def generate_output(self,args):
        path = os.path.abspath(args)            
        
        with open(file= path, mode='w') as f_name:
            for str in self.generate_connection_strings():
                print(str, file=f_name)

        logger.info("script executed successfully")


    def generate_connection_strings(self, instance_ids=None):

        if instance_ids is None:
            instance_ids = self.instance_ids
        
        return [ "{0}@{1}  {2}".format(self.user_name,
                                       self.ip_dict[inst_id],
                                       self.weight) for inst_id in instance_ids ]


    def terminate_instance(self, instance_id):
        """ terminate a single instance (also updating various internal structures)

        """

        ### do a consistency check
        if self.check_terminated_instance_request_consistency():
            time.sleep(15)

        if instance_id in self.instance_ids:

            inst = self.conn.get_only_instances(instance_ids = [instance_id])[0]
            if self.use_private_ips:
                ip=inst.private_ip_address
                public_ip=inst.ip_address
            else:
                ip=inst.ip_address
                public_ip=inst.ip_address
            #ip = inst.ip_address
            sir_id = inst.spot_instance_request_id

            self.conn.terminate_instances(instance_ids = [instance_id])
            if sir_id:
                self.terminated_ids.append(instance_id)    ### self.terminated_id only apply to instances create by spot request
                self.request_status_dict[sir_id] = 'terminated'
            else:
                self.resv_inst_status_dict[instance_id] = 'terminated'
            self.instance_ids.remove(instance_id)
            del self.ip_dict[instance_id]
            del self.rev_ip_dict[ip]
            if public_ip in self.eip_obj_dict:
                self.release_elastic_ip(ip)
            #if ip in self.elastic_ips:
            #    self.elastic_ips.remove(ip)
            #    self.conn.release_address(public_ip=ip)

    def terminate_all_instances(self):
        ### make local copy to avoid strangeness with self.instance_ids removals
        instance_id_list = list(self.instance_ids)
        for inst_id in instance_id_list:
            self.terminate_instance(inst_id)

        ### call this to force the sirs to cancel asap.
        self.check_terminated_instance_request_consistency()

        ### release all elastic ips
        for ip in self.eip_obj_dict:
            self.release_elastic_ip(ip)
        #for ip in self.elastic_ips:
        #    self.conn.release_address(public_ip=ip)

    def rotate_new_elastic_ip(self, instance_id):
        """ give the passed instance a new external ip
        """

        # get existing public ip
        inst = self.conn.get_only_instances(instance_ids = [instance_id])[0]
        old_ip = inst.ip_address
        #old_ip = self.ip_dict[instance_id]

        # allocate new ip
        try:
            new_ip_obj = self.conn.allocate_address()
        except:
            return False

        self.eip_obj_dict[new_ip_obj.public_ip] = new_ip_obj
        #self.elastic_ips.add(new_ip_obj.public_ip)

        time.sleep(10)

        #assign it to a new instance
        status=self.conn.associate_address(instance_id=instance_id, public_ip=new_ip_obj.public_ip)
        if status is False:
            return False

        ### if using private ips, we don't need to swap anything
        if not self.use_private_ips:
            self.ip_dict[instance_id] = new_ip_obj.public_ip
            self.rev_ip_dict[new_ip_obj.public_ip] = instance_id

        #wait for assignment to take hold (15 seconds)
        time.sleep(15)

        # release old ip (if elastic)
        #if old_ip in self.elastic_ips:
            #self.conn.release_address(public_ip=old_ip)
            #self.elastic_ips.remove(old_ip)
        if old_ip in self.eip_obj_dict:
            self.release_elastic_ip(old_ip)

        ### if using private ips, we don't need to delete the old ip
        if not self.use_private_ips:
            del self.rev_ip_dict[old_ip]

        return True

    def release_elastic_ip(self, eip):
        """ release a specific elastic ip by ip address
        safe mode. Requests from aws our eip objects first in order to prevent some wierdness
        or delays with regards to changing ips.
        possibly do a few retries (timing issues)
        """

        eip_obj = None
        try:
            eip_obj = self.conn.get_all_addresses(addresses=[eip])[0]
        except IndexError:
            return True

        if eip_obj:
            retries=0
            done=False
            while not done and retries < 3:
                try:
                    status=eip_obj.release()
                    done=True
                except:
                    retries+=1
                    time.sleep(15)
                    try:
                        eip_obj = self.conn.get_all_addresses(addresses=[eip])[0]
                    except IndexError:
                        return True

            if not done:
                return False

            if status:
                del self.eip_obj_dict[eip]
                
            return status

        else:
            return False
        

    def request_new_elastic_ip(self):
        pass


   
"""!
    calls all the functions
"""
def main():
    logger.info("entering main")
    parser = argparse.ArgumentParser(description='inputing the filenames')
    parser.add_argument('-a',dest = "inputfname",help="config file", required =True,type = str,metavar ='FILE')
    parser.add_argument('-b',dest = "instancefname",help="instance id output file", required =True,type = str,metavar ='FILE')
    parser.add_argument('-c',dest = "outputfname",help="dispatch output file",required =True,type = str,metavar ='FILE')

    args = parser.parse_args()
    
    awsLogic = AWSLogic()
    awsLogic.read_config_file(args=args.inputfname)
    awsLogic.create_ec2_connection()       
    awsLogic.create_spot_instances()
    awsLogic.wait_for_fulfillment()
    awsLogic.create_instance_ids_file(args= args.instancefname)
    awsLogic.generate_output(args=args.outputfname)
    

if __name__ == '__main__':
    sys.exit(main())
    
