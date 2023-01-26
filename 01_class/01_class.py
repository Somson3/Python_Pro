import Goods
import Shopper
import Zakaz

x_1 = Goods.Goods('banana', 40, 'good banana', '1x2x3')
x_2 = Goods.Goods('milk', 25, 'good milk', '3')
x_3 = Goods.Goods('bread', 20, 'white bread with raisins and poppy seeds', '500 g.')

ivanov = Shopper.Shopper('Ivanov', 'Ivan', '066 817 20 35', 5)
petrov = Shopper.Shopper('Petrov', 'Nikolay', '067 320 20 55', 2)
sidorov = Shopper.Shopper('Sidorov', 'Ura', '063 138 40 89', 4)
kovalenko = Shopper.Shopper('Kovalenko', 'Dmutro', '063 658 50 78', 1)

# zakaz_1 = Zacaz('Ivanov')
# zakaz_1.add_good(x_1, 5)
#
# zakaz_2 = Zacaz('Peterov')
# zakaz_2.add_good(x_1, 5)


zakaz_1 = Zakaz.Zakaz(ivanov)
zakaz_1.add_good(x_1, 5)
zakaz_1.add_good(x_2, 3)

zakaz_2 = Zakaz.Zakaz(petrov)
zakaz_2.add_good(x_1, 5)
zakaz_2.add_good(x_3, 2)

print(zakaz_1.shoper, zakaz_1.zakaz_sum())
print(zakaz_2.shoper, zakaz_2.zakaz_sum())
