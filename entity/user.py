class User:
    def __init__(self, user_id=None, name="", email="", password="", contact_number="", address="",role="",courier_id=""):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address
        self.__role=role
        self.__courier_id=courier_id

    # Getter
    def get_user_id(self):
        return self.__user_id
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_contact_number(self):
        return self.__contact_number
    def get_address(self):
        return self.__address
    def get_role(self):
        return self.__role
    def get_courier_id(self):
        return self.__courier_id
    #Setter
    def user_id(self,value):
        self.__user_id=value
    def name(self,value):
        self.__name=value
    def email(self,value):
        self.__email=value
    def password(self,value):
        self.__password=value
    def contact_number(self,value):
        self.__contact_number=value
    def address(self,value):
        self.__address=value
    def role(self,value):
        self.__role=value
    def courier_id(self,value):
        self.__courier_id=value



