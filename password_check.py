correct_password = "Admin123"
name = input("Enter name: ")
surname = input("Enter Surname: ")
password = input("Enter passward: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

message = "Hi %s %s, you are logged in" % (name,surname)
print(message)