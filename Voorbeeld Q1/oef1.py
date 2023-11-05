# Gezien de ver(w)armingscrisis mag de verwarming enkel aan in de maanden november tot en met februari,
# enkel als de buitentemperatuur lager is dan 16 graden.
# Schrijf hiervoor een functie mag_de_verwarming_aan die twee parameters aanvaardt:
# • een temperatuur in graden.
# • een maandnummer van 1 tot 12.
# De functie controleert de voorwaarden en geeft, afhankelijk van maand en temperatuur, de tekst “Verwarming
# aan!” of “Verwarming uit!” terug.
# Test de functie uit (zie code bronmateriaal):
# Wat is de buitentemperatuur?:> 14.5
# Geef het maandnummer op [1-12]:> 1
# Mag de verwarming aan? > Verwarming aan!


def mag_de_verwarming_aan(temperatuur:float, maandnummer:int) -> int:
    if (maandnummer == 1 or maandnummer == 2 or maandnummer == 11 or maandnummer == 12) and temperatuur < 16:
        return 1
    else:
        return 2


# We wensen hetzelfde voor meerdere dagen in de maanden oktober, november en december te simuleren.
# We werken in twee stapjes:
# 1) Schrijf een functie simuleer_temperaturen_maand die drie parameters heeft: het aantal dagen in de
# maand, de min-temperatuur en de max-temperatuur. Deze functie geeft een list terug met
# willekeurige dagtemperaturen voor elke dag. De gekozen temperatuur ligt tussen het doorgegeven
# min en max (beide grenzen inbegrepen).

from typing import List
from random import randint


def simuleer_temperaturen_maand(dagen:int, min_temp:float, max_temp:float) -> List:
    temperaturen = []
    while len(temperaturen) <= (dagen - 1):
        random_getal = randint(min_temp, max_temp)
        temperaturen.append(random_getal)
    return temperaturen


# 2) Schrijf tenslotte de functie tel_verwarmingsdagen die twee parameters heeft: het maandnummer en
# een list met dagtemperaturen. Deze functie telt het aantal dagen waarop de verwarming zal draaien.
# Maak handig gebruik van de functie ‘mag_de_verwarming_aan’! Dat aantal wordt teruggeven.

def tel_verwarmingsdagen(maandnummer:int, temperaturen:List) -> int:
    aantal_dagen = 0
    if maandnummer == 1 or maandnummer == 2 or maandnummer == 11 or maandnummer == 12:
        for i in temperaturen:
            if mag_de_verwarming_aan(i,maandnummer) == 1:
                aantal_dagen += 1
    return aantal_dagen

            






# temperatuur = float(input("Geef de temperatuur op:> "))
maandnummer = int(input("Geef de maandnummer op:> "))
# mag_de_verwarming_aan(temperatuur,maandnummer)

# willekeurige_temps = simuleer_temperaturen_maand(10, 1, 20)
# print(willekeurige_temps)

# aantal_dagen = int(input("Geef de aantal dagen in de maand op:> "))
# min_temp = int(input("Geef de minimum temperatuur op:> "))
# max_temp = int(input("Geef de maximum temperatuur op:> "))

november = [20, 20, 13, 20, 15, 6, 5, -5, 19, 20, -1, 19,
19, 10, 11, 12, 0, 1, -1, -2, -4, 9, 2, 19, 8, 13, -5, -1, 3, 5]

december = [1, -10, 12, -6, -9, 13, 12, 0, 11, -3, 11, 2, -
3, 0, 11, 9, 13, 15, -3, 3, 17, 14, 11, -10, 15, 5, -10, 1, 11, -5, -4]

vermarming = tel_verwarmingsdagen(maandnummer,december)
print(vermarming)


