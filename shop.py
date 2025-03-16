class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Customer(name={self.name}, orders_count={len(self.orders)})"

    def __repr__(self):
        return self.__str__()


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self, discount=None):
        total = sum(product.price for product in self.products)
        if discount:
            total = Discount.apply_discount(total, discount)
        return total

        def __str__(self):
            return f"Order(products={self.products})"

        def __repr__(self):
            return self.__str__()

class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(total, discount):
        return total * (1 - discount.discount_percent / 100)

    @staticmethod
    def seasonal_discount():
        return Discount("Seasonal Discount", 20)

    @staticmethod
    def promo_code_discount():
        return Discount("Promo Code Discount", 10)

    def __str__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"

    def __repr__(self):
        return self.__str__()


# Создание продуктов
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Tablet", 300)

# Создание клиентов
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Создание заказов
order1 = Order()
order1.add_product(product1)
order1.add_product(product2)

order2 = Order()
order2.add_product(product3)

# Добавление заказов клиентам
customer1.add_order(order1)
customer2.add_order(order2)

# Применение скидок
seasonal_discount = Discount.seasonal_discount()
total_with_discount = order1.calculate_total(seasonal_discount)

# Вывод информации о клиентах, заказах и продуктах
print(customer1)
print(customer2)
print(order1)
print(order2)
print(f"Total for Order 1 with seasonal discount: {total_with_discount}")
print(f"Total for Order 2: {order2.calculate_total()}")