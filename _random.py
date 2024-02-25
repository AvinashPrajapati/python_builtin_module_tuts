import random

# number between 0 - 1

# num = random.random()

# print("{:.2f}".format(num))

############ random int in range

# int_num = random.randint(0, 100)
# int_num = random.randrange(0, 100, 4)

# print(int_num)

############# suffling the list
# my_list = [i for i in range(0,20)]
# print(my_list)

# random.shuffle(my_list)

# print(my_list)

####################  
# 3354d06a70e1434c86b6c49d61ec5a81
def generate_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0,9))
    return otp

otp = generate_otp()
print(otp)

import argparse  #######
