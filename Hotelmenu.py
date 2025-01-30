# Define a menu of a restaurant
menu = {
    'Pizza':150,
    'Burger':80,
    'Pasta':120,
    'Milkshake':90,
    'Rabri faluda':60,
}

#Greet
print("Welcome to Monty Restaurant")

for item in menu:
    print(item,menu[item])

order_total = 0

item_1 = input("What would you like to order?: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item is {item_1} Has bin added to you order ")

else:
    print(f"Order {item_1} is not available yet!")
    
another_item = input("Do you want to order another item? (Yes/No) ")
if another_item.lower() =="yes":
    item_2 = input("Enter Name Of Second Item ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item is {item_2} has ben added to your order ")
    else:
        print(f"Order {item_2} is not available !")
    print(f"The Total amount is to Pay {order_total}")
