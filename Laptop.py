from Product import Product
from info_check import cpu_check, hard_disk_check, screen_check


class Laptop (Product):
    def __init__(self,product_id,brand,model,year,price, cpu, hard_disk,screen):
        super().__init__(product_id,brand,model,year,price)
        self.cpu = cpu_check(cpu)  # default value for cpu is - "Intel Core i5"
        self.hard_disk = hard_disk_check(hard_disk)  # default value for hard disk is 12
        self.screen = screen_check(screen)  # default value for screen is 2000

    def print_me(self):
        print_from_product = super().print_me()
        print(f'{ print_from_product}',"product type: laptop" f'{ self.cpu}',"cpu:" f'{ self.cpu}',
              "laptop hard disk :"f'{ self.hard_disk}', "laptop screen:" f'{ self.screen}')

    def __repr__(self):
        repr_from_product = super().__repr__()
        return f"{repr_from_product} , laptop, {self.cpu}, {self.hard_disk}, {self.screen}"

    def __str__(self):
        str_from_product = super().__str__()
        return f"{str_from_product }, laptop, {self.cpu}, {self.hard_disk}, {self.screen}"
