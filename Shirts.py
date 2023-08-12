from Product import Product
from info_check import unit_in_stock_check, product_name_check


class Shirts(Product):
    def __init__(self, product_id, price, product_name, units_in_stock):
        super().__init__(product_id, "SuperStore", "", 2023, price)
        self.product_name = product_name_check(product_name)  # default value for product name is - T-Shirt
        self.units_in_stock = unit_in_stock_check(units_in_stock)  # default value for units in stock is 45

    def __str__(self):
        return f'{self.product_id}, {self.price},{self.product_name}, {self.units_in_stock}'
