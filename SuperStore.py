from Client import Client
from Exceptions import ClientNotFoundError, ShirtNotFoundError
from Laptop import Laptop
from Smartphone import Smartphone
from Shirts import Shirts
from Order import Order

import csv


class SuperStore:
    product_list = []
    clients_list = []
    orders_list = []
    shirts_list = []

    def __init__(self, product_csv_name, client_csv_name, shirts_csv_name, orders_csv_name):
        self.all_brand_list = None
        with open(f'{product_csv_name}.csv') as csvfile:
            read = csv.reader(csvfile)
            next(read)
            for row in read:
                product_id = int(row[0])
                brand = row[2]
                model = row[3]
                year = int(row[4])
                price = float(row[5])
                if row[1] == "laptop":
                    cpu = row[6]
                    hard_disk = int(row[7])
                    screen = int(row[8])
                    self.product_list += [Laptop(product_id, brand, model, year, price, cpu, hard_disk, screen)]
                else:
                    cell_net = row[9]
                    num_cores = int(row[10])
                    cam_res = int(row[11])
                    self.product_list += [
                        Smartphone(product_id, brand, model, year, price, cell_net, num_cores, cam_res)]

        with open(f'{client_csv_name}.csv') as csvfile:
            read_1 = csv.reader(csvfile)
            next(read_1)
            for row in read_1:
                client_id = int(row[0])
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]
                client_new = Client(client_id, name, email, address, phone_number, gender)
                self.add_client(client_new)

        with open(f'{shirts_csv_name}.csv') as csvfile:
            read_2 = csv.reader(csvfile)
            next(read_2)
            for row in read_2:
                product_id = int(row[0])
                price = int(row[2])
                product_name = row[1]
                units_in_stock = int(row[3])
                self.product_list += [Shirts(product_id, price, product_name, units_in_stock)]
                self.shirts_list.append(Shirts(product_id, price, product_name, units_in_stock))

        with open(f'{orders_csv_name}.csv') as csvfile:
            read_3 = csv.reader(csvfile)
            next(read_3)
            for row in read_3:
                order_id = int(row[0])
                client_id = int(row[1])
                product_id = int(row[2])
                quantity = int(row[3])
                order_new = Order(order_id, client_id, product_id, quantity)
                self.orders_list.append(order_new)

    def print_products(self):
        for product in self.product_list:
            print(product)

    def print_client(self):
        for client in self.clients_list:
            print(client)

    def get_product(self, product_id_search):
        for product in self.product_list:
            if product_id_search == product.product_id:
                return product
        return None

    def get_client(self, client_id_search):
        for client in self.clients_list:
            if client_id_search == client.client_id:
                return client
        return None

    def get_shirt(self,shirt_id_search):
        for shirt in self.shirts_list:
            if shirt_id_search == shirt.product_id:
                return shirt
        return None

    def add_client(self, client_to_add):
        for client in self.clients_list:
            if client_to_add.client_id == client.client_id:
                return False
        self.clients_list.append(client_to_add)
        return True

    def remove_product(self, product_to_remove_id):
        for product in self.product_list:
            if product_to_remove_id == product.product_id:
                self.product_list.remove(product)
                return True
        return False

    def remove_client(self, client_to_remove_id):
        for client in self.clients_list:
            if client_to_remove_id == client.client_id:
                self.clients_list.remove(client)
                return True
        return False

    def get_all_brand(self, brand_to_search):
        self.all_brand_list = []
        for product in self.product_list:
            if brand_to_search == product.brand:
                self.all_brand_list.append(product)
                return self.all_brand_list

    def get_all_bv_price_under(self, max_price_search):
        all_under = []
        for product in self.product_list:
            if max_price_search > product.price:
                all_under.append(product)
        return all_under

    def get_most_expensive_product(self):
        max_product = self.product_list[0]
        for product in self.product_list:
            if product.price > max_product.price:
                max_product = product
        return max_product

    def get_all_phone(self):
        all_smartphone = []
        for product in self.product_list:
            if type(product) is Smartphone:
                all_smartphone.append(product)
        return all_smartphone

    def get_all_laptop(self):
        all_laptops = []
        for product in self.product_list:
            if type(product) is Laptop:
                all_laptops.append(product)
        return all_laptops

    def phone_average_price(self):
        sum_price = 0
        amount_smartphone = 0
        for product in self.product_list:
            if type(product) is Smartphone:
                sum_price += product.price
                amount_smartphone += 1
        return sum_price / amount_smartphone

    def get_max_screen(self):
        only_laptops = []
        for product in self.product_list:
            if type(product) is Laptop:
                only_laptops.append(product)
        max_screen = only_laptops[0]
        for laptop in only_laptops:
            if laptop.screen > max_screen.screen:
                max_screen = laptop
        return max_screen.screen

    def get_common_cam(self):
        only_cam_res = []
        for product in self.product_list:
            if type(product) is Smartphone:
                only_cam_res.append(product.cam_res)
        return max(set(only_cam_res), key=only_cam_res.count)

    def list_popular(self):
        popular_products = []
        for product in self.product_list:
            if product.is_popular() is True:
                popular_products.append(product)
        return popular_products

    def __iadd__(self, other):
        for product in self.product_list:
            if product.product_id == other.product_id:
                print("Product already exists!")
                return self.product_list
        self.product_list.append(other)
        print("Product was added")
        return "Add!"

    def get_max_order_id(self):
        max_order_id = self.orders_list[0]
        for order in self.orders_list:
            if order.order_id > max_order_id.order_id:
                max_order_id = order
        return max_order_id.order_id

    def add_order(self, client_id, product_id, quantity):
        order_id_for_the_new_order = self.get_max_order_id() + 1
        if self.get_client(client_id) is None:
             raise ClientNotFoundError(f'The client id ({client_id}) not found')
        if self.get_product(product_id) is None:
                    raise ShirtNotFoundError(f'The product id ({product_id}) not found')
        for product in self.product_list:
            if product.product_id == product_id:
                if type(product) is Shirts:
                     quantity_in_store = product.units_in_stock
                     if quantity > quantity_in_store:
                            raise ValueError(f'The quantity ({quantity}) is bigger then the quantity in the store')
                else:
                    if quantity != 1:
                          raise ValueError(f'The quantity ({quantity}) is bigger then the quantity in the store')
        order_to_add = Order(order_id_for_the_new_order, client_id, product_id, quantity)
        self.orders_list.append(order_to_add)
        return "Order added"

    def list_of_all_shirts(self):
        shirt_list = []
        for product in self.product_list:
            if type(product) is Shirts:
                shirt_list.append(product)
        return shirt_list

    def print_all_order(self):
        for order in self.orders_list:
            print(order)