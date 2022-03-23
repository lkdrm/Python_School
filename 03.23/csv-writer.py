import csv

muj_list = [
            ['Anna','Google a.s','23','50000'],
            ['Pavel','Microsoft','39','40000'],
            ['Petr','Microsoft','65','100000'],
            ['Monika','Github','43','60000'],
            ]
"""
with open("nova_data.csv","w",newline="") as outfile:
    zapisovac = csv.writer(outfile,delimiter = ",")
    for rada in muj_list:
        zapisovac.writerow(rada)
"""
with open("nova_data_2.csv","w",newline="") as outfile:
    zapisovac = csv.DictWriter(outfile,fieldnames=["jmeno","prijmeni","vek"])
    zapisovac.writeheader()
    zapisovac.writerow({"jmeno":"Anna", "prijmeni":"Novakova","vek":28,})