#Definované Fce
seznam = []
def pridat_polozku(seznam):
    polozka = input("Zadejte název položky k přidání: ")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")

def odebrat_polozku(seznam):
    polozka = input("Zadejte název položky k odebrání: ")
    seznam.remove(polozka)
    print(f"Položka {polozka} byla odebrána: ")
    
def zobrazit_seznam():
    print(f"Seznam obsahuje tyto položky: {seznam}")

def seradit_seznam():
    seznam_sorted = sorted(seznam)
    print("Seznam byl úspěšně seřazen podle abecedy.")
    print(seznam_sorted)

def pocet_polozek():
    size = len(seznam)  
    print(f"Nyní se v seznamu nachází {size} položky.")

def ukoncit_program():
    exit()
