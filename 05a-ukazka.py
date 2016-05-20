# Čo myslíš, čo tento malý programček robí?
# Čo sa stane, keď ho spustíš pomocou klávesy F5?

def prihlasenie(stav, meno):
    if stav == "uspech":
        print("Úspešne ste sa prihlásili.")
        print("Ako sa máte, " + meno + "?")
        nalada = input()
        print(nalada + "? Ďakujem. Ja sa mám fajn. :)")
    else:
        print("Nesprávne meno alebo heslo. Dovidenia, " + meno + ".")


print("Zadajte meno:")
meno = input()
print("Zadajte heslo:")
heslo = input()
if meno == "Tibor" and heslo == "tajne":
    prihlasenie("uspech", meno)
else:
    prihlasenie("neuspech", meno)
