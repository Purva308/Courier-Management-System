class CourierService:
    def __init__(self,service_id="",service_name="",cost=""):
        self.__service_id=service_id
        self.__service_name=service_name
        self.__cost=cost

    def __str__(self):
        return f"CourierService [ID= {self.__service_id},Name={self.__service_name},Cost={self.__cost}]"

#Getters
    def get_service_id(self):
        return self.__service_id

    def get_service_name(self):
        return self.__service_name

    def get_cost(self):
        return self.__cost

#Setters
    def service_id(self, value):
        self.__service_id = value

    def service_name(self, value):
        self.__service_name = value

    def cost(self, value):
        self.__cost = value