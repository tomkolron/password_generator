import sys
import string
import random

if len(sys.argv) < 2:
    print("Add the length as the first command argument")
    sys.exit()
length = int(sys.argv[1])

# Get all alphanumeric characters and special characters
chars = string.ascii_letters + string.digits + string.punctuation
pswrd = []

for i in range(length-1):
    pswrd.append(chars[random.randint(0, len(chars)-1)])


print(''.join(pswrd), end='')

