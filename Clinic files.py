
class Data:
    record = {}
    data = []

class Patient:
    def __int__(self,name,last_name,id):
        self.name = name
        self.last_name = last_name
        self.id = id.upper

    def new_patient(self):
        self.name = input('Please enter your name: ')
        self.last_name = input('Please enter your last name: ')
        self.id = input('Please enter your ID number: ')
        Data.data.append(self.name)
        Data.data.append(self.last_name)
        Data.data.append(self.id)
        return Patient


    def add_patient(self):
        Data.record[self.new_patient(self)] = Data.data

    def print_record(self):
        for patient, dat in Data.record.items():
            print('{}: {}'.format(patient,dat))



def menu():
    option = input('Please choose one of this options typing the corresponding letter:\n\
a) Add new patient\nb) Show patients lists\nc) Exit\n')

    while option not in ('AaBbCc'):
        print('Type a valid option')
        option = input('Please choose one of this options typing the corresponding letter:\n\
a) Add new patient\nb) Show patients lists\nc) Exit\n')

    while option == 'a' or option == 'A':
        Patient.add_patient(Patient)
        print('Patient sucessfully added!')
        option = input('Please choose one of this options typing the corresponding letter:\n\
a) Add new patient\nb) Show patients lists\nc) Exit\n')

    if option == 'b' or option == 'B':
        Patient.print_record(Patient)

    if option == 'c' or option == 'C':
        print('Thank you for your time, hope we have helped!')

#Main code

start = menu()



