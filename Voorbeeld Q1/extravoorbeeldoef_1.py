# Vervolledig de functie geef_provincie die voor een doorgegeven postcode (parameter) de juiste provincienaam teruggeeft.
# We beperken ons tot de provincies uit Vlaanderen.
# Er geldt dat:
# • West-Vlaanderen: postcodes tussen 8000-8999
# • Oost-Vlaanderen: postcodes tussen 9000-9999
# • Antwerpen: postcodes tussen 2000-2999
# • Limburg: postcodes tussen 3500-3999
# • Vlaams-Brabant: postcodes tussen 1500-1999 en 3000-3499
# Test deze functie uit door aan de gebruiker een postcode op te vragen.

def geef_provincie(postcode:int) -> None:
    if postcode >= 8000 and postcode <= 8999:
        West = print("U bent in de provincie West-Vlaanderen")
        return West
    elif postcode >= 9000 and postcode <= 9999:
        Oost = print("U bent in de provincie Oost-Vlaanderen")
        return Oost
    elif postcode >= 2000 and postcode <= 2999:
        Antw = print("U bent in Antwerpen")
        return Antw
    elif postcode >= 3500 and postcode <= 3999:
        Limb = print("U bent in Limburg")
        return Limb
    elif postcode >= 1500 and postcode <= 1999 or (postcode >= 3000 and postcode <= 3499):
        Vla = print("U bent in de provincie Vlaams-Brabant")
        return Vla

postcode = int(input("Geef hier een postcode: "))

geef_provincie(postcode)
