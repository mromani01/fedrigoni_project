#DATA PARSING FROM CSV FILES
import csv
from models import Dipendente, Macchinario

def carica_dipendenti_da_csv(file_path):
    """
    Legge la Qualification Matrix e restituisce una lista di oggetti Dipendete.
    """
    dipendenti = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
       
        reader = csv.DictReader(csvfile)
       
        for row in reader:
            matricola = row.get("Matricola", "N/D")
            nome = row.get("Nome", "Sconosciuto")
            ruolo = row.get("Ruolo", "Generico")

            nuovo_dipendente = Dipendente(matricola, nome, ruolo)
            dipendenti.append(nuovo_dipendente)
    return dipendenti


def carica_macchinari_da_csv(file_path):
    """
    Legge la Macchinari Matrix e restituisce una lista di oggetti Macchinario.
    """
    macchinari = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nome = row.get("Nome", "Sconosciuto")
            reparto = row.get("Reparto", "Generico")
            personale_richiesto = int(row.get("Personale Richiesto", 1))

            nuovo_macchinario = Macchinario(nome, reparto, personale_richiesto)
            macchinari.append(nuovo_macchinario)
    return macchinari


# --- PICCOLO TEST ---
if __name__ == "__main__":
    print("Test caricamento dati...")
    # Puoi testarlo inserendo il percorso reale del tuo file
    dipendenti = carica_dipendenti_da_csv("/home/matteo/Scrivania/fedrigoni_projectdata/QUALIFICATION_MATRIX_UNITN.xlsx - QUALIFICATION MATRIX.csv")
    macchinari = carica_macchinari_da_csv("/home/matteo/Scrivania/fedrigoni_project/data/MACCHINARI_MATRIX_UNITN.xlsx - MACCHINARI MATRIX.csv")
    print(dipendenti)
    print(macchinari)