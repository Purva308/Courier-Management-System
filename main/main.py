from entity.courier import Courier
from dao.courieruserserviceImpl import CourierUserServiceImpl
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from datetime import date
def main():
    service=CourierUserServiceImpl()

    while True:
        print("\n ========= Courier Management System =========")
        print("1. Place Order")
        print("2. Get Order status")
        print("3. Cancel order")
        print("4. Get assigned orders")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice=="1":
            try:
                courier_id=int(input("Enter the courier ID: "))
                sender_name=input("Enter the sender name:")
                sender_address=input("Enter the sender address: ")
                receiver_name=input("Enter the receiver name: ")
                receiver_address=input("Enter the receiver address: ")
                weight=float(input("Enter weight: "))
                status=input("Enter status (In Transit/Pending/Delivered/Out for Delivery): ")
                tracking_number=input("Enter your tracking number: ")
                pickup_time = input("Enter the pickup time(HH:MM:SS): ")
                delivery_date=input("Enter the delivery date(YYYY-MM-DD): ")
                employee_id=int(input("Enter the employee ID: "))
                location_id=int(input("Enter the location ID: "))
                service_id=int(input("Enter the service ID: "))

                courier_obj=Courier(
                    courier_id,sender_name,sender_address,receiver_name,receiver_address,weight,status,tracking_number,pickup_time,delivery_date,employee_id,location_id,service_id)
                tracking_number=service.place_order(courier_obj)
                print("Tracking Number:",tracking_number)
            except Exception as e:
                print(f"Error placing order {e}.")

        elif choice=="2":
            tracking_number=input("Enter tracking number:")
            service.get_order_status(tracking_number)

        elif choice=="3":
            tracking_number=input("Enter tracking number to cancel: ")
            result = service.cancel_order(tracking_number)
            if result:
                print("Order Cancelled!")


        elif choice=="4":
            employee_id=int(input("Enter the Employee ID: "))
            orders=service.get_assigned_order(employee_id)
            if not orders:
                print("No Order Assinged")

        elif choice=="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.Try again")

if __name__=="__main__":
    main()
