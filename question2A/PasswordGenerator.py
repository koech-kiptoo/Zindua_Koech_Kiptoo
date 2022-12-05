import random
import string

def generatepassword():
    items = ["!","@", "#", "$" , "%", "^", "&", "*", "(", ")"]
    random_item = random.choice(items)
    random_source = string.ascii_letters + string.digits + random_item
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random_item

    # generate other characters randomly
    number = random.randint(4,12)
    for i in range(number):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("First Random Password is ", generatepassword())
