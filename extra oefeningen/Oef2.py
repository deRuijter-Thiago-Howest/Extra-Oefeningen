# Kopieer de code van oefening 01 en breidt verder uit:
# Je vraagt de naam van de groep en het aantal deelnemers.
# Als ze met meer dan 10 zijn betalen ze vijf euro per deelnemer anders zes euro.
# Toon in de console de boodschap “De prijs voor de groep naamGroep is totaal euro.”

Naam_groep = str(input("Geef hier de naam van de groep op :> "))
aantal = int(input("Geef hier de aantal groepsleden :> "))


if aantal > 10:
    prijs = aantal * 5
    print(f"de groep '{Naam_groep}' is groot")
    print(f"de prijs voor de groep '{Naam_groep}' is {prijs} euro")
elif aantal >= 0 and aantal < 10:
    prijs = aantal * 6
    print(f"de groep '{Naam_groep}' is klein")
    print(f"de prijs voor de groep '{Naam_groep}' is {prijs} euro")
else:
    print("ongeldig")