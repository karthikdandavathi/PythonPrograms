import json
import sys

def run_main():
    #inp = [{}]

    inp = [{
        "name": "Al Buquerque",
        "boss": None,
        "party-animal-score": 2.0
    },
    {
        "name": "Ferb Jinglemore",
        "boss": "Al Buquerque",
        "party-animal-score": 12.1
    },
    {
        "name": "Click N. Clack",
        "boss": "Al Buquerque",
        "party-animal-score": 34.3
    },
    {
        "name": "Carl Balgruuf",
        "boss": "Ferb Jinglemore",
        "party-animal-score": -0.4
    },
    {
        "name": "Moe Shroom",
        "boss": "Carl Balgruuf",
        "party-animal-score": 44.91
    },
    {
        "name": "Jerky McGetsDrunkAndPeesInYourFridge",
        "boss": "Carl Balgruuf",
        "party-animal-score": -9999.99
    },
    {
        "name": "Howard M. Burgers",
        "boss": "Click N. Clack",
        "party-animal-score": 14.4
    },
    {
        "name": "Soren de Kiester",
        "boss": "Click N. Clack",
        "party-animal-score": 25
    }]
    
    python_party(inp)


def python_party(inp):
    """"    
        Inp: list of dictionaries containing the prospective guests
        oup: names of the invited guests

        Write up:

        The algorithm takes care of their respective boss name in the list criteria
        The algorithm takes care of the higher party-animal score criteria

        Testing:

        1) Tested for null input
        2) Tested for single input
        3) Tested for strange input
    """
    try: 
        assert isinstance(inp,list)

    except AssertionError:
        print("Input is not in expected format.. Sorry buddy come back with correct format")
        sys.exit()
    
    guest_list =[]

    if len(inp)<=0:
        print("guest list is empty...Invite some one atleast to the party")
        sys.exit

    elif 0<len(inp)<=1:
        try:
            print([guest['name'] for guest in inp])
        except Exception:
            print("guest list is empty...Invite some one atleast to the party")
            sys.exit()
    else:
        for guest in inp:
            if guest['boss'] is None:
                guest_list.append(guest)
                score = guest['party-animal-score']
            else:
                if (guest['boss'] not in [guest['name'] for guest in guest_list] and guest['party-animal-score']>score):
                    guest_list.append(guest)

    for guest in guest_list:
        print(guest['name'])

if __name__=="__main__":
    run_main()  

