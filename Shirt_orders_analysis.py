import numpy as np
from SuperStore import SuperStore
from Exceptions import ClientNotFoundError
import matplotlib.pyplot as plt

store_info = SuperStore("products_supply", "clients", "shirts", "orders")

#Q1:
orders_data = np.genfromtxt("orders.csv", delimiter=",", skip_header=1 )
orders = np.array(orders_data,dtype=np.int32)

#Q2:
def payment():
    list_of_all_payments = []
    payment_list =[]
    dict_of_prices = {}
    for shirt in store_info.list_of_all_shirts():
        dict_of_prices[shirt.product_id] = int(shirt.price)
    for i in range(len(orders)):
        if orders[i][2] in dict_of_prices.keys():
            price = dict_of_prices[orders[i][2]]
            payment = price*orders[i][3]
            payment_list.append(payment)
    for i in payment_list:
        list_of_all_payments.append([i])
    return list_of_all_payments

prices = np.array(payment(),dtype=np.int32)
orders_with_prices =np.hstack((orders, prices))

# Q3:
def info_to_print_max_order():
    max_price = orders_with_prices[:,4].max()
    client_dict ={}
    shirts_name_dict ={}
    for client in store_info.clients_list:
        client_dict[client.client_id] = client.name
    for shirt in store_info.list_of_all_shirts():
        shirts_name_dict[shirt.product_id] = shirt.product_name
    for i in range(len(orders_with_prices)):
        if orders_with_prices[i][4] == max_price:
            order_num = orders[i][0]
            client_id = orders[i][1]
            product_id = orders[i][2]
            if product_id in shirts_name_dict.keys() and client_id in client_dict.keys():
                client_name = client_dict[client_id]
                product_name = shirts_name_dict[product_id]
                return (f'number or order: {order_num},client name: {client_name},product name: {product_name},payment: {max_price}')

#Q4:
def all_orders_of_client():
    client_id_input = int(input("Enter the client ID :"))
    sum_of_orders = 0
    total_payment = 0
    for i in range(len(orders_with_prices)):
        if client_id_input == orders_with_prices[i][1]:
            sum_of_orders += 1
            total_payment += orders_with_prices[i][4]
    if store_info.get_client(client_id_input) is None:
        raise ClientNotFoundError(f'The client id ({client_id_input}) not found')
    else:
        client= store_info.get_client(client_id_input)
        client_name = client.name
        return (f'client name: {client_name}, number of orders: {sum_of_orders}, total payment: {total_payment}')

#Q5:
def all_payments_bigger_than_avg():
    order_bigger_than_avp =[]
    avg_payment = np.mean(orders_with_prices[:,4])
    for i in range(len(orders_with_prices)):
        if orders_with_prices[i][4] > avg_payment:
            order_bigger_than_avp.append(orders_with_prices[i])
    return np.array(order_bigger_than_avp)

#Q6:
def client_order_dict():
    clients_in_orders = []
    client_order_dict = {}
    for i in range(len(orders_with_prices)):
        if orders_with_prices[i][1] not in clients_in_orders:
            clients_in_orders.append(orders_with_prices[i][1])
    for client in clients_in_orders:
        client_all_orders = []
        for i in range(len(orders_with_prices)):
            if client == orders_with_prices[i][1]:
                client_all_orders.append(orders_with_prices[i][0])
                client_order_dict[client] = client_all_orders
    return  client_order_dict

#Q7:
def graph_bar():
    client_order_dit = client_order_dict()
    clients = []
    num_of_orders =[]
    for key in client_order_dit.keys():
        clients.append(str(key))
    for i in client_order_dit:
        v = client_order_dit.get(i)
        num_of_orders.append(len(v))
    plt.bar(clients ,num_of_orders, color=["blue","pink","green","red","yellow","purple"])
    plt.title('Number of orders for each customer')
    plt.xlabel('customer')
    plt.ylabel('number of orders')
    return  plt.show()



print( " q3 :" f'{info_to_print_max_order()}')
print( "payment list:" f'{payment()}')
print("the arry with price:" f'{orders_with_prices}')
#print(all_payments_bigger_than_avg())
#print(client_order_dict())
print(graph_bar())