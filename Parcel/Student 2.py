from tabulate import tabulate

table_price = [
    ['Zone A', 'RM8.00', 'RM16.00', 'RM24.00'],
    ['Zone B', 'RM9.00', 'RM18.00', 'RM27.00'],
    ['Zone C', 'RM10.00', 'RM20.00', 'RM30.00'],
    ['Zone D', 'RM11.00', 'RM22.00', 'RM33.00'],
    ['Zone E', 'RM12.00', 'RM24.00', 'RM36.00']
]

def add_price(destination, below_1kg_price, between_1kg_3kg_price, above_3kg_price):
    table_price.append([destination, below_1kg_price, between_1kg_3kg_price, above_3kg_price])

add_price('Zone F', 'RM13.00', 'RM26.00', 'RM39.00')

def change_price(destination, new_above_3kg_price):
    for row in table_price:
        if row[0] == destination:
            row[-1] = new_above_3kg_price

def delete_price(destination):
    for row in table_price:
        if row[0] == destination:
            row[-1] = ''
            
def check_price(destination, weight):
    for row in table_price:
        if row[0] == destination:
            if weight < 1:
                return row[1]
            elif 1 <= weight <= 3:
                return row[2]
            else:
                return row[3]
    return None

print("Current Pricing Table:")
headers = ['Destination', 'Weight below 1kg', 'Weight in between 1kg to 3kg', 'Weight above 3kg']
print(tabulate(table_price, headers=headers, tablefmt="grid"))

change_destination = input("\nEnter the destination to change the price for parcels above 3kg: ")
new_price = input(f"Enter the new price for {change_destination} (above 3kg): ")

change_price(change_destination, new_price)

print("\nUpdated Pricing Table:")
print(tabulate(table_price, headers=headers, tablefmt="grid"))

remove_price = input("\nEnter the destination to delete the price for parcels above 3kg: ")

delete_price(remove_price)

print("\nUpdated Pricing Table:")
print(tabulate(table_price, headers=headers, tablefmt="grid"))

check_destination = input("\nEnter the destination to check the price: ")
check_weight = float(input("Enter the weight of the parcel: "))

price = check_price(check_destination, check_weight)
if price:
    print(f"The price for the parcel to {check_destination} weighing {check_weight}kg is: {price}")
else:
    print("Invalid destination or weight for pricing.")
