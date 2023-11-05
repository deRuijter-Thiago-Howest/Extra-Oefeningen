
def geef_provincie(postcode:int) -> str:
    if postcode >= 8000 and postcode <= 8999:
        return "West-Vlaanderen"
    elif postcode >= 9000 and postcode <= 9999:
        return "Oost-Vlaanderen"
    elif postcode >= 2000 and postcode <= 2999:
        return "Antwerpen"
    elif postcode >= 3500 and postcode <= 3999:
        return "Limburg"
    elif postcode >= 1500 and postcode <= 1999 or (postcode >= 3000 and postcode <= 3499):
        return  "Vlaams Brabant"

# Maak een functie geef_aantallen_per_provincie met als parameters: een dictionary met missen.
# Deze functie telt per provincie het aantal missen. De provincies met bijhorende aantallen worden in een nieuwe dictionary
# terug gegeven. Test uit door de teruggegeven dictionary nadien uit te printen.
# Opmerking: maak hier handig gebruik van de functie uit oefening 1 om bij elke miss eerst de provincie te bepalen.
misses_2018 = {"Tine" : 3700, "Anke" : 8700, "Claudia": 8530, "Marijn": 9000, "Sofie":
2650, "Marie" : 9870, "Leen" : 9000, "Conny" : 2800}
misses_2019 = {"Marieke" : 8800, "Delfien" : 8500, "Mieke": 8531, "Els": 9070, "Lola":
2500, "Dolly" : 9999, "Marianne" : 9000, "Claudine" : 2800, "Lies" : 3080, "Jacqueline" : 3720, "Jozefien"
: 8700}

from typing import Dict
from typing import List

def geef_aantallen_per_provincie(missen_dict:Dict[str,int]) -> Dict:
    resultaat = {}

    for postcode in missen_dict.values():
        provincies = geef_provincie(postcode)
        
        if provincies not in resultaat:
            resultaat[provincies] = 1
        else:
            resultaat[provincies] += 1

    return resultaat      

        


        
        

test = geef_aantallen_per_provincie(misses_2018)
print(test)

        


