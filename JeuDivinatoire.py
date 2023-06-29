from random import*
import sys


BorneMin = 1
BorneMax = 100
NbEssaiMax = 10
print("Bienvenue dans le jeu divinatoire !\n")
print("Essayez de trouver le nombre entier généré par l'ordinateur.\n")
for i in range(2):
    NbAlea = randint(BorneMin, BorneMax)
    Compteur = 1
    while 0 < Compteur <= NbEssaiMax:
        test = False
        while not test:
            NbSaisi = input("Saisissez un nombre entier entre 0 et 100 : ")
            try:
                Nbsaisi = int(NbSaisi)
                test = True
            except:
                print("Erreur. Vous devez saisir un nombre entier.")
                print("Merci de recommencer.\n")
        if 0 <= int(NbSaisi) <= 100:
            if int(NbSaisi) == NbAlea:
                print("Félicitations vous avez réussi en", Compteur, "essai(s) !")
                Compteur = -1
            elif int(NbSaisi) > NbAlea:
                print("Le nombre à trouver est inférieur à", NbSaisi, ".\n")
            else:
                print("Le nombre à trouver est supérieur à", NbSaisi, ".\n")
            Compteur = Compteur + 1
        else:
            print("Erreur. Vous devez saisir un nombre entre 0 et 100.")
            print("Merci de recommencer.\n")
    if Compteur > NbEssaiMax:
        print("Game Over. Le nombre à trouver était", NbAlea, ".")
    print("Vous avez le droit à une seconde partie ! Enjoy !\n")
print("Merci d'avoir joué !")
