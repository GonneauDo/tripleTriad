import vs
import ia1
import ia2
from subprocess import call

print('''Joueur contre Joueur :   0
Joueur contre IA :       1''')
redo = True
while redo:
    try:
        versus = int(input())
        redo = False
        if versus > 1:
            redo = True
            print("Valeur incorrecte")
    except:
        print("Valeur incorrecte")
if versus == 0:
    call(['python3','vs.py'])
else:
    print('''Difficulté :
        Facile     : 0
        Difficile  : 1''')
    redo = True
    while redo:
        try:
            difficulte = int(input())
            redo = False
            if difficulte > 1:
                redo = True
                print("Valeur incorrecte")
        except:
            print("Valeur incorrecte")
    if difficulte == 0:
        call(['python3','ia1.py'])
    else:
        call(['python3', 'ia2.py'])
