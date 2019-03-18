# Product Inventory Project - Create an application which manages an inventory of products.
#  Create a product class which has a price, id, and quantity on hand.
#  Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

class Inventory(object):
    def __init__(self):
        self.products = {}

    def addProduct(self, product):
        self.products[product.id] = product

    def __str__(self):
        out = '\t'.join(['ID', 'Price', 'Quantity'])
        for product in self.products.values():
            out += '\n' + '\t'.join([str(x) for x in [product.id, product.price, product.quantity]])
        return out

inv = Inventory()
inv.addProduct(Product(10, 'abc', 20))
inv.addProduct(Product(20, 'efg', 10))

print(inv)
