class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class FoodOrderingApp:
    def __init__(self):
        self.admins = []
        self.users = []

    def add_admin(self, username, password):
        admin = Admin(username, password)
        self.admins.append(admin)

    def add_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)

    def admin_login(self, username, password):
        for admin in self.admins:
            if admin.username == username and admin.password == password:
                return True
        return False

    def user_login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return True
        return False





2

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "kiran@gmail.com" and password == "kiran@123":
    print("Login successful!")
    # continue with app functionality
else:
    print("Invalid username or password. Please try again.")



3

import random

# create an empty list to hold the food items
food_items = []

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

def add_food_item():
    # get the details of the new food item from the admin
    name = input("Enter the name of the food item: ")
    quantity = input("Enter the quantity of the food item (e.g. 100ml, 250gm, 4pieces): ")
    price = float(input("Enter the price of the food item: "))
    discount = float(input("Enter the discount for the food item (in percentage): "))
    stock = int(input("Enter the stock amount for the food item: "))
    
    # create a new FoodItem object and add it to the food_items list
    food_item = FoodItem(name, quantity, price, discount, stock)
    food_items.append(food_item)
    
    print("New food item added successfully!")


4

# display the list of all available food items
print("List of all available food items:")
for item in food_items:
    print(f"{item['FoodID']}: {item['Name']} ({item['Quantity']}) - INR {item['Price']}, Discount: {item['Discount']}%, Stock: {item['Stock']}")

# prompt the admin to enter the FoodID of the item they want to edit
food_id = int(input("Enter the FoodID of the item you want to edit: "))

# search for the item with the specified FoodID
found_item = False
for item in food_items:
    if item['FoodID'] == food_id:
        found_item = True
        # update the details of the item
        name = input("Enter the new name of the item: ")
        quantity = input("Enter the new quantity of the item: ")
        price = int(input("Enter the new price of the item: "))
        discount = int(input("Enter the new discount of the item: "))
        stock = int(input("Enter the new stock of the item: "))
        item['Name'] = name
        item['Quantity'] = quantity
        item['Price'] = price
        item['Discount'] = discount
        item['Stock'] = stock
        print("Item details updated successfully.")
        break

if not found_item:
    print("Item not found.")




# 5
# with sql

# import mysql.connector

# # Establish database connection
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="foodordering"
# )

# # Function to view all food items
# def view_all_food_items():
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM food_items")
#     food_items = mycursor.fetchall()
#     for item in food_items:
#         print("FoodID:", item[0])
#         print("Name:", item[1])
#         print("Quantity:", item[2])
#         print("Price:", item[3])
#         print("Discount:", item[4])
#         print("Stock:", item[5])
#         print("---------------------")

# # Call the function to view all food items
# view_all_food_items()


5


# Sample food items list
food_items = [
    {
        'food_id': 1,
        'name': 'Tandoori Chicken',
        'quantity': '4 pieces',
        'price': 240,
        'discount': 10,
        'stock': 50
    },
    {
        'food_id': 2,
        'name': 'Vegan Burger',
        'quantity': '1 piece',
        'price': 320,
        'discount': 5,
        'stock': 20
    },
    {
        'food_id': 3,
        'name': 'Truffle Cake',
        'quantity': '500gm',
        'price': 900,
        'discount': 15,
        'stock': 10
    }
]

# Function to display list of all food items
def display_food_items(food_items):
    print('List of all food items:')
    for item in food_items:
        print(f"ID: {item['food_id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Discount: {item['discount']}%, Stock: {item['stock']}")
    
# Call the function to display all food items
display_food_items(food_items)

# output==>
# List of all food items:
# ID: 1, Name: Tandoori Chicken, Quantity: 4 pieces, Price: 240, Discount: 10%, Stock: 50
# ID: 2, Name: Vegan Burger, Quantity: 1 piece, Price: 320, Discount: 5%, Stock: 20
# ID: 3, Name: Truffle Cake, Quantity: 500gm, Price: 900, Discount: 15%, Stock: 10





6


# define a function to remove a food item from the menu
def remove_food_item(food_items):
    # ask the admin for the ID of the food item they want to remove
    food_id = input("Enter the ID of the food item you want to remove: ")

    # search for the food item with the given ID
    for food_item in food_items:
        if food_item["FoodID"] == food_id:
            # remove the food item from the list of food items
            food_items.remove(food_item)
            print("Food item removed successfully!")
            break
    else:
        # if the food item is not found, print an error message
        print("Error: No food item found with the given ID")




7



users = {}

def register():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm your password: ")
    
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    
    user_data = {
        "full_name": full_name,
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "password": password,
        "order_history": []
    }
    
    users[email] = user_data
    print("Registration successful!")


8


users = []

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

def user_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user.email == email and user.password == password:
            print("Login successful!")
            # Add code to redirect to user dashboard
            return
    print("Incorrect email or password. Please try again.")

def user_register():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    new_user = User(full_name, phone_number, email, address, password)
    users.append(new_user)
    print("Registration successful!")
    # Add code to redirect to user login page

# Example usage
user_register()
user_login()




9


def user_options():
    print("Welcome to the user dashboard!")
    print("Please select an option:")
    print("1. Place New Order")
    print("2. Order History")
    print("3. Update Profile")

    option = int(input("Enter your choice (1-3): "))
    if option == 1:
        place_new_order()
    elif option == 2:
        order_history()
    elif option == 3:
        update_profile()
    else:
        print("Invalid choice. Please try again.")
        user_options()



10


food_menu = [
    {'name': 'Tandoori Chicken', 'quantity': '4 pieces', 'price': 240},
    {'name': 'Vegan Burger', 'quantity': '1 Piece', 'price': 320},
    {'name': 'Truffle Cake', 'quantity': '500gm', 'price': 900}
]

def show_food_menu():
    print('Menu:')
    for i, food in enumerate(food_menu):
        print(f'{i+1}. {food["name"]} ({food["quantity"]}) [INR {food["price"]}]')

def place_order():
    order = []
    show_food_menu()
    selected_items = input('Enter the item numbers you want to order (separated by comma): ').split(',')
    for item in selected_items:
        try:
            item_index = int(item.strip()) - 1
            if item_index < 0 or item_index >= len(food_menu):
                raise ValueError()
            order.append(food_menu[item_index])
        except ValueError:
            print(f'Invalid item number: {item.strip()}')
    if len(order) == 0:
        print('No items selected for order.')
        return
    print('Selected items:')
    for food in order:
        print(f'- {food["name"]} ({food["quantity"]}) [INR {food["price"]}]')
    confirm = input('Place order? (y/n): ').strip().lower()
    if confirm == 'y':
        print('Order placed successfully.')
    else:
        print('Order cancelled.')

place_order()



11



food_items = [    {'name': 'Tandoori Chicken', 'quantity': '4 pieces', 'price': 'INR 240'},    {'name': 'Vegan Burger', 'quantity': '1 Piece', 'price': 'INR 320'},    {'name': 'Truffle Cake', 'quantity': '500gm', 'price': 'INR 900'}]

order = []
selected_items = [2, 3]  # Example: User selects Vegan Burger and Truffle Cake

for item_num in selected_items:
    order.append(food_items[item_num - 1])  # Adjusting for 0-indexed list

print("Your order:")
for item in order:
    print("- " + item['name'] + " (" + item['quantity'] + ") " + "[" + item['price'] + "]")


12


# List of food items
food_items = {
    1: {"name": "Tandoori Chicken", "quantity": "4 pieces", "price": 240},
    2: {"name": "Vegan Burger", "quantity": "1 Piece", "price": 320},
    3: {"name": "Truffle Cake", "quantity": "500gm", "price": 900}
}

# Function to display the list of food items
def display_food_items():
    print("List of food items:")
    for item_id, item_info in food_items.items():
        print(f"{item_id}. {item_info['name']} ({item_info['quantity']}) [INR {item_info['price']}]")

# Function to place a new order
def place_new_order():
    # Display the list of food items
    display_food_items()
    
    # Get user input for food items
    order_items = input("Enter the numbers of food items you want to order (separated by comma): ")
    order_items = order_items.split(",")
    order_items = [int(x.strip()) for x in order_items]
    
    # Display the list of selected items
    print("Selected items:")
    total_price = 0
    for item_id in order_items:
        item_info = food_items.get(item_id)
        if item_info:
            print(f"{item_info['name']} ({item_info['quantity']}) [INR {item_info['price']}]")
            total_price += item_info['price']
    
    # Confirm order placement
    confirm_order = input(f"Total price is INR {total_price}. Do you want to place the order? (yes/no): ")
    if confirm_order.lower() == "yes":
        print("Order placed successfully!")
    else:
        print("Order cancelled.")

# Test the function
place_new_order()


# output==>

# List of food items:
# 1. Tandoori Chicken (4 pieces) [INR 240]
# 2. Vegan Burger (1 Piece) [INR 320]
# 3. Truffle Cake (500gm) [INR 900]
# Enter the numbers of food items you want to order (separated by comma): 2, 3
# Selected items:
# Vegan Burger (1 Piece) [INR 320]
# Truffle Cake (500gm) [INR 900]
# Total price is INR 1220. Do you want to place the order? (yes/no): yes
# Order placed successfully!



13


import json

def load_orders():
    with open('orders.json', 'r') as f:
        orders = json.load(f)
    return orders

def save_orders(orders):
    with open('orders.json', 'w') as f:
        json.dump(orders, f)

def get_order_history():
    orders = load_orders()
    if not orders:
        return "No orders found."
    order_history = []
    for order in orders:
        order_str = f"Order ID: {order['order_id']}\n"
        order_str += f"Items: {', '.join(order['items'])}\n"
        order_str += f"Total Price: INR {order['total_price']}\n"
        order_str += f"Date: {order['date']}\n"
        order_history.append(order_str)
    return '\n'.join(order_history)




14

[
  {
    "user_id": "123",
    "order_id": "1",
    "items": [
      {
        "name": "Vegan Burger",
        "price": 320,
        "quantity": 1
      },
      {
        "name": "Truffle Cake",
        "price": 900,
        "quantity": 1
      }
    ],
    "total_price": 1220,
    "timestamp": "2022-03-16T08:26:30Z"
  },
  {
    "user_id": "123",
    "order_id": "2",
    "items": [
      {
        "name": "Tandoori Chicken",
        "price": 240,
        "quantity": 2
      }
    ],
    "total_price": 480,
    "timestamp": "2022-03-17T09:30:20Z"
  }
]


15


# To create a JSON file in your directory, you can follow these steps:

# Open a text editor (like Notepad or Sublime Text) and create a new file.

# Type in the content of your JSON file.

# Save the file with a ".json" extension. For example, if you want to name your file "orders", you would save it as "orders.json".

# Make sure to save the file in the directory where you want it to be located.

# Here's an example of what the content of the "orders.json" file might look like:

# json
# Copy code



{
  "orders": [
    {
      "order_id": 1,
      "user_id": 123,
      "items": [
        {
          "name": "Vegan Burger",
          "quantity": 1,
          "price": 320
        },
        {
          "name": "Truffle Cake",
          "quantity": 1,
          "price": 900
        }
      ],
      "total_price": 1220,
      "order_date": "2022-03-16"
    },
    {
      "order_id": 2,
      "user_id": 456,
      "items": [
        {
          "name": "Tandoori Chicken",
          "quantity": 4,
          "price": 240
        },
        {
          "name": "Vegan Burger",
          "quantity": 2,
          "price": 320
        }
      ],
      "total_price": 1760,
      "order_date": "2022-03-15"
    }
  ]
}



16

import json

# function to update user profile
def update_profile(user_email, new_profile_info):
    # load user data from users.json file
    with open('users.json', 'r') as f:
        users_data = json.load(f)

    # loop through users data and find the user with the matching email
    for user in users_data:
        if user['email'] == user_email:
            # update user profile with new information
            user['full_name'] = new_profile_info.get('full_name', user['full_name'])
            user['phone_number'] = new_profile_info.get('phone_number', user['phone_number'])
            user['email'] = new_profile_info.get('email', user['email'])
            user['address'] = new_profile_info.get('address', user['address'])
            user['password'] = new_profile_info.get('password', user['password'])

            # save updated user data to users.json file
            with open('users.json', 'w') as f:
                json.dump(users_data, f, indent=4)

            return True

    # if user is not found, return False
    return False


# function callable
# # example usage
# user_email = 'example@example.com'
# new_profile_info = {
#     'full_name': 'John Doe',
#     'phone_number': '1234567890',
#     'email': 'johndoe@example.com',
#     'address': '123 Main St',
#     'password': 'new_password'
# }

# update_profile(user_email, new_profile_info)



# touch users.js
