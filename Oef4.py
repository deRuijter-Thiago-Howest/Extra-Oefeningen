# Afhankelijk van het aantal kilometers dat een werknemer van zijn werk woont moet hij een ecologische
# bijdrage betalen voor het gebruik van de bedrijfswagen:
# - Minder dan 50 km geen bijdrage
# - Vanaf 50 km is er een bijdrage van 0,20 euro per gereden km
import math

aantal_km = int(input("Hoeveel kilometers woont u van uw werk? "))

if aantal_km < 50:
    print("U hoeft geen bijdrage te betalen")
elif aantal_km > 50:
    rest_km = aantal_km - 50
    bijdrage = round(rest_km * 0.20, 2)
    print(f"U moet {bijdrage} euro betalen aan brijdage voor het gebruik van de bedrijfswagen")
else:
    print("foutieve input")
