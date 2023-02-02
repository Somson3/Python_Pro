class Instructor:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.type = 'instructor'

    def __str__(self):
        return f'{self.type} - {self.surname} {self.name[0]}.'
