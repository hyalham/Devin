#   Deviner un nombre compris entre 1 et 999 soit choisi par le programme, soit choisi par l'utilisateur 
from random import randint
    #   Afficher un menu pour 1-Deviner ou 2-Faire deviner ou 3-Stop
    
choix = '3'

while choix != '0':
    # Orienter vers une option
    print("1. L'ordinateur choisit un nombre et vous le devinez")
    print("2. Vous choisissez un nombre et l'ordinateur le devine")
    print("0. Quitter le programme")
    print()
    choix = input("Votre choix : ")
        # Deviner le nombre mystère
    if choix == '1':
        # Le programme choisi un nombre au hasard entre 1 et 999 
        print("J'ai choisi un nombre compris entre 1 et 999")
        nb_myst = randint(1,999)
        nb_test = 0
        rang_propo = 0
        print()
            # Repeter une demande de proposition avec option trouvé pour sortir ataumatiquement de la boucle
        while nb_test != nb_myst:
            rang_propo += 1
            print()
            nb_test = int(input (f'Proposition {rang_propo}  '))
            print()
            #    Le programme répond par "plus grand" "plus petit" ou "trouvé"
            if nb_test > nb_myst:
                print("Trop grand !")
            elif nb_test < nb_myst:
                print("Trop petit !")
            else:
                print(f'"Bravo ! Vous avez trouvé en {rang_propo} essais.')
                print()
    # Faire deviner le nombre au programme
    elif choix == '2' :
        #   Deviner un nombre compris entre 1 et 999 soit choisi par l'utilisateur 
        #   Assigneation des variables
        oui_non = None
        while oui_non == 'n':
            oui_non = int(input('Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ?'))
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
                # if hypothese 
                if down < machine_number and (machine_number - down) > 1 :
                    down = machine_number + 1
                else:
                    up = 999
                    down = 1
                # print(down, up)
            elif rang == 'g':
                if up > machine_number and (up - machine_number) > 1 :
                    up = machine_number - 1
                else:
                    up = 999
                    down = 1
                # print(down, up)
            elif rang == 't' :
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




