
# Introduction to Python Classes
# In-Class Activities: Python Object-Oriented Programming

# Video 1

class User:

    def __init__(self, username=None, password=None,
                 email=None, birthday=None):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday


    # Video 2

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

    def __repr__(self):
        return (
            f"User(username={self.username!r}, "
            f"email={self.email!r}, "
            f"birthday={self.birthday!r})"
        )


    # Video 3

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def update_email(self, new_email):
        self.email = new_email

    def update_password(self, new_password):
        self.password = new_password

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Birthday: {self.birthday}")


    # Video 4

    @property
    def user_info(self):
        return f"{self.username} ({self.email})"

    @property
    def birth_date(self):
        return self.birthday

    @birth_date.setter
    def birth_date(self, new_birthday):
        self.birthday = new_birthday


user = User("John", 'password', 'john@some.com', '12/25/1999')

print(user.username)
print(user.password)
print(user)


print("\nVIDEO 2: String Representations")

print(str(user))
print(repr(user))


print("\nVIDEO 3: Class Methods")

print(user.get_username())
print(user.get_email())

user.update_email("johnsmith@some.com")
print(user.email)

user.update_password("newpassword")
print(user.password)

user.display_info()


print("\nVIDEO 4: Properties")

print(user.user_info)
print(user.birth_date)

user.birth_date = "12/26/1999"

print(user.birth_date)


# Final User Information

print("\nFinal User Information")

print(user)