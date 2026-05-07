#creiamo le strutture dati 
class Dipendente:
    #costruttore
    def __init__(self, id_dipendente, nome, ruolo, in_ferie=False, in_malattia=False):
        self.id_dipendente = id_dipendente
        self.nome = nome
        self.ruolo = ruolo
        self.in_ferie = in_ferie
        self.in_malattia = in_malattia



 #Creiamo un array fittizzio di dipendenti
personale = [
    Dipendente(1, "Mario Rossi", "bobinatore", in_ferie=True),
    Dipendente(2, "Luigi Bianchi", "conduttore", in_malattia=True),
    Dipendente(3, "Giulia Verdi", "bobinatore"),
    Dipendente(4, "Anna Neri", "conduttore"),
    Dipendente(5, "Paolo Gialli", "bobinatore", in_ferie=True),
    Dipendente(6, "Sara Blu", "conduttore", in_ferie=True)
]

def verifica_vincoli_ferie(lista_personale):
    #verifica se i vincoli imposti dall'azienda vengono rispettati

    totale_ferie = 0
    bobinatori_in_ferie = 0
    conduttori_in_ferie = 0
    for dipendente in lista_personale:
        if dipendente.in_ferie:
            totale_ferie += 1
            if dipendente.ruolo == "bobinatore":
                bobinatori_in_ferie += 1
            elif dipendente.ruolo == "conduttore":
                conduttori_in_ferie += 1
    
    #ora applichiamo le "Rules" imposte dall'azienda

    #Regola 1: Al massimo 4 persone in ferie al giorno
    if totale_ferie > 4:
        print(f"Errore: Troppi dipnendenti in ferie ({totale_ferie}). Massimo consentito: 4.")
        return False
    #Regola 2: Non + di 4 bobinatori in ferie
    if(bobinatori_in_ferie > 4):
        print(f"Errore: Troppi bobinatori in ferie ({bobinatori_in_ferie}). Massimo consentito: 4.")
        return False
    #Regola 3: Non + di 3 conduttori in ferie
    if(conduttori_in_ferie > 3):
        print(f"Errore: Troppi conduttori in ferie ({conduttori_in_ferie}). Massimo consentito: 3.")
        return False
    
    print("Tutti i vincoli sono rispettati. Procedere con la schedulazione.")
    return True


def genera_personale_disponibile(lista_personale):
    #crea una lista di dipendenti disponibili (non in ferie o malattia)
    personale_disponibile = []
    for dipendente in lista_personale:
        if not dipendente.in_ferie and not dipendente.in_malattia:
            personale_disponibile.append(dipendente)
    return personale_disponibile


#Esecuzione del programma
print("--- INIZIO ELABORAZIONE TURNI ---")
if verifica_vincoli_ferie(personale):
    disponibili = genera_personale_disponibile(personale)
    print("Personale disponibile per la schedulazione di oggi:")
    for dipendente in disponibili:
        print(f" - {dipendente.nome} ({dipendente.ruolo})")
else: 
    print("\nRisolvere i conflitti di ferie")