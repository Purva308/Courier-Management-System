# Create an array to store the tracking history of a parcel, where each entry represents a location update.
data1 = [
    ("TK001","Rakesh Yadav","Mumbai"),
    ("TK002","Anjali Reddy", "Delhi"),
    ("TK003","Johnathon Doe", "Hyderabad"),
    ("TK004","Fatima Sheikh", "Chennai"),
    ("TK005","Neha Singh", "Pune"),
    ("TK006","Shreya Khapoor", "Kolkata"),
    ("TK007","Vikram Mehta","Ahmedabad")
]

def display_tracking_history(tracking_number):
    flag = False
    for tracking_no, employee_name, location in data1:
        if tracking_no == tracking_number:
            print(f"Tracking Number: {tracking_no} is handled by {employee_name} and courier is in {location}")
            flag = True
    if flag == False:
        print("Invalid tracking number")

display_tracking_history("TK002")

# Implement a method to find the nearest available courier for a new order using an array of couriers.
data2 = [
    ("Rakesh Yadav","Bangalore"),
    ("Anjali Reddy", "Mumbai"),
    ("Johnathon Doe", "Delhi"),
    ("Fatima Sheikh", "Hyderabad"),
    ("Neha Singh", "Chennai"),
    ("Shreya Khapoor", "Pune"),
    ("Vikram Mehta","Kolkata")
]

def nearest_available_courier(sender_city):
    flag = False
    for emp_name, city in data2:
        if sender_city == city:
            print(f"For the nearest available courier contact {emp_name} as they are available for your city")
            flag = True
    if flag == False:
        print("Invalid data")

nearest_available_courier("Chennai")