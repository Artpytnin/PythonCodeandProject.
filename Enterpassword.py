import random
import math

character = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
special = "!@=/+-*="
password_length = int(input("Enter password length"))


if password_length < 8 :
    print("\npassword Length must be atleast 10")
    exit()

elif password_length > 15 :
   print("\npassword Length must be atleast 12")
   exit()
   character = password_length // 2
   number_length = math.ceil(user_length * 25 / 100)

character_length = password_length

def generate_randoms(length , array , character = False) :
    result = []
    for i in range(length) :
        index = random.randint(0 , len(array) + 1)
        character = array [index]
if character :
    case = random.randint(0 , 1)
    if case == 1 :
        character = character.upper()
    


buffer = []
buffer.extend (generate_randoms(character_length , character , True))
buffer.extend (generate_randoms(number_length , number , ))
random.shuffle (buffer)
user = "" .join([str(i) for i in buffer])
print("\nGenerated password: \n")
