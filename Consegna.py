import random
Città = input ('Inserisci il nome della tua città: ')
Nome = input ('Inserisci il nome del tuo animale: ')
Lista= ['Gli Indomabili', 'Il Labirinto', 'Il Canto', 'I Cinghiali', 'I Piccioni']
Lista_aggettivi= random.choice(Lista)
print (f"Il nome della tua band è: {Nome} 'e' {Lista_aggettivi} 'di' {Città}")