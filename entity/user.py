class User:
    def __init__(self, user_id=None, user_name="", email="", password="", contact_number="", address="",role="",courier_id=""):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address


    def __str__(self):
        return f"User [ID = {self.__user_id},Name = {self.__user_name}, Email = {self.__email}]"

    # Getter
    def get_user_id(self):
        return self.__user_id
    def get_user_name(self):
        return self.__user_name
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_contact_number(self):
        return self.__contact_number
    def get_address(self):
        return self.__address

    #Setter
    def user_id(self,value):
        self.__user_id=value
    def user_name(self,value):
        self.__user_name=value
    def email(self,value):
        self.__email=value
    def password(self,value):
        self.__password=value
    def contact_number(self,value):
        self.__contact_number=value
    def address(self,value):
        self.__address=value




