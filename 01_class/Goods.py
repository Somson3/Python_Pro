class Goods:

    def __init__(self, good, price, product_description, dimensions_of_the_product):
        if price <= 0:
            raise ValueError('Price must be positive number')
        self.good = good
        self.price = price
        self.product_description = product_description
        self.dimensions_of_the_product = dimensions_of_the_product
        self.type = 'good'

    def __str__(self):
        return f'{self.good} - {self.price} {self.product_description}.'
