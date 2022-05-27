nota = -100

while not (0 <= nota <= 10):
    nota = float(input())
    if 0 <= nota < 4:
        print('E')

    elif 4 <= nota < 5:
        print('D')

    elif 5 <= nota < 7:
        print('C')

    elif 7 <= nota < 8.5:
        print('B')

    elif 8.5 <= nota <= 10:
        print('A')

    else:
        print('Nota inválida.')  #NOTA INVÁLIDA É A REPETIÇÃO.