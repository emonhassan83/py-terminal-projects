class User:
    def __init__(self, email, password, role):
        self._email = email
        self._password = password
        self.role = role

    @property
    def email(self):
        return self._email

    def verify_password(self, password):
        return self._password == password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password, role="Customer")


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password, role="Seller")

class UserManager:
    def __init__(self):
        self.__users = []

    # user registration functionality
    def register_user(self, email, password, role):
        # Check duplicate email registration
        for user in self.__users:
            if user.email.lower() == email.lower():
                raise ValueError("Email already registered!")


        # prevent invalid role
        if role.lower() == "customer":
            new_user = Customer(email, password)
        elif role.lower() == 'seller':
            new_user = Seller(email, password)
        else:
            raise ValueError("Invalid user role!")

        self.__users.append(new_user)
        return new_user

    # user login functionality
    def login(self, email, password):
        for user in self.__users:
            if user.email.lower() == email.lower() and user.verify_password(password):
                return user
        return None