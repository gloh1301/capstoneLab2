from dataclasses import dataclass


# with a traditional class you need to init and make sure to use self
# where with a dataclass you have the types set for each type instead of setting the .self items as variables
@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'


def main():
    alex = Student('Alex', 'qwerty', 3.4)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'asdfgh', 3.5)
    print(sam)


main()
