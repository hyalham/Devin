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
    print()
        # Deviner le nombre mystère
    if choix == '1':
        # Le programme choisi un nombre au hasard entre 1 et 999 
        nb_myst = randint(1,999)
        print("J'ai choisi un nombre compris entre 1 et 999")
        
        nb_test = 0
        rang_propo = 0
        print()
        # Demander à l'utilisateur d'entrer un nombre
        while nb_test != nb_myst:
            print()
            nb_test = int(input (f'Proposition {rang_propo+1}  '))
            print()
            rang_propo += 1
            #    Le programme répond par "plus grand" "plus petit" ou "trouvé"
            if nb_test > nb_myst:
                print("Trop grand !")
            elif nb_test < nb_myst:
                print("Trop petit !")
            else:
                print(f'Trouvé!')
                print()
        print(f'"Bravo ! Vous avez trouvé en {rang_propo} essais.')
        print()
    # Faire deviner le nombre au programme
    elif choix == '2' :
        #   Deviner un nombre compris entre 1 et 999 soit choisi par l'utilisateur 
        #   Assigneation des variables
        print()
        oui_non = input('Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ?')
        while oui_non != 'o':
            oui_non = input('J\'attends...')
        up = 999
        down = 1
        rang_propo = 0
        rang = '0'  # "Plus Grand" ou "Plus Petit"
        machine_number = 0
        stop = False
            #   Repeter une demande d'evaluation
        while not stop :
            # Calculer la valeur mediane de cet intervale
            rang_propo += 1
            machine_number = int((up + down) // 2)
            # Indiquer si le nombre proposé est trop grand, trop petit outrouvé
            print()
            print(f"Proposition {rang_propo} : {machine_number}")
            print()
            rang = input("Trop (g)rand, trop (p)etit ou (t)rouvé ?")
            print()
            #   Verifier la position du nombre dans l'intervale et si l'utilisateur a triché
            if rang == 'p':
                if down < machine_number and (up- down) != 0 :
                    down = machine_number + 1
                else:
                    stop = True
            elif rang == 'g':
                if up > machine_number and (up - down) != 0 :
                    up = machine_number - 1
                else:
                    stop = True
            elif rang == 't' :
                stop = True
            else :
                print("Je n'ai pas compris la réponse. Merci de répondre :")
                print("g si ma proposition est trop grande")
                print("p si ma proposition est trop petite")
                print("t si j'ai trouvé le nombre")
                rang_propo -= 1
        if rang =='t':
            print(f"J'ai trouvé en {rang_propo} essais.")
            print()                

print('Au revoir...')




