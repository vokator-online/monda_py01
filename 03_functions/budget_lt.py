""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""
biudzetas = {}

def prideti_pajamas_isskaiciuoti_balansa(paskirtis, suma):
    if paskirtis not in biudzetas:
        biudzetas[paskirtis] = 0
    biudzetas[paskirtis] += suma

def prideti_islaidas_isskaiciuoti_balansa(paskirtis, suma):
    prideti_pajamas_isskaiciuoti_balansa(paskirtis, -suma)

def spausdinti_zurnala():
    print("Biudžeto turinys:")
    for paskirtis, suma in biudzetas.items():
        print(f"{paskirtis}: {suma}")

def suskaiciuoti_balansa():
    balansas = sum(biudzetas.values())
    print(f"Biudžeto balansas: {balansas}")

# Pavyzdinė naudojimo situacija:
prideti_pajamas_isskaiciuoti_balansa("Atlyginimas", 2000)
prideti_islaidas_isskaiciuoti_balansa("Maistas", 300)
prideti_islaidas_isskaiciuoti_balansa("Kuras", 200)
prideti_islaidas_isskaiciuoti_balansa("Pramogos", 200)
spausdinti_zurnala()
suskaiciuoti_balansa()
