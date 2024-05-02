# Écrivez votre code ici !
# Création de la liste fruits
fruits = ["pomme","banane","orange"]
print(fruits)

# Ajout de l'élément "kiwi"
fruits.append("kiwi")
print(fruits)

# Suppression de la variable "orange"
# Méthode 1:
fruits.remove("orange")
print(fruits)
# Méthode 2:
del fruits("orange")
print(fruits)

# Modification du deuxième indice en l'élément "ananas"
fruits[1] = "ananas"
print(fruits)

# Affichage de la longueur de la liste fruits
print(len(fruits))

# Triage de la liste fruits par ordre alphabétique
fruits.sort()
print(fruits)

# Fin de l'exercice
