# Schrijf een functie loon_met_index die uitrekent hoeveel je zal verdienen na de volgende overschrijding
# van de spilindex. Indien de spilindex overschreden wordt, stijgen de lonen met 2%.
# Toon de verschillende lonen die je vorig jaar verdiende, als je weet dat de spilindex 5 keer overschreden
# werd.

def loon_met_index(loon:int) -> float:

    nieuw_loon = loon + (loon / 100 * 2)
    return nieuw_loon


loon = int(input("Geef uw loon weer:> "))
nieuw_loon = loon_met_index(loon)
print(f"Uw loon in januari is {nieuw_loon} euro")
nieuw_loon = loon_met_index(nieuw_loon)
print(f"Uw loon in maart is {nieuw_loon} euro")
nieuw_loon = loon_met_index(nieuw_loon)
print(f"Uw loon in juni is {nieuw_loon} euro")
nieuw_loon = loon_met_index(nieuw_loon)
print(f"Uw loon in september is {nieuw_loon} euro")
nieuw_loon = loon_met_index(nieuw_loon)
print(f"Uw loon in januari is {nieuw_loon} euro")





