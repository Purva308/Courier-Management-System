class Payment:
    def __init__(self, payment_id="", courier_id="", amount="", paymentDate=""):
        self.__payment_id=payment_id
        self.__courier_id=courier_id
        self.__amount=amount
        self.__paymentDate=paymentDate
# Getter
    def __str__(self):
        return f"Payment[ID ={self.__payment_id},CourierID={self.__courier_id},Amount={self.__amount}]"

    def get_payment_id(self):
        return self.__payment_id

    def get_courier_id(self):
        return self.__courier_id

    def get_amount(self):
        return self.__amount

    def get_paymentDate(self):
        return self.__paymentDate
#Setter

    def payment_id(self, PaymentID):
        self.__payment_id = PaymentID

    def courier_id(self, CourierID):
        self.__courier_id = CourierID

    def amount(self, Amount):
        self.__amount = Amount

    def payment_date(self, PaymentDate):
        self.__paymentDate = PaymentDate