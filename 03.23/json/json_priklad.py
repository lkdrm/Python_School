import json

data = {
    "jmeno": "Petr",
    "vek":23,
    "sporty": ["fotbal","basketball","hokej"],
    "znamky":(1,1,2,3,5),
    "pije-pivo":False,
    "domaci zvire": {
        "jmeno": "Chubaka",
        "rasa": "Mein coon",
        "povolani": "Mazlit"
    }
}

with open("data.json","w") as infile:
    json.dump(data,infile, indent=4)

retezec = json.dumps(data,indent=4)

print(retezec)