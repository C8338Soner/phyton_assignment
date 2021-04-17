# Password reminder.
user_name = "Joseph"
password = "D45622_dds"

name = input("Enter your name: ")

if name in user_name:
    print("Hello {} \b!, password is :{}".format(user_name, password))
else:
    print("Hello ", name, "\b""! See you later.")
