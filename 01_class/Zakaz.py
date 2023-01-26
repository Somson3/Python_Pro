import Goods
import Shopper

class Zakaz:

    def __init__(self, shoper):
        self.shoper = shoper
        self.goods = []
        self.quantities = []

    def add_good(self, good, quantities):
        self.goods.append(good)
        self.quantities.append(quantities)

    def zakaz_sum(self):
        return sum(self.goods[i].price * self.quantities[i] for i in range(len(self.goods)))

    def __str__(self):
        return f'{self.shoper, self.goods, self.quantities, self.price} grn'
