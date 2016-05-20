print("Zadaj meno:")
meno = input()
print("Zadaj heslo:")
heslo = input()
if meno == "Tibor" or heslo == "tajne": # Musí byť správne zadané meno alebo heslo
    print("Úspešne ste sa prihlásili.")
else:
    print("Nesprávne meno a heslo.")
