# Je vraagt de naam van de groep en het aantal deelnemers.
# Als ze met meer dan 10 zijn toon je in de console “de groep ‘naamvandegroep’ is groot” anders toon je
# “de groep ‘naamvandegroep’ is klein”.

Naam_groep = str(input("Geef hier de naam van de groep op :> "))
aantal = int(input("Geef hier de aantal groepsleden :> "))

if aantal > 10:
    print(f"de groep {Naam_groep} is groot")
elif aantal >= 0 and aantal < 10:
    print(f"De {Naam_groep} is klein")
else:
    print("ongeldig")