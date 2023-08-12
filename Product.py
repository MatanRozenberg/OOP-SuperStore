from info_check import id_check, year_check, price_check


class Product:
    def __init__(self, product_id, brand, model, year, price):
        self.product_id = id_check(product_id)  # default value for id is 111111111
        self.brand = brand
        self.model = model
        self.year = year_check(year)  # default value for year is 2022
        self.price = price_check(price)  # default value for price is 3000

    def print_me(self):
        print(f" product_id:{self.product_id}\n brand: {self.brand}\n model: {self.model}\n year: {self.year}\n "
              f"price: {self.price}")

    def __repr__(self):
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}"

    def __str__(self):
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}"

    def is_popular(self):
        if self.year > 2017 and self.price < 3000:
            return True
        else:
            return False
