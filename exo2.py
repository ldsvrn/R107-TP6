def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst


lst1 = [1, 2, 3]
lst2 = ajouter_elt(lst1, len(lst1))

print(lst1, lst2)
print(f"{type(lst1)} {id(lst1)} \n{type(lst2)} {id(lst2)}")
# les ids sont les mêmes
