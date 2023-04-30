from login import *
from user import *
class Main:
    def execute(self,choice):
        if choice==1:
            print("*********Welcome in Admin Section*********")
            if isinstance(user, Admin):
              user.add_food_item("Pizza", "Large", 10.99, 0.1, 50, food_items)

        if choice==2:
            print("*********Edit Food item*********")
            if isinstance(user, Admin):
              user.edit_food_item(1, "Pizza", "Medium", 8.99, 0.15, 30, food_items)
        if choice==3:
            print("********View Food Item*********")
            user.view_food_items(food_items)
        if choice==4:
            print("*********Remove Food Item*********")
            if isinstance(user, Admin):
              user.remove_food_item(1, food_items)

        if choice==5:
            print("*********Login AS User")  
            print("Please register befor login")
            user_register()
            user_login()

        if choice==6:
            user_options()     
main=Main()
food_items = []
user_access = UserAccess()
user = user_access.login()

while True:
    choice=int(input("Enter \n1.Login As Admin \n2.Edit food item \n3.Delete Book \n4.Update Book \n5.Search Book By ID \n6.Search Book By Name \n: "))
    main.execute(choice)
        


