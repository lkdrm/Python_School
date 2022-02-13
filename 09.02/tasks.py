"""
1. Napište regex, který najde slovo LES, LED nebo LEV.

2. Napište regex, který najde slovo HAD nebo HRAD.

3. Napište regex, který najde slovo ZAHRADA, OHRADA, PODHRADÍ nebo HRADBY.

4. Napište regex, který najde slovo končící na -NOST (např. spravedlnost).

5. Napište regex, který najde mezeru (nebo i jiný bílý znak) následující po čárce, tečce, dvojtečce 
    nebo středníku.

6. Napište regex, který najde slovo o délce minimálně 7 znaků.

7. Napište regex, který najde slovo neobsahující písmeno o (nebo O).

8. Napište regex, který najde telefonní číslo ve formátu tři číslice, mezera,
tři číslice, znovu mezera a nakonec znovu tři číslice.

9. Vylepšete regex ze cvičení 8 o českou mezinárodní předvolbu.

10. Napište regex, který ověří email. Pojďme se domluvit, že emaily zjednodušíme -
email začíná na písmena včetně číslic a teček, pak je zavináč, pak opět číslice a písmena,
přesně jedna tečka a nakonec dva nebo tři písmenné znaky. (Skutečné regexy pro emaily bývají 
mnohem složitější, tím se nebudeme zabývat - dají se vygooglit.)

Pro začátek můžete pracovat v prostředí https://www.debuggex.com/
nebo https://regexr.com/.
Všechny regexy si ale později vyzkoušejte v terminále na opravdických řetězcích.

"""
#1 task: ready
#  Napište regex, který najde slovo LES, LED nebo LEV.

import re

my_text = "This notebook have a ledlight"

regex = re.compile(r"(le(s|d|v))")

result = regex.search(my_text)
print(result.group())

#2 task:
#    Napište regex, který najde slovo HAD nebo HRAD.
import re

my_text_2 = "Some people say - hrad. But I have had"

regex_2 = re.compile(r"(hr?ad?)")

result_2 = regex_2.search(my_text_2)
print(result_2.group())

#3 task:
#   Napište regex, který najde slovo ZAHRADA, OHRADA, PODHRADÍ nebo HRADBY.
import re

my_text_3 = "Napište regex, který najde slovo zahrada, ohrada, podhradi nebo hradby"

regex_3 = re.compile(r"((za|o|pod)?hrad(a|i|by))")# or [zaopd]*hrad[aiby]+

result_3 = regex_3.search(my_text_3)
print(result_3.group())