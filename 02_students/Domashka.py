""" 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент. Реалізуйте методи
 додавання, видалення студента та метод пошуку студента за прізвищем.
 Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
 """
import logging
import student
import group
import instructor
import globallimiterror

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('Domashka.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


class GlobalLimitError(Exception):
    def __init__(self, limit, msg=' '):
        self.limit = limit
        self.msg = msg

    def __str__(self):
        return f'Current number of students in group equals to limit:{self.limit}\n{self.msq}'







x_1 = student.Student('Teren', 'Vasul', 'group A', 23)
x_2 = student.Student('Petrov', 'Ivan', 'group A', 24)
x_3 = student.Student('Sidorov', 'Ivan', 'group A', 21)
x_4 = student.Student('Danulenko', 'Ivan', 'group A', 20)
x_5 = student.Student('Daragan', 'Ivan', 'group A', 30)
x_6 = student.Student('Sigorenko', 'Ivan', 'group A', 24)
x_7 = student.Student('Pretrenko', 'Ivan', 'group A', 20)
x_8 = student.Student('Kovalenko', 'Ivan', 'group A', 20)
x_9 = student.Student('Kovalshyk', 'Ivan', 'group A', 20)
x_10 = student.Student('Skorba', 'Sergii', 'group A', 20)
x_11 = student.Student('Іvashenko', 'Sergii', 'group A', 20)
x_12 = student.Student('Skorba', 'Sergii', 'group A', 20)


teacher = instructor.Instructor('Tymchuk', 'Oleh')
group = group.Group(teacher, 'Python Pro', limit=8)
group.add_student(x_1)
group.add_student(x_2)
group.add_student(x_3)
group.add_student(x_4)
group.add_student(x_5)
group.add_student(x_6)
group.add_student(x_7)
group.add_student(x_8)
# group.add_student(x_9)
# group.remove_student(x_8)
# group.add_student(x_10)
# group.add_student(x_11)
# group.add_student(x_12)

print(group)


print(group.search('Danulenko')[0])





















# teacher = Instructor('Tymchuk', 'Oleh')
# x_1 = Student('Ivanov1', 'Ivan')
# x_2 = Student('Ivanov2', 'Ivan')
# x_3 = Student('Ivanov3', 'Ivan')
# x_4 = Student('Ivanov4', 'Ivan')
# x_5 = Student('Ivanov5', 'Ivan')
# x_6 = Student('Ivanov6', 'Ivan')
# x_7 = Student('Ivanov7', 'Ivan')
#
# group = Group(teacher, 'Python Pro')
# group.add_student(x_1)
# group.add_student(x_2)
# group.add_student(x_3)
# group.add_student(x_4)
# group.add_student(x_5)
# group.add_student(x_6)
# group.add_student(x_7)
#
# print(group)
# print(len(group))
