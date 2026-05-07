class Dipendente:
    #costruttore
    def __init__(self, matricola, nome, ruolo):
        self.matricola = matricola
        self.nome = nome
        self.ruolo = ruolo
        self.in_ferie = in_ferie
        self.in_malattia = in_malattia

        self.qualifiche = []  # Lista delle qualifiche del dipendente
        
        self.in_ferie = False
        self.in_malattia = False  # Stato iniziale: non in ferie e non in malattia
        self.limitazioni = []  # Problemi di salute/limitazioni fisiche

        def __repr__(self):
            return f"Dipendente({self.matricola}, {self.nome}, {self.ruolo})"
        

class Macchinario:
    def __init__(self, nome, reparto, personale_richiesto):
        self.nome = nome
        self.reparto = reparto
        self.personale_richiesto = personale_richiesto  # Numero di dipendenti richiesti per operare il macchinario

    def __repr__(self):
        return f"Macchinario({self.nome}, {self.reparto}, {self.personale_richiesto})"
    

class Turno:
    def __init__(self, data, tipo_turno):
        self.data = data
        self.tipo_turno = tipo_turno  # Es. "mattina", "pomeriggio", "notte"
        self.dipendenti_assegnati = {}  #Dizionario per i macchinari --> {Macchina: [Lista dipendenti]}