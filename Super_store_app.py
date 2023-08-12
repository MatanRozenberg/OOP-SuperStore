from SuperStore import SuperStore
from tkinter import *
from tkinter import ttk
from info_check import v_years
from tkinter import messagebox
from Laptop import Laptop
from Smartphone import Smartphone

store_info = SuperStore("products_supply", "clients", "shirts", "orders")

app = Tk()
app.title("SuperStore")
app.geometry("800x800")

welcome_lbl = Label(app, text="Welcome to the Superstore app!", font=("Ariel bold", 12), fg="blue")
welcome_lbl.grid(row=0, column=0)

current_row = 1

product_lbl = Label(app, text="Product list:", font=("Ariel", 11), fg="blue")
product_lbl.grid(row=current_row+1 , column=0)

current_row +=3

product_to_see_lbl = Label(app, text="The product list you want to see:")
product_to_see_lbl.grid(row=current_row, column=0)

type_list_combo = ttk.Combobox(app, values=["All products", "Laptops", "Smartphones", "Shirts"])
type_list_combo.grid(row=current_row, column=1)

product_list_lbl = Label(app, text="The list:", fg="blue").grid(row=current_row, column=5)
product_list = Listbox(app, height=5,width=63)
product_list.grid(row=current_row, column=6)

def handel_display_click():
    product_list.delete(0, END)
    if type_list_combo.get() == "All products":
        for product in store_info.product_list:
            product_list.insert(END, str(product))
    if type_list_combo.get() == "Laptops":
        for laptop in store_info.get_all_laptop():
            product_list.insert(END, str(laptop))
    if type_list_combo.get() == "Smartphones":
        for Smartphone in store_info.get_all_phone():
            product_list.insert(END, str(Smartphone))
    if type_list_combo.get() == "Shirts":
        for Shirt in store_info.list_of_all_shirts():
            product_list.insert(END, str(Shirt))

display_lst_btn = Button(app, text="Display products", width=15, height=2, command=handel_display_click)
display_lst_btn.grid(row=current_row, column=2)

current_row += 3

#pitor 2:
create_new_product_lbl = Label(app, text="Create new product:", font=("Ariel", 11), fg="blue")
create_new_product_lbl.grid(row=current_row, column=0)

error_lbl = Label(app, text="",font=("Ariel",8), fg="red")
error_lbl.grid(row=current_row, column=1)
current_row += 2

id_lbl = Label(app, text="ID")
id_lbl.grid(row=current_row, column=1)

price_lbl = Label(app, text="Price")
price_lbl.grid(row=current_row, column=2)

brand_lbl = Label(app, text="Brand")
brand_lbl.grid(row=current_row, column=3)

model_lbl = Label(app, text="Model")
model_lbl.grid(row=current_row, column=4)

year_lbl = Label(app, text="Year")
year_lbl.grid(row=current_row, column=5)

current_row += 1

id_entry = Entry(app)
id_entry.grid(row=current_row, column=1)

price_entry = Entry(app)
price_entry.grid(row=current_row, column=2)

brand_entry = Entry(app)
brand_entry.grid(row=current_row, column=3)

model_entry = Entry(app)
model_entry.grid(row=current_row, column=4)

year_combo = ttk.Combobox(app, values=v_years)
year_combo.grid(row=current_row, column=5)

current_row += 4

def handel_Radiobutton_click():
    if value_var.get() == 1:
        cam_res_entry.configure(state=DISABLED)
        n_cores_entry.configure(state=DISABLED)
        cel_net_entry.configure(state=DISABLED)
        cpu_entry.configure(state=NORMAL)
        hard_disk_entry.configure(state=NORMAL)
        screen_entry.configure(state=NORMAL)
    if value_var.get() == 2:
        cpu_entry.configure(state=DISABLED)
        hard_disk_entry.configure(state=DISABLED)
        screen_entry.configure(state=DISABLED)
        cam_res_entry.configure(state=NORMAL)
        n_cores_entry.configure(state=NORMAL)
        cel_net_entry.configure(state=NORMAL)

value_var = IntVar()

ttk.Radiobutton(app, text='laptop',  variable=value_var, value=1 ,command=handel_Radiobutton_click).grid(row=current_row +1, column=0 )

ttk.Radiobutton(app, text='smartphone',  variable=value_var, value=2, command=handel_Radiobutton_click).grid(row=current_row +2, column=0)

cpu_lbl = Label(app, text="cpu")
cpu_lbl.grid(row=current_row, column=2)

hard_disk_lbl = Label(app, text="hard disk")
hard_disk_lbl.grid(row=current_row, column=3)

screen_lbl = Label(app, text="screen")
screen_lbl.grid(row=current_row, column=4)

cpu_entry = Entry(app)
cpu_entry.grid(row=current_row + 1, column=2)

hard_disk_entry = Entry(app)
hard_disk_entry.grid(row=current_row +1, column=3)

screen_entry = Entry(app)
screen_entry.grid(row=current_row + 1, column=4)

cel_net_lbl = Label(app, text="cellular network")
cel_net_lbl.grid(row=current_row + 2, column=2)

n_cores_lbl = Label(app, text="number of cores")
n_cores_lbl.grid(row=current_row + 2, column=3)

cam_res_lbl = Label(app, text="camera resolution")
cam_res_lbl.grid(row=current_row + 2, column=4)

cel_net_entry = Entry(app)
cel_net_entry.grid(row=current_row + 3, column=2)

n_cores_entry = Entry(app)
n_cores_entry.grid(row=current_row +3, column=3)

cam_res_entry = Entry(app)
cam_res_entry.grid(row=current_row + 3, column=4)

current_row += 5

def val_info():
    global can_conv_int, valid_id, valid_price, valid_hard_disk, valid_screen, valid_n_cores, valid_cam_res
    if value_var.get() == 1:
        error_lbl.configure(text="")
        id = id_entry.get()
        price = price_entry.get()
        brand = brand_entry.get()
        model = model_entry.get()
        cpu = cpu_entry.get()
        hard_disk = hard_disk_entry.get()
        screen = screen_entry.get()
        try:
            valid_id = int(id)
            valid_price =int(price)
            valid_hard_disk = int(hard_disk)
            valid_screen = int(screen)
            can_conv_int = True
        except ValueError:
                can_conv_int = False
                error_lbl.configure(text = str("You entered a letter to the id/price/hard disk/screen Entry The create failed"))
               #messagebox.showinfo(message="You entered a letter to the id/price/hard disk/screen Entry\n The create failed ")
        if can_conv_int is True :
            product_added = store_info.__iadd__(Laptop(valid_id,brand, model, year_combo.get(),valid_price,cpu,valid_hard_disk, valid_screen))
            if product_added == "Add!":
                messagebox.showinfo(message=f"The create succeed!\n You created the product:{valid_id},{valid_price},{brand},{model} ,{year_combo.get()} ,{cpu},{valid_hard_disk},{valid_screen}")
                id_entry.delete(0, END)
                price_entry.delete(0, END)
                brand_entry.delete(0, END)
                model_entry.delete(0, END)
                year_combo.delete(0, END)
                cpu_entry.delete(0, END)
                hard_disk_entry.delete(0, END)
                screen_entry.delete(0, END)
            else:
                error_lbl.configure(text=str("The create failed!product already exists"))
                #messagebox.showinfo(message=f"The create failed!\n product already exists")
                id_entry.delete(0, END)
                price_entry.delete(0, END)
                brand_entry.delete(0, END)
                model_entry.delete(0, END)
                year_combo.delete(0, END)
                cpu_entry.delete(0, END)
                hard_disk_entry.delete(0, END)
                screen_entry.delete(0, END)
    if value_var.get() == 2:
        error_lbl.configure(text="")
        id = id_entry.get()
        price = price_entry.get()
        brand = brand_entry.get()
        model = model_entry.get()
        cel_net = cel_net_entry.get()
        n_cores = n_cores_entry.get()
        cam_res = cam_res_entry.get()
        try:
            valid_id = int(id)
            valid_price =int(price)
            valid_n_cores = int(n_cores)
            valid_cam_res = int(cam_res)
            can_conv_int = True
        except ValueError:
            can_conv_int = False
            error_lbl.configure(text=str("You entered a letter to the id/price/cores number/Camera resolution Entry The create failed "))
            #messagebox.showinfo(message="You entered a letter to the id/price/cores number/Camera resolution Entry\n The create failed ")
        if can_conv_int is True :
            product_added = store_info.__iadd__(Smartphone(valid_id,brand, model, year_combo.get(),valid_price,cel_net,valid_n_cores, valid_cam_res))
            if product_added == "Add!":
                messagebox.showinfo(message=f"The create succeed!\n You created the product:{valid_id},{valid_price},{brand},{model} ,{year_combo.get()} ,{cel_net},{valid_n_cores},{valid_cam_res}")
                id_entry.delete(0, END)
                price_entry.delete(0, END)
                brand_entry.delete(0, END)
                model_entry.delete(0, END)
                year_combo.delete(0, END)
                cel_net_entry.delete(0, END)
                n_cores_entry.delete(0, END)
                cam_res_entry.delete(0, END)
            else:
                error_lbl.configure(text=str( "The create failed! product already exists"))
                #messagebox.showinfo(message=f"The create failed!\n product already exists")
                id_entry.delete(0, END)
                price_entry.delete(0, END)
                brand_entry.delete(0, END)
                model_entry.delete(0, END)
                year_combo.delete(0, END)
                cel_net_entry.delete(0, END)
                n_cores_entry.delete(0, END)
                cam_res_entry.delete(0, END)

def check_fill():
    error_lbl.configure(text="")
    global  all_fill, can_conv_int
    if value_var.get() == 1:
        id = id_entry.get()
        price = price_entry.get()
        brand = brand_entry.get()
        model = model_entry.get()
        cpu = cpu_entry.get()
        hard_disk = hard_disk_entry.get()
        screen = screen_entry.get()
        year = year_combo.get()
        all_fill = True
        if year == "":
            all_fill = False
        if id == "":
            all_fill = False
            id_entry.config(background='red')
        else:
            id_entry.config(background='white')
        if price == "":
            all_fill = False
            price_entry.config(background='red')
        else:
            price_entry.config(background='white')
        if brand == "":
            all_fill = False
            brand_entry.config(background='red')
        else:
            brand_entry.config(background='white')
        if model == "":
            all_fill = False
            model_entry.config(background='red')
        else:
            model_entry.config(background='white')
        if cpu == "":
            all_fill = False
            cpu_entry.config(background='red')
        else:
            cpu_entry.config(background='white')
        if hard_disk == "":
            all_fill = False
            hard_disk_entry.config(background='red')
        else:
            hard_disk_entry.config(background='white')
        if screen == "":
            all_fill = False
            screen_entry.config(background='red')
        else:
            screen_entry.config(background='white')
        return all_fill
    elif value_var.get() == 2:
        id = id_entry.get()
        price = price_entry.get()
        brand = brand_entry.get()
        model = model_entry.get()
        cel_net = cel_net_entry.get()
        n_cores = n_cores_entry.get()
        cam_res = cam_res_entry.get()
        year = year_combo.get()
        all_fill = True
        if year == "":
            all_fill = False
        if id == "":
            all_fill = False
            id_entry.config(background='red')
        else:
             id_entry.config(background='white')
        if price == "":
            all_fill = False
            price_entry.config(background='red')
        else:
            price_entry.config(background='white')
        if brand == "":
            all_fill = False
            brand_entry.config(background='red')
        else:
            brand_entry.config(background='white')
        if model == "":
            all_fill = False
            model_entry.config(background='red')
        else:
            model_entry.config(background='white')
        if cel_net == "":
            all_fill = False
            cel_net_entry.config(background='red')
        else:
            cel_net_entry.config(background='white')
        if n_cores == "":
            all_fill = False
            n_cores_entry.config(background='red')
        else:
            n_cores_entry.config(background='white')
        if cam_res == "":
            all_fill = False
            cam_res_entry.config(background='red')
        else:
            cam_res_entry.config(background='white')
        return all_fill

def on_button_click():
    if not check_fill():
        if value_var.get()==1 or value_var.get() == 2:
            error_lbl.configure(text=str("You forgot to fill the boxes in red or the year"))
            #messagebox.showinfo(message="You forgot to fill the boxes in red or the year")
        else:
            messagebox.showinfo(message="You need to mark one of the radiobutton")
    else:
        val_info()

Create_btn = Button(app, text="Create", width=15, height=2, command= on_button_click )
Create_btn.grid(row=current_row, column=5)

current_row += 4

#pitor 3 - find your order

create_new_product_lbl = Label(app, text="Find my order:", font=("Ariel", 11), fg="blue")
create_new_product_lbl.grid(row=current_row, column=0)

current_row +=1

order_to_see_lbl = Label(app, text="Choose the information you want to fill :")
order_to_see_lbl.grid(row=current_row, column=0)

def handel_Radiobutton_click_3():
    if value_var2.get() == 2:
        client_id_Entry.configure(state=DISABLED)
        order_num_Entry.configure(state=NORMAL)
    else:
        order_num_Entry.configure(state=DISABLED)
        client_id_Entry.configure(state=NORMAL)

value_var2 = IntVar()

ttk.Radiobutton(app, text='Client ID',  variable=value_var2, value=1 ,command=handel_Radiobutton_click_3).grid(row=current_row +1, column=0 )

ttk.Radiobutton(app, text='Order number',  variable=value_var2, value=2, command=handel_Radiobutton_click_3).grid(row=current_row +2, column=0)

client_id_Entry = Entry(app)
client_id_Entry.grid(row=current_row+1, column=1)

order_num_Entry = Entry(app)
order_num_Entry.grid(row=current_row+2, column=1)

current_row +=1
order_list = Listbox(app, height=5,width=63)
order_list.grid(row=current_row, column=6)

order_list_lbl = Label(app, text="The order:", fg="blue").grid(row=current_row, column=5)

def handel_search_click():
    order_list.delete(0, END)
    if value_var2.get() == 1:
        for order in store_info.orders_list:
            if int(client_id_Entry.get()) == order.client_id:
               order_list.insert(END, str(order))
    if value_var2.get() == 2:
        for order in store_info.orders_list:
            if order.order_id == int(order_num_Entry.get()):
                order_list.insert(END, str(order))



search_button = Button(app, text= "search",width=10, command=handel_search_click).grid(row=current_row,column=2)

app.mainloop()
