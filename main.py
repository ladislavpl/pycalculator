def main(func, operationName):
    try:
        pocet = int(input(f"Zadejte kolik čísel chcete {operationName}: "))
    except ValueError:
        return "Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n"
    if pocet <= 1:
        return f"Nelze {operationName}. Opakujte akci znovu.\n"
    elif pocet == 2:
        try:
            a = float(input("Zadejte první číslo: "))
            b = float(input("Zadejte druhé číslo: "))
        except ValueError:
            return "Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n"
        return f"Výsledek: {func(a, b)}\n"
    else:
        try:
            a = float(input("Zadejte první číslo: "))
        except ValueError:
            return "Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n"
        c = a
        for i in range(1, pocet):
            try:
                b = float(input("Zadejte další číslo: "))
            except ValueError:
                return "Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n"
            c = func(c, b)
        return f"Výsledek: {c}\n"

print("Kalkulačka v1.4\n")

try:
    while True:
        operace = input("Vyber operaci (Pro výpis operací, zadej help): ").lower().strip()

        match operace:
            case "help":
                print("""Funkce programu Kalkulačka:
1 - Sčítání
2 - Odčítání
3 - Násobení
4 - Dělení
5 - Mocnina
6 - Odmocnina
7 - Výpis násobilky
8 - Faktoriál
9 - Pythagorova věta
exit - Ukončit aplikaci
help - Výpis funkcí
""")
            case "exit":
                exit(0)
            case "1":
                print(main(lambda a, b : a + b, "sčítat"))
            case "2":
                print(main(lambda a, b : a - b, "odčítat"))
            case "3":
                print(main(lambda a, b : a * b, "násobit"))
            case "4":
                print(main(lambda a, b : a / b, "dělit"))
            case "5":
                try:
                    a = float(input("Zadejte číslo které chcete umocnit: "))
                    b = int(input("Zadejte exponent: "))
                    print(f"Výsledek: {a ** b}\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "6":
                try:
                    a = float(input("Zadejte číslo které chcete odmocnit: "))
                    b = int(input("Zadejte exponent: "))
                    print(f"Výsledek: {a ** (1 / b)}\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "7":
                try:
                    nasobilka = int(input("Zadejte násobilku kterou chcete vypsat: "))
                    pocet = int(input("Zadejte počet čísel: "))
                    arrayNasobilka = []
                    for i in range(pocet):
                        arrayNasobilka.append(i * nasobilka)
                    print(f"Výpis násobilky: {arrayNasobilka}\n")
                except ValueError:
                    print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
            case "8":
                try:
                    a = int(input("Zadej číslo: "))
                    c = a
                    for i in range(a - 1, 0, -1):
                        c *= i
                    print(f"Výsledek: {c}\n")
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
                        print(f"a = {a}\n")
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                elif b == "" and c != "" and a != "":
                    try:
                        b = (float(c) ** 2 - float(a) ** 2) ** (1 / 2)
                        print(f"b = {b}\n")
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu. Opakujte akci znovu.\n")
                elif c == "" and a != "" and b != "":
                    try:
                        c = (float(a) ** 2 + float(b) ** 2) ** (1 / 2)
                        print(f"c = {c}\n")
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
    exit(0)
