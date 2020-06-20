try:
    n = int(input('Fino a che numero vuoi contare? '))
    for i in range(0,n):
        print(i+1)
except ValueError:
    print("Devi inserire un numero")