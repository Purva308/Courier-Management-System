from util.db_conn_util import DBConnUtil
from entity.courier import Courier
from exception.InvalidEmployeeIdException import InvalidEmployeeIdException
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from dao.icourieruserservice import ICourierUserService

class CourierUserServiceImpl(ICourierUserService):
    tracking_counter=11
    def __init__(self):
        self.connection=DBConnUtil.get_connection()

    def place_order(self,courier_obj):
        cursor=None
        try:
            cursor=self.connection.cursor()
            tracking_number = f"TK{CourierUserServiceImpl.tracking_counter:03d}"
            CourierUserServiceImpl.tracking_counter += 1
            insert_query="""
                INSERT INTO Courier(CourierID,SenderName,SenderAddress,ReceiverName,ReceiverAddress,Weight,Status,TrackingNumber,PickupTime,DeliveryDate,EmployeeID,LocationID,ServiceID)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values=(
                courier_obj.get_courier_id(),
                courier_obj.get_sender_name(),
                courier_obj.get_sender_address(),
                courier_obj.get_receiver_name(),
                courier_obj.get_receiver_address(),
                courier_obj.get_weight(),
                courier_obj.get_status(),
                courier_obj.get_tracking_number(),
                courier_obj.get_delivery_date(),
                courier_obj.get_pickup_time(),
                courier_obj.get_employee_id(),
                courier_obj.get_location_id(),
                courier_obj.get_service_id()
            )
            cursor.execute(insert_query,values)
            self.connection.commit()

            print(f"Order Placed Sucessfully. Your tracking number is{tracking_number}")
            return tracking_number
        except TrackingNumberNotFoundException as e:
            print(f"Error :{e}")
        except Exception as e:
            print(f"Error placing order: {e}")
            return None
        finally:
            cursor.close()


    # Getting the order status using the tracking number
    def get_order_status(self, tracking_number):
        cursor=None
        try:
            cursor=self.connection.cursor()
            query="SELECT status FROM courier WHERE TrackingNumber=%s "
            cursor.execute(query,(tracking_number,))
            result=cursor.fetchone()
            if result:
                print(f"Status for {tracking_number}:{result[0]}")
            else:
                print("Tracking number not found.")

        except TrackingNumberNotFoundException as e:
            print(f"Error :{e}")
        except Exception as e:
            print(f"Error in fetching order status :{e} ")
        finally:
            cursor.close()

    def get_assigned_order(self,employee_id):
        cursor=None
        try:
            cursor=self.connection.cursor()
            query="""
                SELECT CourierID,SenderName,SenderAddress,ReceiverName,ReceiverAddress,Weight,Status,TrackingNumber,PickupTime,DeliveryDate,EmployeeID,LocationID,ServiceID
                From courier
                WHERE EmployeeID=%s            
            """
            cursor.execute(query,(employee_id,))
            orders=cursor.fetchall()
            if not orders:
                print(f"No orders assigned to employee ID{employee_id}")
                return[]
            for order in orders:
                print(f"Courier ID :{order[0]},Sender:{order[1]},Receiver: {order[2]}, Status : {order[4]}, Tracking number:{order[5]}")
            return orders
        except InvalidEmployeeIdException as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()


    def cancel_order(self,tracking_number):
        cursor=None
        try:
            cursor=self.connection.cursor()
            cursor.execute("SELECT Status From courier WHERE TrackingNumber=%s",(tracking_number,))
            result=cursor.fetchone()

            if result is None:
                raise TrackingNumberNotFoundException
            elif result[0]!="In Transit or Pending Pickup":
                print("Only orders with status 'Pending Pickup'can be cancelled.")
                return False
            else:
                updated_query="UPDATE courier SET Status='Cancelled' WHERE TrackingNumber=%s"
                cursor.execute(updated_query,(tracking_number,))
                self.connection.commit()
                print(f"Tracking number{tracking_number} cancelled Successfully")
                return True
        except Exception as e:
            print(f"Error cancelled the order:{e}")
            return False
        finally:
            cursor.close()

