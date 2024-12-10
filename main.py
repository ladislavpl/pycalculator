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

version = "1.2"

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
        case "8":
            a = int(input("Zadej číslo: "))
            c = a
            i = a - 1
            while i >= 1:
                c = c * i
                i = i - 1
            print("Výsledek: ", c, "\n")
        case "9":
            print("1. c² = a² + b²")
            print("2. a² = c² - b²")
            print("3. b² = c² - a²")
            akce = int(input("Vyber akci: "))
            match akce:
                case 1:
                    a = float(input("Zadej a: "))
                    b = float(input("Zadej b: "))
                    c = (a ** 2 + b ** 2) ** (1 / 2)
                    print("c = ", c, "\n")
                case 2:
                    c = float(input("Zadej c: "))
                    b = float(input("Zadej b? "))
                    a = (c ** 2 - b ** 2) ** (1 / 2)
                    print("a = ", a, "\n")
                case 3:
                    c = float(input("Zadej c: "))
                    a = float(input("Zadej a: "))
                    b = (c ** 2 - a ** 2) ** (1 / 2)
                    print("b = ", b, "\n")
                case _:
                    print("Neplatná operace\n")
        case _:
            print("Neplatná operace\n")
