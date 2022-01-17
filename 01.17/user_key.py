dict_of_keys = {
    "Andy":"adc86",
    "Mike":"post82",
    "Kail":"asdv190"
    }

def user():
    while True:
        key = dict_of_keys[input("Napiste uzivatel jmeno ")]
        value = dict_of_keys[key[input("Napiste heslo ")]]
        if key == dict_of_keys.keys(key):
            if str(value) == dict_of_keys.values(value):
                print("Jste prihlasen")
            else:
                print("Napiste spavne heslo")
        else:
            print("Napiste spravneho uzivatele") 

user()