import random
import string
import secrets
#I don't want all punctuation cahracters, so I individually define it
special_characters = "!@#$%^&*"

Combo_pass = string.ascii_lowercase + string.ascii_uppercase + string.digits + special_characters

password = "".join(secrets.choice(Combo_pass) for x in range(6,15))

print(password)


