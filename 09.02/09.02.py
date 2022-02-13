# Regularni vyrazy
# Regex = regularni vyraz

import re

my_text = "Slon je sedivy, ma chobot a kly. Jeho telefon je 777123456. Zije v Africe"

my_text = "Slon je sedivy, ma chobot a kly. Jeho telefon je  abcabc-777123456. Zije v Africe"


# my_text.find("chobot")
# \d = jakakoliv cislice
# r = raw string
# ? - je anebo neni 
# debuggex.com
# regerx.com
# * jedna a nebo vic
# + minimalne jednou
# \b hranice slova \bjablko\b
# ^ na zacatku najde a ukonci
# $ na konci hleda
# \w{3} najde 3 znaky za sebou
# | nebo
# \s whitespace
# () skupina
# {} kolikrat je ten znak pred tim
# [] vycet (cokoliv ze znaku v zavorkach)
# [^] vycet ale negace (cokoliv krome znaku v zavorkach)


regex = re.compile(r"(\d\d\d)(\d\d\d\d\d\d)")
regex_2 = re.compile(r"(\d{3}-?\d{6}")
regex_3 = re.compile(r"\d{3,7}-?\d{6,20}")

regex_4 = re.compile(r"((abc){,4})-?(\d{6,10}")

result = regex.search(my_text)

print(f"Predvolba je {result.group(1)}")
print(f"Samotne cislo je {result.group(2)}")
print(f"Cele cislo je {result.group()}")
print(f"Cele cislo je {result.group(0)}")
### Examples:

import re

retezec = "U nas bydli zeleny pav."
# hledam slovo prav nebo pravo

regex = re.compile(r"pr?avo?")
result = regex.search(retezec)
print(result.group())

retezec2 = "Mame doma modry plot."
# hledam slovo plot nebo plod

regex2 = re.compile(r"plot|plod")
regex_2 = re.compile(r"plo(d|t)") 

result2 = regex2.search(retezec2)
result_2 = regex_2.search(retezec2)

print(result2.group())
print(result_2.group())
