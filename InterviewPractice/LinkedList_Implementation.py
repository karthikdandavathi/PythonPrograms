# LL python implementation

class Node(object):
	def __init__(self,data=None,next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next_node(self):
		return self.next_node

	def set_next_node(self,new_next_node):
		self.next_node = new_next_node

class LinkedList(Node):
	def __init__(self,head=None):
		self.head = head

	def insert(self,data):
		new_node = Node(data)
		new_node.set_next_node(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count+=1
			current = current.get_next_node()
		return count

	def search(self,data):
		current = self.head
		found = False

		while current is not None and found is False:
			if current.get_data()==data:
				found = True
			else:
				current = current.get_next_node()
		if current is None:
			raise ValueError("not in data list")

		return current

	def delete(self,data):
		current = self.head
		previous = None
		found = False

		while current is not None and found is False:
			if current.get_data()==data:
				found = True
			else:
				previous = current
				current = current.get_next_node()

		if current is None:
			raise ValueError("not in data list")
		if previous is None:
			self.head = current.get_next_node()
		else:
			previous.set_next_node(current.get_next_node())



