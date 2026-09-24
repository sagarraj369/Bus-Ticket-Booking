class user:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class admin(user):
    def delete_user(self):
        print("Admin deleted a user")
      
a = admin("sagar m")
b = user("bhanu")
c = user("sanjana")
_input = input("Enter your username: ")

if _input == a.admin:
    print(a.admin)
    print("  ------------------")
    print(" | you are an admin | ")
    print("  ------------------")
elif _input == b.username:
    print(b.user)
    print("you are a regular user")
    
elif _input == c.username:
    print(c.user)
    print("you are a regular user")
   
else:
    for i in range(3):
        print("User not found")
        print("Please enter a valid username")
        break

        