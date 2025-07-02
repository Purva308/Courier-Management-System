# 1.Write a program that checks whether a given order is delivered or not based on its status (e.g., "Processing," "Delivered," "Cancelled").Use if-else statements for this.
def courier_status_check(status):
    if status.lower()=="delivered":
        print("Delivered!")
    elif status.lower()=="in progress":
        print("In Progress!")
    elif status.lower()=="pending":
        print("Pending!")
    else:
        print("Invalid status entered")

courier_status_check("Delivered")

# 2.Implement a switch-case statement to categorize parcels based on their weight into "Light," "Medium," or "Heavy."
def weight_category(weight):
    match weight:
        case weight if weight <=1.0:
            print("Light weight parcel.")
        case weight if weight > 1.0 and weight< 5.0:
            print("Medium weight parcel.")
        case weight if weight>=5.0:
            print("Heavy weight parcel.")
        case _:
            print("Invalid weight")

weight_category(3.0)

# 3.Implement User Authentication 1. Create a login system for employees and customers using control flow statements.
users={
    "aman01": "Aman@123",
    "neha.k": "Neha@456",
    "rajiv_92": "Rajiv@789",
    "anita_s": "Anita@321",
    "raghav.t": "Raghav@101",
    "sneha_me": "Sneha@303",
    "devraj_77": "Dev@007",
    "tania_r": "Tania@200",
    "vikash_y": "Vikash@999",
    "puja_xoxo": "Puja@321"
    }
def user_login(user_name,user_password):
    if user_name in users and users[user_name]==user_password:
        print("Login Successful")
    else:
        print("Invalid Password")

user_login("raghav.t","Raghav@101")

# 4.Implement Courier Assignment Logic 1. Develop a mechanism to assign couriers to shipments based on predefined criteria (e.g., proximity, load capacity) using loops.
Courier_staff = {
    "Courier_A":2,
    "Courier_B":4,
    "Courier_C":1,
    "Courier_D":3
}

def assign_courier():
    min_load = float('inf')
    assigned_courier = None
    for courier, load in Courier_staff.items():
        if load < min_load:
            min_load = load
            assigned_courier = courier

    Courier_staff[assigned_courier] += 1
    print(f"Assigned to {assigned_courier} (New load :{Courier_staff[assigned_courier]})")
assign_courier()