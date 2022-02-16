files = open("02.16.py","r")

#print(files.read())

for line in files:
    print(line,end="")

files.close()


with open("02.16.py","r") as file:
    for line in file:
        print(line,end="")

# with = this is a context manager, which close a file at the end