import string
import random


scaps = string.ascii_uppercase
slow = string.ascii_lowercase
sdig = string.digits
spunct = ['@','$','_','&']

pcaps = random.choice(scaps)
plow = random.choice(slow)
pdig = random.choice(sdig)
ppunct = random.choice(spunct)

print("Your Password : ", pcaps+plow+ppunct+pdig)




