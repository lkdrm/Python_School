import csv

with open("data.csv") as infile:
    csv_file = csv.DictReader(infile,delimiter=",") # or csv.reader(infile,delimiter=",")
    muj_list = []
    for row in csv_file:
        print(row)
        print(f"Jmeno: {row['Jmeno']}, Firma: {row['Pracoviste']}, Plat: {row['plat']}")
        #print(f"Jmeno: {row[0]}, Firma: {row[1]}, Plat {row[3]}")
        muj_list.append(row)

print(muj_list)