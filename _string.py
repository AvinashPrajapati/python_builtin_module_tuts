import string

# string = "\thello"
# print(string)

######### whitespace ddd      sdsd
# sample = "\tHello, world  \t"
# print(sample)

# whitespace = string.whitespace  #\t \n
# # cleaned = ''.join(char if char not in whitespace else '' for char in sample)

# cleaned = sample.strip(whitespace)

# print(cleaned)

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print("ram".capitalize())
# print(string.capwords("ram"))
# print(string.digits)
# print(string.hexdigits)  #  #7abf4R
# print(string.octdigits) 
# print(string.hexdigits) 
# print(string.printable)  #  all possible strring chars
# print(string.punctuation)   # string symbols

sample = "Ram is very {}good Ram"

# print(type(sample))

# output = sample.capitalize()
# output = sample.casefold()
# output = sample.count('Ram')
# output = sample.center(1)
output = sample.format(6)

print(output)















