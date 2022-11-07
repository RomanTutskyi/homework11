from core import *


adress_book = AdressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True

        except UnboundLocalError:
            return False

        except AttributeError:
            return False

        except ValueError:
            return False

        except IndexError:
            return False

        except KeyError:
            print('| key error')
            return False
    return wrapper


@input_error
def add_contact(string):
    string = string.split()
    if len(string) == 3:
        record = Record(string[0], string[1], string[2])
        adress_book.add_record(record)
        return True

    else:
        record = Record(in_name=string[0], in_phone=string[1])
        adress_book.add_record(record)
        return True


@input_error
def add_phone(string):
    name, phone = string.split()
    adress_book[name].add_phone(phone)
    return True


@input_error
def change_phone(string):
    string = string.split()
    record = adress_book.data[string[0]]
    record.change(string[1], string[2])
    return True


@input_error
def show_person(string):
    person = adress_book.data[string]
    for i in adress_book.data[string].phones:
        print(f'- {i.value}')

    if person.brt.value != None:
        print(person.brt.value)

    return True


@input_error
def remove(string):
    string = string.split()
    name, phone = string[0], string[1]
    if adress_book.in_data(name) != True:
        return False

    for i in adress_book.data[name].phones:
        if i.value == phone:
            record = adress_book[name]
            record.remove_phone(phone)
            return True

    return False


@input_error
def add_brt(string):
    string = string.split(' ')
    name, brt_date = string[0], string[1]
    adress_book.data[name].add_birthday(brt_date)

    return True


@input_error
def days_to_birthday(string):
    if adress_book.in_data(string):
        if adress_book.data[string].brt.value == None:
            return f'{string} have no birthday'
        record = adress_book[string]
        print('start')
        print(adress_book.days_to_birthday(record))
        return True


@input_error
def all_notes(count):
    count = int(count)
    adress_book.iteration(count)

    for _ in range(count):
        print(next(adress_book))
add_contact('ivan 47327423412231')
add_phone('mukola 3215')
add_phone('medj 4444431')
add_phone('roma 3313231')
add_phone('ilona 231212322')
add_phone('maks 000')
add_brt('roma 03.08.2005')
add_contact('sanya lopata')
add_phone('adron android')
add_phone('ilona tucha')
add_phone('ivan magila')
add_contact('sasha pupsik 14.08.2003')
add_phone('sasha love')


COMMANDS = {
    'add':  add_contact,
    'remove':  remove,
    'add phone': add_phone,
    'show': show_person,
    'change': change_phone,
    'all': all_notes,
    'add birthday': add_brt,
    'days to birthday': days_to_birthday,
    'show all': None
}


def main():
    print(
        '> Hello user , I know this commands:')
    print(
        '-add [name phone* dd.mm.yyyy*] , -add phone [name phone] , -add birthday [name birthday]')
    print('-change[name phone new_phone] , -remove[name phone]')
    print(
        ' , -show [name] , -show all , -all [num of notes] , -days to birthday [name]')
    print("  * - optional field , [..] - args to command")

    while True:
        u_input = input('∞ ').rstrip().lstrip()

        if u_input in ['bye', 'quit', 'exit', 'break', 'q']:
            print('>Good  Bye :)')
            break

        if u_input in ['hello',  'hey']:
            print('> Hello , my name is gustavo')

            for i in COMMANDS:
                print(f'-{i}')

        elif u_input == 'show all':
            print(adress_book.data)

        elif u_input == 'clear':
            system('clear')

        elif u_input in COMMANDS:
            string = input('Command args: ')
            command = COMMANDS[u_input]

            if command(string) == True:
                print('> Done!')

            else:
                print('> Check again args  to this command!')

        else:
            print('> I cant find this')


if __name__ == "__main__":
    main()

