#   Deviner un nombre compris entre 1 et 999 soit choisi par l'utilisateur 
from random import randint
    # Faire deviner le nombre au programme
    #   Assigner une valeur au nombre à faire deviner
oui_non = 'n'
while oui_non == 'n':
    oui_non = input('Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ?')
    print('J\'attends...')
            
up = 999
down = 1
rang_propo = 0
rang = '0'  # "Plus Grand" ou "Plus Petit"
machine_number = 0
stop = False
    #   Repeter une demande d'evaluation
while stop == False:
# hypothese = None
        # Calculer la valeur mediane de cet intervale
    rang_propo += 1
    machine_number = int((up + down) / 2)
    # Tester si le nombre est trouvé
    print(f"Proposition {rang_propo} : {machine_number}")
    print()
    rang = input("Trop (g)rand, trop (p)etit ou (t)rouvé ?")
    print()
       #   Verifier la position du nombre dans l'intervale et si l'utilisateur a triché
    if rang == 'p':
        if down < machine_number and (machine_number - down) > 1 :
            down = machine_number + 1
        else:
            up = 999
            down = 1
    elif rang == 'g':
        if up > machine_number and (up - machine_number) > 1 :
            up = machine_number - 1
        else:
            up = 999
            down = 1
    elif rang == 't':
        print(f"J'ai trouvé en {rang_propo} essais.")
        print()
        stop = True
    else :
        print("Je n'ai pas compris la réponse. Merci de répondre :")
        print("g si ma proposition est trop grande")
        print("p si ma proposition est trop petite")
        print("t si j'ai trouvé le nombre")
        rang_propo -= 1

print('Au revoir...')