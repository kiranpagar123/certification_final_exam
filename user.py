  

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
        else:
            print("Incorrect email or password. Please try again.")
    




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



def user_options():
    while True:

        option = int(input("Welcome to the user dashboard! \nEnter your choice: \n1.Place order \n2.Order History \n3.Update History \n: "))
        if option == 1:
            place_new_order
        elif option == 2:
            get_order_history

        elif option == 3:
           update_profile()
        else:
            print("Invalid choice. Please try again.")    


def user_register():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    new_user = User(full_name, phone_number, email, address, password)
    users.append(new_user)
    print("Registration successful!")
    
