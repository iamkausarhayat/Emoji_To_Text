import random
char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFIGKLMNOPQRSTUVWXYZ!@#$%^&*()"
length = int(input("Enter length: "))
password = ""
for a in range(length):
    password += random.choice(char)
    print(password)