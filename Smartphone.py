from Product import Product
from info_check import cell_net_check, num_cores_check, cam_res_check


class Smartphone(Product):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = cell_net_check(cell_net)  # default value for cell net is 3G
        self.num_cores = num_cores_check(num_cores)  # default value for num_cores is 12
        self.cam_res = cam_res_check(cam_res)  # default value for cam_rs is

    def print_me(self):
        print_from_product = super().print_me()
        print(f'{print_from_product}'"product type: smartphone", "cell net:" f'{self.cell_net}',
              "Smartphone num cores:" f'{self.num_cores}',
              "Smartphone cam res:" f'{self.cam_res}')

    def __repr__(self):
        repr_from_product = super().__repr__()
        return f'{repr_from_product},smartphone,{self.cell_net},{self.num_cores},{self.cam_res}'

    def __str__(self):
        str_from_product = super().__str__()
        return f'{str_from_product},smartphone,{self.cell_net},{self.num_cores},{self.cam_res}'
