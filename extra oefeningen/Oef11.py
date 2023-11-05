# Schrijf een functie hoelang_nog met 2 parameters: het vertrekuur en de vertrekminuten van de trein.
# Reken aan de hand van de huidige tijd uit hoeveel minuten je nog hebt om de trein te halen.
# Rekenvoorbeeld 1 :
# Stel de het is nu 16:15, de trein vertrekt om 16:30
# (16*60 minuten + 15 minuten) = 975 minuten
# (16*60 minuten + 30 minuten) = 990 minuten
# 990 minuten – 975 minuten = 15 minuten te wachten
# Rekenvoorbeeld 2 :
# Stel de het is nu 16:15, de trein vertrekt om 18:34
# (16*60 minuten + 15 minuten) = 975 minuten
# (18*60 minuten + 34 minuten) = 1114 minuten
# 1114 minuten – 975 minuten = 139 minuten te wachten
import datetime
huidige_tijd = datetime.datetime.now()
aangepast_formaat = int(huidige_tijd.strftime("%H"))
aangepast_formaat2 = int(huidige_tijd.strftime("%M"))

def hoelang_nog(vertrekuur:int, vertrekminuten:int) -> int:
    tijd1 = (aangepast_formaat * 60 + aangepast_formaat2)
    tijd2 = (vertrekuur * 60 + vertrekminuten)
    wachttijd = tijd2 - tijd1
    return wachttijd



vertrekuur = int(input("Geef hier de vertrekuur van de trein op:>  "))
vertrekminuten = int(input("Geef hier de vertreminuten van de trein op:>  "))


print(f"Je hebt nog {hoelang_nog(vertrekuur,vertrekminuten)} minuten om de trein te halen")



