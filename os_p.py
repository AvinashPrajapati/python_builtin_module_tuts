import os

# print(os.name)  #posix, nt, os2, ce, java, riscos

# print(os.environ)

# print(os.getcwd())  #return current directory

# os.chdir()

# print(os.listdir('D:\dev\Youtube\pythonStuffs'))

# os.mkdir('D:\dev\Youtube\pythonStuffs\ewdir')
# os.makedirs("/path/to/new/directory", mode=0o777, exist_ok=True)

# os.removedirs('D:\dev\Youtube\pythonStuffs\ewdir')

# os.rmdir()

# os.rename()

# full_path = os.path.join("D:\dev\Youtube\pythonStuffs", "directory", "file.txt")
full_path = os.path.split("D:\dev\Youtube\pythonStuffs")
print(full_path)

# os.path.exists()  #filepath
# os.path.isdir()  #is dir
# os.path.isfile()  #is file