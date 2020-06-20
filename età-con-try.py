try:
    età = int(input('Età: '))
    if età >= 18:
        print('Sei maggiorenne')
    else:
        print('Sei minorenne')
except ValueError:
    print('Devi inserire un numero')