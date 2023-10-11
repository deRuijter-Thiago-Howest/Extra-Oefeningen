# Je vraagt twee getallen. Je geeft de melding “het eerste getal is groter dan het tweede” of “het tweede
# getal is groter dan het eerste”.

getal1= int(input("Geef hier de eerste getal op :> "))
getal2= int(input("Geef hier de tweede getal op :> "))

if getal1 > getal2:
    print(f"{getal1} is groter dan {getal2}")
elif getal2 > getal1:
    print(f"{getal1} is kleiner dan {getal2}")
elif getal1 == getal2:
    print(f"{getal1} is even groot als {getal2}")
else:
    print("foutieve input")