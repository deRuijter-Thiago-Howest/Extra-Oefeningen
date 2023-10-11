# Schrijf een functie uber_eats die twee parameters heeft: aantal pizza’s en aantal dranken. Bereken
# hoeveel deze bestelling kost (een pizza kost €9,99 en een drankje €2). Vergeet niet om € 2,50
# leveringskosten per bestelling toe te voegen
# Je roept de functie twee keer op.


def uber_eats(aantal_pizzas:int,aantal_dranken:int) -> float:
    if Soort == 'B':
        prijs_pizzas = aantal_pizzas * 9.99
        prijs_dranken = aantal_dranken * 2
        Totaal = prijs_pizzas + prijs_dranken + 2.50
        return Totaal
    elif Soort == 'A':
        prijs_pizzas = aantal_pizzas * 9.99
        prijs_dranken = aantal_dranken * 2
        Totaal = prijs_pizzas + prijs_dranken
        return Totaal
    

Soort = str(input("Kies 'B' voor: Bestelling of 'A' voor afhaling :> "))

pizzas = int(input("Geef het aantal pizza's op:>"))   #afwerking

Bestelling1 = print(f"De bestelling van 2 pizzas en 3 drankjes is {uber_eats(pizzas,3)}")
Bestelling2 = print(f"De bestelling van 10 pizzas en 2 drankjes is {uber_eats(10,2)}")



