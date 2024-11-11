class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            content = file.read()
            file.close()
            return content
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        file = open(self.__file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str in existing_products:
                print(f"Продукт {product} уже есть в магазине")
            else:
                file.write(product_str + '\n')
                existing_products.append(product_str)
        file.close()


# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())
