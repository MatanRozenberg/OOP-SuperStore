from info_check import id_check, email_check, phone_number_check, gender_check


class Client:
    def __init__(self, client_id, name, email, address, phone_number, gender):
        self.client_id = id_check(client_id)  # default value for id is 111111111
        self.name = name
        self.email = email_check(email)  # default value for email is what was input plus - @mail.com
        self.address = address
        self.phone_number = phone_number_check(phone_number)  # default value for phone is 050000000
        self.gender = gender_check(gender)  # default value for gender is F

    def print_me(self):
        print(f" client_id:{self.client_id} \n name: {self.name}\n email: {self.email}\n address: {self.address}\n "
              f"phone_number: {self.phone_number}\n gender: {self.gender}")

    def __repr__(self):
        return f"{self.client_id}, {self.name}, {self.email}, {self.address}, {self.phone_number}, {self.gender}"

    def __str__(self):
        return f"{self.client_id}, {self.name}, {self.email}, {self.address}, {self.phone_number}, {self.gender}"
