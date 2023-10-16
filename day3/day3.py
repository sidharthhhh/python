# file = open('sid.txt', 'r')  # making the file ready for reading, open mean file is open for specific task
# file = open('sid.txt', 'w')
# file = open('sid.txt', 'a') # this is append mode for adding new content in the file
# content = file.read() # reading the content of file and store in content variable

# line = file.readline() # it will read first line
# lines = file.readlines() # it wil read multiple line or complete file
# print(content)
# print(line)
# print(lines)
# file.close()


# for adding content in file
# file.write("i m leaning python\n") #  this will replace or override the existing content
# file.write('\ni live in bhopal\n')
# print(content)
# file.close() # for best practice close the file.


# ---------------------------------------------------------------------------------
# how to work with directories
import os  # os will help in intracting with operating system.
import os.path
import shutil # we can remove the folder alomg with content of folder
# os.mkdir('folder1') #it will create a directory
# a = os.listdir('.') # for listing the content inside the folder
# print(a)

# for checking weather a file is exist or not 
# x= os.path.exists('sid.txt')
# print("the existing of file sid.txt is :", x) # give result in boolean 

# x= os.path.exists('folder1')
# print(x)

# for removing a directory or folder 
# os.rmdir('folder1')
# a =  os.listdir('.')
# print(a)

# removing a file
# os.remove('sid.txt')

# it will remove folder along with its a content.
shutil.rmtree('folder1')
a=os.listdir('.')
print(a)







