import student


class Group:

    def __init__(self, instructor, title, limit=12):
        if limit <= 0:
            raise ValueError('limit less or equal zero')
        self.instructor = instructor
        self.title = title
        self.limit = limit
        self.students = []
        logger.info(f'Create new group {self.title}')

    def add_student(self, student.student: Student):
        if not isinstance(student, Student):
            raise TypeError
        if len(self.students) == self.limit:
            logger.warning(f'Group {self.title} is full')
        if student in self.students:
            raise ValueError('Student already registered')
        self.students.append(student)

    def remove_student(self, student):
        if student not in self.students:
            logger.warning(f'{self.student} not in {self.title}')
            raise ValueError(f'{self.student} not in {self.title}')

        self.students.remove(student)

    def search(self, surname):
        res = []
        for item in self.students:
            if item.surname == surname:
                res.append(item)
        return res

    def __str__(self):
        return f'{self.title} - {self.instructor}\n' + '\n'.join(map(str, self.students))

    def __len__(self):
        return len(self.students)
