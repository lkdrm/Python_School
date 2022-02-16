import os

print(os.getcwd()) # current working directory

print(os.curdir) # opet current directory, ale ted relativne
print(os.pardir) # parrent directory

file = open("new_txt.txt","r")

read_file_dict = file.readlines()
read_file = file.read()


print(read_file)
file.close()
 
file_2 = open("new_7.txt","w")

file_2.write("Hello\n")
file_2.write("How are you?\n")

file_2.close()

#file_3 = open("new_7.txt","w")

#file_3.write("This is a fourth text")
#file_3.close()

file_3 = open("new_7.txt","a")

file_3.write("This is a third line\n")
file_3.close()

file_for_read = open("new_7.txt","r")
print(file_for_read.read())
file_for_read.close()