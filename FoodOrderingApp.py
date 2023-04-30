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



