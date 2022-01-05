def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst


l1, l2 = ajouter_elt(), ajouter_elt()
print(l1, id(l1))
print(l2, id(l2))


# Les IDs sont les même, il s'agit donc du même objet.

def add_char(ch="abc", elt='d'):
    return ch + elt


str1, str2 = add_char(), add_char()
print(str1, id(str1))
print(str2, id(str2))
# Les IDs sont différents, il s'agit d'un élément non mutables.
