import random


# Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs comprises entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    lst = []
    for i in range(nbr):
        lst.append(random.randint(vmin, vmax))
    return lst


# Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs
# d'un tableau 'table' inférieures à la valeur 'vseuil'
def combienInferieur(table, vseuil=25):
    count = 0
    for i in table:
        if i < vseuil:
            count += 1
    return count


nb = int(input("Combien de nombres voulez vous: "))
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)

yesno = input("Voulez vous préciser le seuil? [o/n]: ")
seuil = 0
if yesno == "o" or "oui":
    seuil = 30
else:
    seuil = 25

total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
