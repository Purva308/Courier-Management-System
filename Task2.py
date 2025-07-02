# Write a program that uses a for loop to display all the orders for a specific customer
from entity.courier import Courier

Courier_data=[
    ('Aarav Shah', 'Diya Mehra', 'TK001'),
    ('Diya Mehra', 'Ravi Kumar', 'TK002'),
    ('Ravi Kumar', 'Sara Sharma', 'TK003'),
    ('Sara Sharma', 'Nikhil Rao', 'TK004'),
    ('Nikhil Rao', 'Ananya Verma', 'TK005'),
    ('Ananya Verma', 'Priya Arora', 'TK006'),
    ('Priya Arora', 'Kunal Joshi', 'TK007'),
    ('Kunal Joshi', 'Ishita Roy', 'TK008'),
    ('Ishita Roy', 'Manav Desai', 'TK009'),
    ('Manav Desai', 'Aarav Shah', 'TK010')
]
def orders_of_customer(name):
    flag = False
    for sender, receiver, tracking_number in Courier_data:
        if sender == name or receiver == name:
            print(f"Orders placed by this customer are {tracking_number}")
            flag = True
    if flag == False:
        print("No order data found for this customer")


orders_of_customer("Aarav Shah")

# Implement a while loop to track the real-time location of a courier until it reaches its destination
courier_status_data = [
    ("In Progress","2025-06-12", "TK002"),
    ("Delivered","2025-06-07", "TK003"),
    ("Pending","not dispatched", "TK004"),
    ("Delivered","2025-06-07", "TK005"),
    ("In Progress","2025-06-11", "TK006"),
    ("Delivered","2025-06-10","TK007"),
    ("Pending",	"not dispatched", "TK008"),
    ("Delivered","2025-06-09", "TK009"),
    ("Delivered","2025-06-08", "TK010")
]
def couriers_in_progress(data):
    index = 0
    while index < len(data):
        status, date, tracking_number = data[index]
        if status == "In Progress":
            print(f"Your Courier is dispatched on the date {date} and tracking numbere is {tracking_number}")
        elif status == "Pending":
            print(f"your Courier is yet to be dispatched.")
        index+=1

couriers_in_progress(courier_status_data)