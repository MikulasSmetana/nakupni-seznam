def pridat_polozku(seznam):
    polozka = input("Zadejte název položky k přidání: ")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")

def odebrat_polozku(seznam):
    polozka = input("Zadejte název položky k odebrání: ")
    seznam.remove(polozka)
    print(f"Položka {polozka} byla odebrána: ")

