class Courier:
    def __init__(self,courier_id=None,sender_name="",sender_address="",receiver_name="",receiver_address="",weight="",status="",tracking_number="",deilevery_date="",pickup_time="",employee_id="",location_id="",service_id=""):
        self.__courier_id=courier_id
        self.__sender_name=sender_name
        self.__sender_address=sender_address
        self.__receiver_name=receiver_name
        self.__receiver_address=receiver_address
        self.__weight=weight
        self.__status=status
        self.__tracking_number=tracking_number
        self.__delivery_date=deilevery_date
        self.__pickup_time=pickup_time
        self.__employee_id=employee_id
        self.__location_id=location_id
        self.__service_id=service_id

    # Getter
    def get_courier_id(self):
        return self.__courier_id
    def get_sender_name(self):
        return self.__sender_name
    def get_sender_address(self):
        return self.__sender_address
    def get_receiver_name(self):
        return self.__receiver_name
    def get_receiver_address(self):
        return self.__receiver_address
    def get_weight(self):
        return self.__weight
    def get_status(self):
        return self.__status
    def get_tracking_number(self):
        return self.__tracking_number
    def get_delivery_date(self):
        return self.__delivery_date
    def get_pickup_time(self):
        return self.__pickup_time
    def get_employee_id(self):
        return self.__employee_id
    def get_location_id(self):
        return self.__location_id
    def get_service_id(self):
        return self.__service_id

    #Setter

