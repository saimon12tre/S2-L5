import datetime

print("BENVENUTO NELL'ASSISTENTE VIRTUALE\n")
print("***  Digita help oppure menu per vedere cosa posso fare per te  *** \n\n ")

def assistente_virtuale(comando):
    if comando.lower()== "qual è la data di oggi?":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando.lower() == "che ore sono?":
        ora_attuale = datetime.datetime.now()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando.lower() == "come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    return risposta
    
while True:
    comando_utente = input("Cosa vuoi sapere? ")
  
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    elif comando_utente.lower() == "menu" or comando_utente.lower() == "help":
        print("\n\n** MENU COMANDI **\n1 - qual è la data di oggi?\n2 - che ore sono?\n3 - come ti chiami?\n")
    else:
        print(assistente_virtuale(comando_utente))
