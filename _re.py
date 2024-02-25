import re

########### 1

# pattern = re.compile(r'\d+')  #integer find

# pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')  #email finder

pattern = re.compile(r'#\w+')  #hashtag find
pattern = re.compile(r'@\w+')  # @hashtag find


output = pattern.findall("fi 123 6 @mukesh@ram")

print(output)

####2  for bad words in comment system

# output = re.findall(r'There', 'There is anything important')

# print(output)

