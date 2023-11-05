# Schrijf een functie vertaal met twee parameters: taal en woord. De functie vertaalt het woord naar de
# gevraagde taal. Enkel volgende woorden moeten in het Frans of Engels kunnen vertaald worden.
# Voor de eenvoud gaan we er vanuit dat elk woord in kleine letters opgegeven

def vertaal(taal:str,woord:str) -> str:
    if taal == 'frans' and woord == 'hond':
        vertaling = print(f"De franse woord voor hond is 'Chien' ")
        return vertaling
    elif taal == 'engels' and woord == 'hond':
        vertaling = print("De engelse woord voor hond is 'Dog' ")
        return vertaling
    elif taal == 'engels' and woord == 'kat':
        vertaling = print("De engelse woord voor kat is 'Cat' ")
        return vertaling
    elif taal == 'frans' and woord == 'kat':
        vertaling = print("De franse woord voor kat is 'Chat' ")
        return vertaling
    elif woord != 'hond' and woord != 'kat' and taal == 'frans':
        vertaling = print("Ongeldig Woord")
        return vertaling
    elif woord != 'hond' and woord != 'kat' and taal == 'engels':
        vertaling = print("Ongeldig Woord ")
        return vertaling
    else:
        print("foutieve input")
   




Woord = str(input("Geef hier de te vertalen woord  :> "))
Taal = str(input("Geef hier de taal naar waar het woord vertaald wordt (frans of engels) :> "))

vertaal(Taal,Woord)