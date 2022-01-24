"""
1.) Vytvořte funkci, která vezme slovo 
a vytvoří z něj slovo v Pig Latin
a) Když slovo začíná samohláskou, přidá se na konec "way"
b) Když slovo začíná souhláskou, souhláska se odebere, přidá se na konec 
a za ní se přidá "ay"
air => airway
ear => earway
elephant => elephantway
computer => omputercay
cat => atcay
papaya => apayapay

2.) Těžší verze:
Pokud je v daném slově první písmeno velké, 
bude velké první písmeno i ve výsledku
Computer => Omputercay

3.) Ještě těžší verze: 
Slovo může mít na konci tečku nebo čárku -
pokud tam je, bude na konci i ve výsledku
"computer," => "omputercay,"

4.) To samé, ale s celou větou (věta se nejdříve
rozdělí na slova, nakonec se zase spojí)
- můžete použít funkci ze cvičení jedna,
nemusíte uvažovat diakritiku a velká písmena

5.) Ještě jeden tajný dětský jazyk, tentokrát se jmenuje Ubbi Dubbi
Napište funkci, která vezme slovo, vytvoří
z něj nové slovo a před každou samohlásku přidá písmena "ub"
octopus => uboctubopubus

-----------------------------------------------------------------------------------------------------------------------

Pokud chcete další cvičení, tak zde (ale spíše jako domácí úkol):
1.) Spočítejte, kolik je ve slově samohlásek (ale pokud jste zvládli 
to předtím, tak tohle bude dost lehké)
"elephant" => 3

2.) Spočítejte, kolikrát se ve slově vyskytuje sekvence "bob"
'azcbobobegghakl' => 2

3.) Napište funkci, která vezme řetězec a seřadí písmena v něm 
podle abecedy

4.) Těžší úkol:
Napište funkci, která vezme řetězec, a najde nejdelší podřetězec, 
ve kterém jsou písmena řazená podle abecedy
'azcbobobegghakl' => 'beggh'

5.) Caesarova šifra - písmenka se posunou na další písmenko v abecedě
a => b
b => c
c => d
z => a

ahoj => bipk (posun o jedna)
ahoj => dkrm (posun o tři)

6.) Ceasarova šifra naopak - rozkódovat
"""

#First task:
# samohlasky =  a, e, i/y, o, u;
# souhlásky = h, ch, k, r, d, t, n, b, f, l, m;
word = "air"
word_2 = "computer"
def find_and_change(word):
    change = list(word)
    if change[0] in "aeiyou":
        change[-1] += "way"
        return "".join(change)
    else:
        change[-1] += change[0]
        change[0] = ""
        change[-1] += "ay"
        return "".join(change)
# computer => omputercay


print(find_and_change(word_2))
print(find_and_change(word))

# retezec = "air"
# retezec += "way"

# retezec = "computer" 
# retezec[1:] + retezec[0] + "ay"