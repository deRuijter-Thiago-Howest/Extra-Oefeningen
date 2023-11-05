# Schrijf een functie die bepaalt of een student volledig geslaagd is. Deze functie heeft 6 parameters.
# Indien alle getallen 10 of meer zijn is de student geslaagd, anders krijgt hij/zij/hen de melding dat de
# uitslag pas na de deliberatie duidelijk zal worden.


def geslaagd(score1:int,score2:int,score3:int,score4:int,score5:int,score6:int) -> str:
    if score1 >= 10 and score2 >= 10 and score3 >= 10 and score4 >= 10 and score5 >= 10 and score6 >= 10:
        print("Proficiat, u bent geslaagd!")
    else:
        print("Uw uitslag wordt pas na de deliberatie duidelijk...")


geslaagd(10,9,10,10,10,10)






