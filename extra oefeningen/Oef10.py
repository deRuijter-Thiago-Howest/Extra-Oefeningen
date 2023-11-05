# Gezien de verwarmingscrisis mag de verwarming enkel aan in de maanden november tot februari als de
# buitentemperatuur lager is dan 16 graden. Schrijf een functie mag _de_verwarming_aan(graden,
# maandnummer).


def mag_de_verwarming_aan(graden:int,maandnummer:int) -> str:
    if maandnummer == 11 or maandnummer == 12 or maandnummer == 1 or maandnummer == 2 and graden < 16:
        print(f"Mag de verwarming aan in maandnummer {maandnummer} bij {graden} graden buiten? Ja")
    else:
        print(f"Mag de verwarming aan in maandnummer {maandnummer} bij {graden} graden buiten? Neen.")






graden = int(input("Geef hier de temperatuur in:> "))
maandnummer = int(input("Geef hier de maandnummer in :> "))

mag_de_verwarming_aan(graden, maandnummer)