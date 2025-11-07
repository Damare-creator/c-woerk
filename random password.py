import random
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-="

ascii_chars = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

restchars = uppercase + lowercase + numbers + symbols + ascii_chars

length = int(input("How long should the password be? (e.g. 12): "))
count = int(input("How many passwords do you want? (e.g. 5): "))

passwords = []

for i in range(count):
    password = ""
    for j in range(length):
        password += random.choice(restchars)
    passwords.append(password)

print("\nYour passwords:")
for i, pwd in enumerate(passwords, 1):
    print(f"{i}. {pwd}")

