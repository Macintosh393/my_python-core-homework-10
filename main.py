from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.validation(value):
            super().__init__(value)


    def validation(self, phone_num):
        if len(phone_num) == 10 and phone_num.isdigit():
            return True
        else:
            return False

class Record:
    def __init__(self, name, *args):
        self.name = Name(name)
        self.phones = [*args]


    def add_phone(self, phone_num):
        self.phones.append(Phone(phone_num))
    

    def remove_phone(self, phone_num):
        for phone in self.phones:
            if phone.value == phone_num:
                self.phones.remove(phone)
    

    def edit_phone(self, old_phone_num, new_phone_num):
        for phone in self.phones:
            if phone.value == old_phone_num:
                phone.value = new_phone_num
    

    def find_phone(self, phone_num):
        for phone in self.phones:
            if phone.value == phone_num:
                return phone


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record


    def find(self, name):
        return self.data.get(name)


    def delete(self, user_name):
        for name, record in self.data.items():
            if name == user_name:
                self.data.pop(name)


if __name__ == '__main__':
    book = AddressBook()

    john_record = Record('John')
    john_record.add_phone('1234567890')
    john_record.add_phone('5555555555')

    book.add_record(john_record)

    jane_record = Record('Jane')
    jane_record.add_phone('9876543210')
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find('John')
    john.edit_phone('1234567890', '1112223333')

    print(john)

    found_phone = john.find_phone('5555555555')
    print(f"{john.name}: {found_phone}")

    book.delete('Jane')
