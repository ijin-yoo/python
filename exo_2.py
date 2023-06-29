#création d'une liste contenant 5 pays
pays = ["France", "Angleterre", "Grèce", "Tunisie", "Maroc"]
print(pays)

#ajout d'un 6ème pays
pays.append("Corée du Sud")
print(pays)

#affichage du 3ème élément de la liste
print(pays[2])

#modification du 2ème élément de la liste
pays[1] = "Espagne"
print(pays)

#suppression du 4ème élément de la liste
del pays[3]
print(pays)