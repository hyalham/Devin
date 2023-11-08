# Jeu du devin ou comment deviner un nombre choisi au hasard par le programme
from random import randint

#   Le programme choisi un nombre au hasard entre 1 et 999 
print("J'ai choisi un nombre compris entre 1 et 999")
nb_myst = randint(1,999)
nb_test = 0
rang_propo = 0
print()

#   Le programme demande à l'utilisateur de donner un nombre jusqu’à ce qu’il soit trouvé
while nb_test != nb_myst:
    rang_propo += 1
    print()
    nb_test = int(input(f'Proposition {rang_propo} : '))
    print()
    #   Le programme répond par "plus grand" "plus petit" ou "trouvé"
    if nb_test > nb_myst:
        print("Trop grand !")
    elif nb_test < nb_myst:
        print("Trop petit !")
    
else:
    print(f"Bravo ! Vous avez trouvé en {rang_propo} essais.")      
