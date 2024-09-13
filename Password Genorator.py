import string 
import secrets

length = int(input("How long do you what your password to be?"))

letters = string.ascii_letters
digits = string.digits
punctuation =  string.punctuation

combined = letters + digits + punctuation

password = ''
for i in range (length):
    password+= ''.join(secrets.choice(combined))

print(password)

file = open("password.csv", "a")
file.write(password)
file.close()
print("Password has been saved to file ")

