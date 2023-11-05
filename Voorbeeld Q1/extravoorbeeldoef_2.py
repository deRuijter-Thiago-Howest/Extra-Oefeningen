# Voor deze en volgende oefening vertrek je van een dictionary met deelnemers aan een miss-verkiezing.
# De key is de naam van de miss, de value is de postcode.
# In de broncode vind je twee voorbeelden waarmee je kan testen:

# • Maak een functie filter_missen_postcode met als parameters: een dictionary met missen en twee postcodes.
# • In de functie filter_missen_postcode filter je enkel deze missen uit de doorgegeven dictionary waarvan de postcode
# tussen de twee doorgegeven postcodes valt (grenzen inbegrepen).
# • Je geeft de namen van de misses in een list terug.
# • Test uit met bovenstaande dictionaries en print nadien de teruggegeven list af.

misses_2018 = {"Tine" : 3700, "Anke" : 8700, "Claudia": 8530, "Marijn": 9000, "Sofie":
2650, "Marie" : 9870, "Leen" : 9000, "Conny" : 2800}
misses_2019 = {"Marieke" : 8800, "Delfien" : 8500, "Mieke": 8531, "Els": 9070, "Lola":
2500, "Dolly" : 9999, "Marianne" : 9000, "Claudine" : 2800, "Lies" : 3080, "Jacqueline" : 3720, "Jozefien"
: 8700}

from typing import Dict
from typing import List

def filter_missen_postcode(miss_dict:Dict[str, int], min_postcode:int, max_postcode:int) -> List:
    resultaat = []
    for miss, value in miss_dict.items():
        if value >= min_postcode and value <= max_postcode:
            resultaat.append(miss)
    return resultaat

kleinste_postcode = int(input("Geef de kleinste postcode op:> "))
grootste_postcode = int(input("Geef de grootste postcode op:> "))

gefilterde_missen = filter_missen_postcode(misses_2018, kleinste_postcode, grootste_postcode)
print(f"Dit zijn de gevonden missen uit 2018: {gefilterde_missen}")

gefilterde_missen2 = filter_missen_postcode(misses_2019, kleinste_postcode, grootste_postcode)
print(f"Dit zijn de gevonden missen uit 2019: {gefilterde_missen2}")