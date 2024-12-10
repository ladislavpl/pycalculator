import sys
import time

def main(func, operationName):
    while True:
        try:
            pocet = int(input("Zadejte kolik čísel chcete " + operationName + ": "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            break
        if pocet <= 1:
            print("Nelze " + operationName + ". Opakujte akci znovu.\n")
            break
        elif pocet == 2:
            try:
                a = float(input("Zadejte první číslo: "))
                b = float(input("Zadejte druhé číslo: "))
            except ValueError:
                print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                break
            print("Výsledek: ", func(a, b), "\n")
            break
        else:
            i = 2
            try:
                a = float(input("Zadejte první číslo: "))
            except ValueError:
                print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                break
            c = a
            try:
                while i <= pocet:
                    b = float(input("Zadejte další číslo: "))
                    c = func(c, b)
                    i = i + 1
            except ValueError:
                print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                break
            print("Výsledek: ", c, "\n")
            break

version = "1.2.1"

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
                while True:
                    try:
                        a = float(input("Zadejte číslo které chcete umocnit: "))
                        b = int(input("Zadejte exponent: "))
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                        break
                    print("Výsledek: ", a ** b, "\n")
                    break
            case "6":
                while True:
                    try:
                        a = float(input("Zadejte číslo které chcete odmocnit: "))
                        b = int(input("Zadejte exponent: "))
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                        break
                    print("Výsledek: ", a ** (1 / b), "\n")
                    break
            case "7":
                while True:
                    try:
                        nasobilka = int(input("Zadejte násobilku kterou chcete vypsat: "))
                        pocet = int(input("Zadejte počet čísel: "))
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                        break
                    i = 1
                    arrayNasobilka = []
                    while i <= pocet:
                        arrayNasobilka.append(i * nasobilka)
                        i = i + 1
                    print("Výpis násobilky: ", arrayNasobilka, "\n")
                    break
            case "8":
                while True:
                    try:
                        a = int(input("Zadej číslo: "))
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                        break
                    c = a
                    i = a - 1
                    while i >= 1:
                        c = c * i
                        i = i - 1
                    print("Výsledek: ", c, "\n")
                    break
            case "9":
                while True:
                    print("1. c² = a² + b²")
                    print("2. a² = c² - b²")
                    print("3. b² = c² - a²")
                    try:
                        akce = int(input("Vyber akci: "))
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                        break
                    match akce:
                        case 1:
                            try:
                                a = float(input("Zadej a: "))
                                b = float(input("Zadej b: "))
                            except ValueError:
                                print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                                break
                            c = (a ** 2 + b ** 2) ** (1 / 2)
                            print("c = ", c, "\n")
                            break
                        case 2:
                            try:
                                c = float(input("Zadej c: "))
                                b = float(input("Zadej b? "))
                            except ValueError:
                                print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                                break
                            a = (c ** 2 - b ** 2) ** (1 / 2)
                            print("a = ", a, "\n")
                            break
                        case 3:
                            try:
                                c = float(input("Zadej c: "))
                                a = float(input("Zadej a: "))
                            except ValueError:
                                print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                                break
                            b = (c ** 2 - a ** 2) ** (1 / 2)
                            print("b = ", b, "\n")
                            break
                        case _:
                            print("Neplatná operace\n")
                            break
            case _:
                print("Neplatná operace\n")
except KeyboardInterrupt:
    print("Vypínám...")
    time.sleep(1)
