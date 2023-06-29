#on récupère dans des variables 2 nombres entrez par l'utilisateur
nb1 = float(input("Entrez un nombre : "))
nb2 = float(input("Entrez un nombre : "))

#calcul de la somme
sum = nb1 + nb2

#calcul de la différence
sub = nb1 - nb2

#calcul du produit
pro = nb1 * nb2

#calcul du quotient
quo = nb1 / nb2

#affichage des résultats
print("La somme des deux nombres est :", sum)
print("La différence entre", nb1, "et", nb2, "est :", sub)
print("La produit des deux nombres est :", pro)
print("La quotient de la division de", nb1, "par", nb2, "est :", round(quo, ndigits=2))