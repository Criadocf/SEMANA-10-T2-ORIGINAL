H = float(5.50)
C = float(6.80)
M = float(4.50)
A = float(7.00)
Q = float(4.00)
soma_itens = 0
codigo = 'SDS'

while codigo != 'X':
    codigo = str(input('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA \n''')).upper()[0]
    if codigo not in ['H','C','A','Q','M','X']:
      print('opcao invalida')
    if codigo == 'H':
      soma_itens += H
    if codigo == 'C':
      soma_itens += C
    if codigo == 'M':
      soma_itens += M
    if codigo == 'A':
      soma_itens += A
    if codigo == 'Q':
      soma_itens += Q
    if codigo == 'X':
      print(f'{soma_itens:.2f}')
    