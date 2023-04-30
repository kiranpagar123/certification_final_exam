
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "kiran@gmail.com" and password == "kiran@123":
    print("Login successful!")
    # continue with app functionality
else:
    print("Invalid username or password. Please try again.")

      


class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        
    def add_food_item(self, name, quantity, price, discount, stock, food_items):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(food_items) + 1
        food_items.append(food_item)
        print("Food item added successfully.")
        
    def edit_food_item(self, food_id, name, quantity, price, discount, stock, food_items):
        for food_item in food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully.")
                return
        print("Food item with the given ID not found.")
        
    def view_food_items(self, food_items):
        print("Food Items:")
        for food_item in food_items:
            print(f"ID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")
            
    def remove_food_item(self, food_id, food_items):
        for i in range(len(food_items)):
            if food_items[i].food_id == food_id:
                del food_items[i]
                print("Food item removed successfully.")
                return
        print("Food item with the given ID not found.")
        
class UserAccess:
    def __init__(self):
        self.users = {"kiran@gmail.com": "kiran@123", "user1": "pass1", "user2": "pass2"}
        
    def login(self):
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in self.users and self.users[username] == password:
                return Admin(username, password) if username == "admin" else User(username, password)
            print("Invalid username or password. Please try again.")
            
# Sample usage









