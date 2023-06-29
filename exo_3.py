#création de la fonction afficher_info
def afficher_info(dico):
    print(f"Nom : {dico['nom']}")
    print(f"Prénom : {dico['prenom']}")
    print(f"Age : {dico['age']}")
    print(f"Matière Préférée : {dico['matiere preferee']}")

#création du dictionnaire student
student = {
    "nom" : "Kechiche",
    "prenom" : "Sandess",
    "age" : "24 ans",
    "matiere preferee" : "Maths",
}

#appelle de la fonction "afficher_info" avec pour paramètre "student"
afficher_info(student)
