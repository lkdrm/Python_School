#Tasks:

my_dict = {
    "name":"Pavel",
    "year":29,
    "sports":["football","basketball","hokey"],
}
my_dict["high"] = 176
my_dict["man"] = True

print(my_dict.values())

print(my_dict.keys())

for key,value in my_dict.items():
    print(f"{key}--{value}")