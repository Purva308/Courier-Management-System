# Parcel Tracking: Create a program that allows users to input a parcel tracking number.Store the tracking number and Status in 2d String Array. Initialize the array with values. Then, simulate the tracking process by displaying messages like "Parcel in transit," "Parcel out for delivery," or "Parcel delivered" based on the tracking number's status.
tracking_numbers = [
    ["TK001", "Delivered"],
    ["TK002", "In Transit"],
    ["TK003", "Delivered"],
    ["TK004","Pending"]
]
def parcel_tracking(tracking_number):
    flag = False
    for tracking_no, status in tracking_numbers:
        if tracking_no == tracking_number:
            if status == "Delivered":
                print("Parcel is delivered")
            elif status == "In Transit":
                print("Parcel in transit")
            elif status == "Pending":
                print("Parcel is out for delivery")
            flag = True
            break
    if flag == False:
        print("Invalid tracking number")

parcel_tracking("TK004")

# Customer Data Validation: Write a function which takes 2 parameters, data-denotes the data and detail-denotes if it is name addtress or phone number.Validate customer information based on following critirea. Ensure that names contain only letters and are properly capitalized, addresses do not contain special characters, and phone numbers follow a specific format (e.g., ###-###-####).
import re
def customer_data_validation(data, detail):
    if detail == "name":
        return data.isalpha() and data.istitle()
    elif detail == "address":
        return bool(re.match(r"^[a-zA-Z0-9\s,.-]+$", data))
    elif detail == "phone":
        return bool(re.match(r"^\d{3}-\d{3}-\d{4}$", data))
    else:
        return False
print(customer_data_validation("Aarav", "name"))
print(customer_data_validation("Mumbai, India", "address"))
print(customer_data_validation("987-654-3210","phone"))

# Address Formatting: Develop a function that takes an address as input (street, city, state, zip code) and formats it correctly, including capitalizing the first letter of each word and properly formatting the zip code.
def address_formatting(street, city, state, zip_code):
    return f"{street.title()}, {city.title()}, {state.title()}, {zip_code}"
print(address_formatting("guindy", "chennai","tamilnadu",600032))

# Order Confirmation Email: Create a program that generates an order confirmation email. The email should include details such as the customer's name, order number, delivery address, and expected delivery date.
def order_confirmation_mail(name, trackingno, address, delivery_date):
    print(f"Dear {name}, \n Your order #{trackingno} has been placed successfully.\n Your order will be delivered to {address}. \n Expected delivery date is {delivery_date} ")

order_confirmation_mail("Diya Mehra", "TK002", "Andheri, Mumbai", "2025-06-15")

# Calculate Shipping Costs: Develop a function that calculates the shipping cost based on the distance between two locations and the weight of the parcel. You can use string inputs for the source and destination addresses.
services_cost = {
    1:100.00,
    2:200.00,
    3:300.00,
    4:250.00,
    5:500.00,
    6:700.00,
    7:450.00,
    8:350.00,
    9:120.00,
    10:600.00
}
couriers = [
    ("Aarav Shah", "Bangalore", "Diya Mehra", "Mumbai",5.50, 2),
    ("Diya Mehra", "Mumbai",	"Ravi Kumar", "Delhi",3.25, 6),
	("Ravi Kumar", "Delhi",	"Sara Sharma", "Hyderabad",7.10, 10),
	("Sara Sharma",	"Hyderabad","Nikhil Rao","Chennai",4.40, 1),
	("Nikhil Rao","Chennai","Ananya Verma",	"Pune",2.85, 3),
	("Ananya Verma","Pune",	"Priya Arora",	"Kolkata",6.30, 5),
	("Priya Arora",	"Kolkata","Kunal Joshi","Ahmedabad",8.90, 8),
	("Kunal Joshi",	"Ahmedabad","Ishita Roy","Lucknow",5.70, 9),
	("Ishita Roy","Lucknow","Manav Desai","Jaipur",4.20, 7),
	("Manav Desai",	"Jaipur","Aarav Shah","Bangalore",9.50, 4)
]
def calculate_shipping(sender_city, receiver_city):
    for sender, sender_address, receiver, receiver_address, weight, service_id in couriers:
        if sender_address == sender_city and receiver_address == receiver_city:
            cost = services_cost.get(service_id, 0)
            print(f"Shipping from {sender_city} to {receiver_city}:")
            print(f"Parcel weight: {weight} kg")
            print(f"Shipping cost: {cost}")
            return
    print("No matching courier found for the given route.")

calculate_shipping("Chennai","Pune")

# Password Generator: Create a function that generates secure passwords for courier system accounts. Ensure the passwords contain a mix of uppercase letters, lowercase letters, numbers, and special characters.
import random
import string

def password_generator(length = 10):
    text = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(text) for _ in range(length))
    return password
print(password_generator(5))

# Find Similar Addresses: Implement a function that finds similar addresses in the system. This can be useful for identifying duplicate customer entries or optimizing delivery routes.Use string functions to implement this.
def find_similar_addresses(address_list, keyword):
    for address in address_list:
        if keyword.lower() in address.lower():
            print("Similar Address Found:", address)

addresses = ["Electronic city, Bangalore","Andheri, Mumbai", "Karol Bagh, Delhi"]
find_similar_addresses(addresses, "bangalore")