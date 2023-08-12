from SuperStore import SuperStore
from Client import Client
from Laptop import Laptop
from Smartphone import Smartphone
from Shirts import Shirts
from Exceptions import ClientNotFoundError, ShirtNotFoundError
from Shirt_orders_analysis import graph_bar


def create_new_laptop():
    new_product_id = int(input("Enter the product ID"))
    new_product_brand = input("Enter the product brand")
    new_product_model = input("Enter the product model")
    mew_product_year = int(input("Enter the product year"))
    new_product_price = int(input("Enter the product price"))
    cpu = input("Enter the laptop CPU")
    hard_disk = int(input("Enter the hard disk size"))
    screen = int(input("Enter the screen size in inch "))
    new_laptop = Laptop(new_product_id, new_product_brand, new_product_model, mew_product_year, new_product_price, cpu,
                        hard_disk, screen)
    return new_laptop


def create_new_smartphone():
    new_product_id = int(input("Enter the product ID"))
    new_product_brand = input("Enter the product brand")
    new_product_model = input("Enter the product model")
    mew_product_year = int(input("Enter the product year"))
    new_product_price = int(input("Enter the product price"))
    cell_net = input("Enter the smartphone cellular net")
    num_cores = int(input("Enter the smartphone number of cores, a full number"))
    cam_res = int(input("Enter the smartphone camera resolution in megapixels "))
    new_smartphone = Smartphone(new_product_id, new_product_brand, new_product_model, mew_product_year,
                                new_product_price, cell_net, num_cores, cam_res)
    return new_smartphone


def create_new_shirt():
    new_product_id = int(input("Enter the product ID"))
    new_product_price = int(input("Enter the product price"))
    product_name = input("Enter the shirt name")
    units_in_stock = int(input("Enter the shirt units in stock "))
    new_shirt = Shirts(new_product_id, new_product_price, product_name, units_in_stock)
    return new_shirt


def create_new_client():
    new_client_id = int(input("Enter the client ID"))
    new_client_name = input("Enter the client name")
    new_client_email = input("Enter the client email")
    new_client_address = input("Enter the client address")
    mew_client_phone_number = input("Enter the client phone number")
    new_client_gender = input("Enter the client gender")
    new_client = Client(new_client_id, new_client_name, new_client_email, new_client_address, mew_client_phone_number,
                        new_client_gender)
    return new_client


def menu():
    store_info = SuperStore("products_supply", "clients", "shirts", "orders")

    while True:
        n_action = input("Please enter the number of action you want\n"
                         "1.Print all products.\n"
                         "2.Print all clients.\n"
                         "3.Add new product to the store.\n"
                         "4.Add new client to the store.\n"
                         "5.Remove product.\n"
                         "6.Remove client.\n"
                         "7.Print all products under price.\n"
                         "8.Print the most expensive product.\n"
                         "9.Print a list of all the smartphones.\n"
                         "10.Print a list of all the laptops.\n"
                         "11.Print the average price for smartphone.\n"
                         "12.Print a biggest screen in the store.\n"
                         "13.Print a common camera resolution in the store.\n"
                         "14.Print a list of all popular product in the store\n"
                         "15.Print a list of all the shirts in the store\n"
                         "16.Add a new order to hte store\n"
                         "17.Print a list of all orders in the store\n"
                         "B.See a bar plot for number of orders for each customer \n"
                         "18.EXIT.\n"
                         "the number of the action you want is:")
        if n_action == "1":
            store_info.print_products()
        elif n_action == "2":
            store_info.print_client()
        elif n_action == "3":
            product_added = True
            while product_added:
                product_to_add = int(input(
                    "Enter the product type you want to add: \n For Laptop enter 1\n For Smartphone enter 2\n For "
                    "Shirt enter 3\n The product ypu want to add is:"))
                if product_to_add == 1:
                    product_for_3 = create_new_laptop()
                    store_info.__iadd__(product_for_3)
                    product_added = False
                elif product_to_add == 2:
                    product_for_3 = create_new_smartphone()
                    store_info.__iadd__(product_for_3)
                    product_added = False
                elif product_to_add == 3:
                    product_for_3 = create_new_shirt()
                    store_info.__iadd__(product_for_3)
                    product_added = False
        elif n_action == "4":
            client_for_4 = create_new_client()
            print(store_info.add_client(client_for_4))
        elif n_action == "5":
            product_id_for_5 = int(input("Enter the product ID"))
            print(store_info.remove_product(product_id_for_5))
        elif n_action == "6":
            client_id_for_6 = int(input("Enter the client ID"))
            print(store_info.remove_client(client_id_for_6))
        elif n_action == "7":
            max_price = float(input("Enter the maximum price "))
            list_of_all_under = store_info.get_all_bv_price_under(max_price)
            for product in list_of_all_under:
                print(product)
        elif n_action == "8":
            print(store_info.get_most_expensive_product())
        elif n_action == "9":
            list_of_smartphones = store_info.get_all_phone()
            for smartphones in list_of_smartphones:
                print(smartphones)
        elif n_action == "10":
            list_of_laptops = store_info.get_all_laptop()
            for laptops in list_of_laptops:
                print(laptops)
        elif n_action == "11":
            print(store_info.phone_average_price())
        elif n_action == "12":
            print(store_info.get_max_screen())
        elif n_action == "13":
            print(store_info.get_common_cam())
        elif n_action == "14":
            list_of_popular = store_info.list_popular()
            for popular_product in list_of_popular:
                print(popular_product)
        elif n_action == "15":
            list_of_shirts = SuperStore.shirts_list
            for shirt in list_of_shirts:
                print(shirt)
        elif n_action == "16":
            x = True
            while x != "Order added":
                client_id_to_order = int(input("Enter the client id"))
                product_id_to_order = int(input("Enter the product id"))
                quantity_to_order = int(input("Enter the quantity"))
                try:
                    x = store_info.add_order(client_id_to_order, product_id_to_order, quantity_to_order)
                except ClientNotFoundError as e:
                    print(e)
                except ShirtNotFoundError as e:
                    print(e)
                except ValueError as e:
                    print(e)
            print(x)
        elif n_action == "17":
            store_info.print_all_order()
        elif n_action == "B" or n_action == "b":
            graph_bar()
        elif n_action == "18":
            break
        else:
            print("ERROR: Enter a number that has not been defined")


menu()
