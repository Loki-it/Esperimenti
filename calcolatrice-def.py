# Definizione delle funzioni

# Addizione | x+y
def addizione(x,y):
    return x + y

# Sottrazione | x-y
def sottrazione(x,y):
    return x - y

# Moltiplicazione | x*y
def moltiplicazione(x,y):
    return x * y

# Divisione | x÷y
def divisione(x,y):
    return x / y

# Calcolo Percentuale | x%y
def percentuale(x,y):
    return x + y

# Menù
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

# Definire X e Y che sono i 2 numeri per ogni cosa
x = float(input('inserisci il primo numero: '))
y = float(input('inserisci il secondo numero: '))

# Menù Addizione | x+y
if scelta == '1':
    print(x, "+", y, "=", addizione(x, y))

# Menù Sottrazione | x-y
if scelta == "2":
    print(x, "-", y, "=", sottrazione(x, y))

# Menù Moltiplicazione | x*y
if scelta == "3":
    print(x, "x", y, "=", moltiplicazione(x, y))

# Menù Divisione | x÷y
if scelta == "4":
    print(x, "÷", y, "=", divisione(x, y))

# E' utile su windows se si apre la calcolatrice con il doppio click a posto che da terminale
# (perchè in caso contrario appena esce il risultato si chiude immediatamente)
input("Premi Invio per uscire")

