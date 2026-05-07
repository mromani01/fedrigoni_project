# Piano d'Azione: Schedulatore Turni Fedrigoni

[cite_start]Questo documento delinea i passaggi operativi per programmare lo strumento di creazione automatica dei turni [cite: 14][cite_start], rispettando le direttive della "Fedrigoni Challenge"[cite: 2].

## Fase 1: Creazione dei Dati di Test (Input)
[cite_start]Poiché non disponi dei dati reali completi, devi creare un set di dati ridotto utilizzando nomi fittizi[cite: 12]. [cite_start]Prepara file o strutture dati per i seguenti elementi[cite: 6]:
* [cite_start]**Anagrafica Personale:** Elenco dei dipendenti[cite: 7].
* [cite_start]**Specializzazioni:** Ruoli assegnati, tra cui necessariamente "bobinatori" e "conduttori di macchina"[cite: 11, 33, 34].
* [cite_start]**Limitazioni:** Eventuali problemi di salute o restrizioni del personale[cite: 10].
* [cite_start]**Macchinari:** Elenco delle macchine e relativa necessità di copertura[cite: 8, 9].
* [cite_start]**Registro Assenze:** Un file (es. simulazione Excel) per registrare malattie improvvise e ferie[cite: 11, 41].

## Fase 2: Implementazione dei Vincoli Algoritmici
L'algoritmo deve applicare rigidamente le regole aziendali. Scrivi le funzioni di controllo per:
* [cite_start]**Filtro Malattia:** Se un dipendente comunica la malattia (dati registrati su file Excel), non può essere inserito nel turno[cite: 41, 44].
* [cite_start]**Filtro Ferie (Priorità Massima)[cite: 37]:**
    * [cite_start]Blocco superamento limite: Massimo 4 persone possono prendere ferie al giorno[cite: 29].
    * [cite_start]Vincolo Bobinatori: Non possono esserci più di 4 o 5 bobinatori in ferie nello stesso reparto/turno (per evitare il blocco macchine)[cite: 33].
    * [cite_start]Vincolo Conduttori: Non più di 3 conduttori di macchina in ferie[cite: 34].
    * [cite_start]Blocco Revoca: L'algoritmo non può revocare le ferie se il dipendente è già in ferie[cite: 38].

## Fase 3: Sviluppo del Motore di Schedulazione
Sviluppa il cuore logico del programma:
* **Assegnazione:** Il sistema deve incrociare il personale disponibile con i macchinari.
* [cite_start]**Ricalcolo Dinamico:** Il turno deve essere ricalcolato automaticamente ad ogni singola variazione di informazione (per gestire la continua mutevolezza degli schemi)[cite: 3, 4].

## Fase 4: Output e Interfaccia
[cite_start]Il prodotto finale deve produrre un output chiaro e utilizzabile[cite: 14]:
* [cite_start]**Schermata Assenze:** Il sistema deve informare in modo trasparente su chi è attualmente in ferie[cite: 36].
* [cite_start]**Generazione Turno:** Creazione del turno effettivo, popolato esclusivamente con il personale risultato disponibile[cite: 36].

## Fase 5: Documentazione e Consegna
Prepara il materiale richiesto per le due figure di riferimento:
* [cite_start]**Per l'Azienda:** Redigi una documentazione dettagliata in modo che l'azienda possa proseguire autonomamente con il progetto[cite: 21].
* [cite_start]**Per il Professore:** Assicurati di avere un prodotto applicativo funzionante, fondamentale per dimostrare l'applicazione pratica dei concetti d'esame[cite: 22].
