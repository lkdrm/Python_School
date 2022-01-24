retez = "\"ahoj\" jak se mas. Jdu snist \\travu"
retez2 = r"\"ahoj\" \n jak se mas. Jdu snist \\travu"

# escape
# \n = new line
# \t = tab

# with R on start is war string

print(retez)
print(retez2)


year = 25
name = "Vitalik"

#print(f"My name is {name} and i`m {year} years old" )

for znak in name:
    print(znak,end="")

word = "Anicka ma rada banany"

print(word.split(" ",2))

word_2 = ["anicka","ma","rada","banany"]
print(" ".join(word_2))
