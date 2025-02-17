#  Program to keep track of conference attendees. 

class Attendee:

    def __init__(self, name, company, state, email):
        'Creates an Attendee object to keep track of their data'
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getName(self):
        'Returns name'
        return self.name

    def getCompany(self):
        'Returns company name'
        return self.company

    def getState(self):
        'Returns state name'
        return self.state

    def getEmail(self):
        'Returns email'
        return self.email

    def getData(self):
        'Returns the entire info as a tuple'
        return self.name, self.company, self.state, self.email
    
attendees_list=[]

def load_attendee(file):
    infile=open(file,'r')
    for line in infile:
        name, company, state, email = line.strip().split(",")
        attendees_list.append(Attendee(name, company, state, email))

def add_attendee(attendee):
    attendees_list.append(attendee)

def display_attendee(name):
    for attendee in attendees_list:
        if attendee.getName()==name:
            return attendee.getData()
    return None

def delete_attendee(name):
    for attendee in attendees_list:
        if name==attendee.getName():
            attendees_list.remove(attendee)

def name_email():
    return [(attendee.getName(),attendee.getEmail())for attendee in attendees_list]

def name_email_state(state):
    return [(attendee.getName(),attendee.getEmail())for attendee in attendees_list if attendee.getState().lower()==state.lower()]

def update_file(file):
    outfile=open(file,'w')
    for attendee in attendees_list:
            name, company, state, email = attendee.getData()
            print(name, company, state, email, sep=",", file=outfile)
    outfile.close()

def main():

    input_file='ex3.txt'
    output_file='ex3.txt'

    load_attendee(input_file)

    print()

    print("All Attendees (Name, Email):", name_email())

    print()

    print("Attendees from TamilNadu:", name_email_state("TamilNadu"))

    print()

    attendee_data = display_attendee("John Doe")
    print("Attendee Data:", attendee_data)

    print()

    delete_attendee("John Doe")
    print("After Deletion:", name_email())
    
    print()

    update_file(output_file)

main()