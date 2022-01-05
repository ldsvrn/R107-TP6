L1 = [0] * 3

print(f"- Liste: {L1}\n- Type: {type(L1)}\n- ID: {id(L1)}\n")

for i in L1:
    print(f"- Type: {type(i)}\n\t- ID {id(L1)}\n")

L1[1] += 1

print(f"- Liste: {L1}\n- Type: {type(L1)}\n- ID: {id(L1)}\n")

for i in L1:
    print(f"- Type: {type(i)}\n\t- ID {id(L1)}")

# Tous les éléménts de la liste on le même ID, on peut bien dire que les listes sont mutables.
