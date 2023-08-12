def id_check(id):
    if "id".isnumeric() is True:
        id_new = int(id)
    else:
        id_new = id
    return id_new


def gender_check(gender):
    if type(gender) == str:
        gender = gender.upper()
        if gender in ["F", "M"]:
            return gender
        elif gender in ["MALE"]:
            return "M"
        else:
            return "F"
    else:
        return "F"


def year_check(year):
    if type(year) != int:
        year_new = 2022
    else:
        year_new = year
    return year_new


def email_check(email):
    if "@" in email:
        email_new = email
    else:
        email_new = email + "@mail.com"
    return email_new


def price_check(price):
    if "price".isnumeric()== True:
        price_new = price
    else:
        price_new = 3000
    return price_new


def phone_number_check(phone_number):
    if type(phone_number) != str or len(phone_number) != 10:
        return "0500000000"
    else:
        return phone_number


def cpu_check(cpu):
    if type(cpu) == int or type(cpu) == float:
        cpu_new = "Intel Core i5"
    else:
        cpu_new = cpu
    return cpu_new


def hard_disk_check(hard_disk):
    if type(hard_disk) == str or type(hard_disk) == float:
        hard_disk_new = 12
    else:
        hard_disk_new = hard_disk
    return hard_disk_new


def screen_check(screen):
    if type(screen) == str or type(screen) == float:
        screen_new = 2000
    else:
        screen_new = screen
    return screen_new


def cell_net_check(cell_net):
    if type(cell_net) == int or type(cell_net) == float or "G" not in cell_net:
        cell_net_new = "3G"
    else:
        cell_net_new = cell_net
    return cell_net_new


def cam_res_check(cam_res):
    if type(cam_res) == str or type(cam_res) == float:
        cam_res_new = 64
    else:
        cam_res_new = cam_res
    return cam_res_new


def num_cores_check(num_cores):
    if type(num_cores) == str or type(num_cores) == float:
        num_cores_new = 12
    else:
        num_cores_new = num_cores
    return num_cores_new


def unit_in_stock_check(unit_in_stock):
    if type(unit_in_stock) == str or type(unit_in_stock) == float:
        unit_in_stock_new = 45
    else:
        unit_in_stock_new = unit_in_stock
    return unit_in_stock_new


def product_name_check(product_name):
    if type(product_name) != str:
        product_name_new = "T-Shirt"
    else:
        product_name_new = product_name
    return product_name_new


def quantity_check(quantity):
    if type(quantity) != int:
        quantity_new = 6
    else:
        quantity_new = quantity
    return quantity_new


v_years = list(range(1970, 2024))

#if type(id) == str or type(id) == float:
    #     id_new = 111111111
    # else:
    #     id_new = id
    # return id_new
