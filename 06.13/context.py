# pomoci finally

import time
f = open("output.txt","w")

time.sleep(1)
try:
    text = f.write("Ahoj")
    print(text)
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Chyba.")
finally:
    print("Tohle se stane vzdy. At je chyba nebo ne.")
    f.close()
#### Context managment:

with open("output.txt","w") as file:
    file.write("Ahoj")

#### 
