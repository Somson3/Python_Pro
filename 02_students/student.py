import logging


class Man:
    def __init__(self, surname, name, data_of_brith):
        self.surname = surname
        self.name = name
        self.data_of_brith = data_of_brith

    def __str__(self):
        return f'{self.surname, self.name, self.data_of_brith}'


class Student(Man):
    def __init__(self, surname, name, group, data_of_brith):
        super().__init__(surname, name, data_of_brith)
        self.surname = surname
        self.name = name
        self.group = group
        self.type = 'student'
        logger.info(f'Create new student{self}')

    def __str__(self):
        return f'{self.type} - {self.surname} {self.name[0]}.'
