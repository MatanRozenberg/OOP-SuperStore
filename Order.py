from info_check import id_check, quantity_check


class Order:
    def __init__(self, order_id, client_id, product_id, quantity):
        self.order_id = order_id
        self.client_id = id_check(client_id)  # default value for id is 111111111
        self.product_id = id_check(product_id)  # default value for id is 111111111
        self.quantity = quantity_check(quantity)  # default value for id is 6

    def __str__(self):
        return f"{self.order_id}, {self.client_id}, {self.product_id}, {self.quantity}"
