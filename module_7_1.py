class Product:
    def __init__(self, name: str, wight: float, category: str):
        self.name = name
        self.wight = wight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.wight}, {self.category}'


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_read = file.read()
        file.close()
        return file_read

    def add(self, *products):
        get_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in get_products:
                file.write(f'{product}\n')
            else:
                print(f'Продукт {str(product)} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())