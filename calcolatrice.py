print ("""-------------------
1. Addizione
2. Sottrazione
3. Moltiplicazione
4. Divisione
5. Calcolo percentuale
-------------------""")

# La scelta dell'utente
print("Cosa vuoi fare?")
scelta = input("Scrivi un numero: ")

# Addizione | x+y
if scelta == "1":
    print("Stai per fare una Addizione")
    x = float(input('inserisci il primo numero: '))
    y = float(input('inserisci il secondo numero: '))
    print("Risultato:",float(x+y))

# Sottrazione | x-y
elif scelta == "2":
    print("Stai per fare una Sottrazione")
    x = float(input('inserisci il primo numero: '))
    y = float(input('inserisci il secondo numero: '))
    print("Risultato:",float(x-y))

# Moltiplicazione | x*y
elif scelta == "3":
    print("Stai per fare una Moltiplicazione")
    x = float(input('inserisci il primo numero: '))
    y = float(input('inserisci il secondo numero: '))
    print("Risultato:",float(x*y))

# Divisione | x*y
elif scelta == "4":
    print("Stai per fare una Divisione")
    x = float(input('inserisci il primo numero: '))
    y = float(input('inserisci il secondo numero: '))
    print("Risultato:",float(x/y))

# Calcolo percentuale | x*y/100 | il 22% (Y) di 100 (X) =
elif scelta == "5":
    print("Stai per calcolare la percentuale Es. il 22% di 100 \nNota: Non usare il simbolo %")
    y = float(input('il: '))
    x = float(input('di: '))
    print("Risultato:",float(x*y/100))

# Se sbaglia qualcosa
else:
    print('Devi scrivere un numero, stupidino')

# E' utile su windows se si apre la calcolatrice con il doppio click a posto che da terminale
# (perchè in caso contrario appena esce il risultato si chiude immediatamente)
input("Premi Invio per uscire")

