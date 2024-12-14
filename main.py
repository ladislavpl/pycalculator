import sys
import time

def main(func, operationName):
    try:
        pocet = int(input("Zadejte kolik čísel chcete " + operationName + ": "))
        if pocet <= 1:
            print("Nelze " + operationName + ". Opakujte akci znovu.\n")
        elif pocet == 2:
            a = float(input("Zadejte první číslo: "))
            b = float(input("Zadejte druhé číslo: "))
            print("Výsledek: ", func(a, b), "\n")
        else:
            a = float(input("Zadejte první číslo: "))
            c = a
            for i in range(1, pocet):
                b = float(input("Zadejte další číslo: "))
                c = func(c, b)
            print("Výsledek: ", c, "\n")
    except ValueError:
        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")     

version = "1.3.1"

print("Kalkulačka")
print("Verze: ", version, "\n")
try:
    while True:
        operace = input("Vyber operaci (Pro výpis operací, zadej help): ")

        match operace:
            case "help":
                print("Funkce programu Kalkukačka:")
                print("1 - Sčítaní")
                print("2 - Odčítání")
                print("3 - Násobení")
                print("4 - Dělení")
                print("5 - Mocnina")
                print("6 - Odmocnina")
                print("7 - Výpis násobilky")
                print("8 - Faktoriál")
                print("9 - Pythagorova věta")
                print("exit - Ukončit aplikaci")
                print("help - Výpis funkcí")
                print("\n")
            case "exit":
                print("Vypínám...")
                time.sleep(1)
                sys.exit(0)
            case "1":
                main(lambda a, b : a + b, "sčítat")
            case "2":
                main(lambda a, b : a - b, "odčítat")
            case "3":
                main(lambda a, b : a * b, "násobit")
            case "4":
                main(lambda a, b : a / b, "dělit")
            case "5":
                try:
                    a = float(input("Zadejte číslo které chcete umocnit: "))
                    b = int(input("Zadejte exponent: "))
                    print("Výsledek: ", a ** b, "\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "6":
                try:
                    a = float(input("Zadejte číslo které chcete odmocnit: "))
                    b = int(input("Zadejte exponent: "))
                    print("Výsledek: ", a ** (1 / b), "\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "7":
                try:
                    nasobilka = int(input("Zadejte násobilku kterou chcete vypsat: "))
                    pocet = int(input("Zadejte počet čísel: "))
                    arrayNasobilka = []
                    for i in range(pocet):
                        arrayNasobilka.append(i * nasobilka)
                    print("Výpis násobilky: ", arrayNasobilka, "\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "8":
                try:
                    a = int(input("Zadej číslo: "))
                    c = a
                    for i in range(a - 1, 0, -1):
                        c = c * i
                    print("Výsledek: ", c, "\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "9":
                print("Zanechte jednu proměnnou prázdnou pro její vypočtení nebo vyplnit všechny pro ověření, jestli je trojúhelník pravoúhlý.")
                a = input("Zadej a: ")
                b = input("Zadej b: ")
                c = input("Zadej c: ")
                if a == "" and c != "" and b != "":
                    try:
                        a = (float(c) ** 2 - float(b) ** 2) ** (1 / 2)
                        print("a = ", a, "\n")
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                elif b == "" and c != "" and a != "":
                    try:
                        b = (float(c) ** 2 - float(a) ** 2) ** (1 / 2)
                        print("b = ", b, "\n")
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                elif c == "" and a != "" and b != "":
                    try:
                        c = (float(a) ** 2 + float(b) ** 2) ** (1 / 2)
                        print("c = ", c, "\n")
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                elif c != "" and b != "" and a != "":
                    try:
                        soucet = float(a) ** 2 + float(b) ** 2
                        c2 = float(c) ** 2
                        if c2 == soucet:
                            print("Trojúhelník je pravoúhlý\n")
                        else:
                            print("Trojúhelník není pravoúhlý\n")
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                else:
                    print("Nelze pracovat. Máte více jak jednu prázdnou.\n")
            case _:
                print("Neplatná operace\n")
except KeyboardInterrupt:
    print("\nVypínám...")
    time.sleep(1)
