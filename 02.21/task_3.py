with open("carky.txt") as infile, open("output.txt","w") as outfile:
    stars = False
    for line in infile:
        outfile.write(line)
        if not line.endswith(",\n") and not stars:
            stars = True
            outfile.write("**********\n")

with open("output.txt") as file:
    print(file.read())