# Schrijf een functie waarmee je de maaltijd_met_korting kan berekenen. Deze functie heeft twee
# parameters: het te betalen bedrag en student/docent. Studenten krijgen in het restaurant 20% korting,
# docenten 35%.
# De functie retrouneert enkel het te betalen bedrag

def maaltijd_met_korting(te_betalen:float,rol:str) -> float:
    if rol == 'D':
        korting = te_betalen - (te_betalen / 100 * 35)
        return korting
    elif rol == 'S':
        korting = te_betalen - (te_betalen / 100 * 20)
        return korting
    else:
        print("foutieve input")




te_betalen = float(input("Geef hier de te betalen bedrag :> "))
rol = str(input("Typ 'D' voor 'Docent' en 'S' voor 'Student' :> "))

print(f"Uw totaal te betalen bedrag is {maaltijd_met_korting(te_betalen,rol)}")
