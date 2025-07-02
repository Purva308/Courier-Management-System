class Location:
    def __init__(self,location_id="",location_name="",address=""):
        self.__location_id=location_id
        self.__location_name=location_name
        self.__address=address

    def __str__(self):
        return f"Location [ID = {self.__location_id},Name = {self.__location_name}, Address = {self.__address}]"

 #Getters
    def get_location_id(self):
        return self.__location_id

    def get_location_name(self):
        return self.__location_name

    def get_address(self):
        return self.__address

    # Setters
    def location_id(self, LocationID):
        self.__location_id = LocationID

    def location_name(self, LocationName):
        self.__location_name = LocationName

    def address(self, Address):
        self.__address = Address