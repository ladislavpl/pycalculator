import sys
import time

def main(func, operationName):
    pocet = int(input("Zadejte kolik čísel chcete " + operationName + ": "))
    if pocet <= 1:
        print("Nelze " + operationName + ". Opakujte akci znovu.\n")
    elif pocet == 2:
        a = float(input("Zadejte první číslo: "))
        b = float(input("Zadejte druhé číslo: "))
        print("Výsledek: ", func(a, b), "\n")
    else:
        i = 2
        a = float(input("Zadejte první číslo: "))
        c = a
        while i <= pocet:
            b = float(input("Zadejte další číslo: "))
            c = func(c, b)
            i = i + 1
        print("Výsledek: ", c, "\n")

version = "1.1"

print("Kalkulačka")
print("Verze: ", version, "\n")

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
            a = float(input("Zadejte číslo které chcete umocnit: "))
            b = int(input("Zadejte exponent: "))
            print("Výsledek: ", a ** b, "\n")
        case "6":
            a = float(input("Zadejte číslo které chcete odmocnit: "))
            b = int(input("Zadejte exponent: "))
            print("Výsledek: ", a ** (1 / b), "\n")
        case "7":
            nasobilka = int(input("Zadejte násobilku kterou chcete vypsat: "))
            pocet = int(input("Zadejte počet čísel: "))
            i = 1
            arrayNasobilka = []
            while i <= pocet:
                arrayNasobilka.append(i * nasobilka)
                i = i + 1
            print("Výpis násobilky: ", arrayNasobilka, "\n")
        case _:
            print("Neplatná operace\n")