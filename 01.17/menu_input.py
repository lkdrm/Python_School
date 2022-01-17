menu = {
    "polevka": ["drtsova",30],
    "piti": ["sprite",20],
    "desert": ["dort",40],
}

def klient_menu () :
    klient_list = []
    while True: 
        klient = input("Dobry den zvolte co budete?")
        if klient == "polevka":
            print(klient_list)
            klient_list.append(menu["polevka"][1])
        elif klient == "piti":
            klient_list.append(menu["piti"][1])
        elif klient == "desert":
            klient_list.append(menu["desert"][1])
        elif klient == "ano":
            print("Dohromady zaplatite:",sum(klient_list))
            break 



klient_menu()

