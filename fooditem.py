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

    def add_food_item(self):
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


    def edit_food(self):
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
    def display_food_items(self,food_items):
        print('List of all food items:')
        for item in food_items:
            print(f"ID: {item['food_id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Discount: {item['discount']}%, Stock: {item['stock']}")
        
    # Call the function to display all food items
    







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


obj=FoodItem("pizza",1,2,34,5)
obj.add_food_item()
obj.display_food_items(food_items)
obj.edit_food()
obj.display_food_items(food_items)
obj.remove_food_item(food_items)


