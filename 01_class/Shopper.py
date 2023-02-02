class Shopper:

    def __init__(self, surname, name, phone_number, dimensions_of_the_product):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.dimensions_of_the_product = dimensions_of_the_product
        self.type = 'shopper'

    def __str__(self):
        return f'{self.surname} - {self.name}  {self.dimensions_of_the_product}.'
