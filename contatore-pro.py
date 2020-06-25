n = int(input('Fino a che numero vuoi contare? '))
s = int(input('Saltando quanti numeri alla volta? '))
for i in range(-1,n,s):
    print(i+1)

input("Premi Invio per uscire")