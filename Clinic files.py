class Data:
    record = {}


class Patient:
    def __init__(self, name, last_name, id, gender):
        self.name = name
        self.last_name = last_name
        self.id = id
        self.gender = gender


def wrong_option():
    option = input()
    while option not in 'AaBbCc':
        print('Type a valid option')
        option = input()




def new_patient():
    name = input('Please enter your name: ')
    last_name = input('Please enter your last name: ')
    id = input('Please enter your ID number: ')
    gender = input('Please type Male(M) or Female(F): ')
    while gender not in 'MmFf':
        print('{} is not a valid option.'.format(gender))
        gender = input('Please type Male(M) or Female(F): ')
    if gender in 'Mm':
        gender = 'male'
    elif gender in 'Ff':
        gender = 'female'
    new_p = Patient(name, last_name, id, gender)
    Data.record[id] = [new_p.last_name, new_p.name, new_p.id, gender]
    return new_p

def print_record():
    input_id = input('Please enter your ID number to visualize your info: ')
    if input_id in Data.record:
        for i in range(len(Data.record[input_id])):
            data = ''
            data += Data.record[input_id][i]
            print(data)

        select = input('Would you like to:\na) Try another ID number\nb) Go to main menu\nc) Exit\n')
        if select in 'Aa':
            print_record()
        elif select in 'Bb':
            menu()
        elif select in 'Cc':
            print('Thank you for your time, hope we have helped!')

    else:
        while input_id not in Data.record:
            print('The ID number given is not in our current database')
            select2 = input('Would you like to:\na) Try another ID number\nb) Go to main menu\nc) Exit\n')
            while select2 not in 'Cc':
                if select2 in 'Aa':
                    print_record()
                elif select2 in 'Bb':
                    menu()
                elif select2 in 'Cc':
                    print('Thank you for your time, hope we have helped!')
                    break
            else:
                print('Thank you for your time, hope we have helped!')
                break



def menu():
    option = input('Please choose one of this options typing the corresponding letter:\n\
a) Add new patient\nb) Show patient info\nc) Exit\n')


    while option in 'Aa':
        new_patient()
        print('Patient successfully added!')
        option = input('Please choose one of this options typing the corresponding letter:\n\
a) Add new patient\nb) Show patient info\nc) Exit\n')


    if option in 'Bb':
        print_record()


    if option in 'Cc':
        print('Thank you for your time, hope we have helped!')



# Main code

menu()
