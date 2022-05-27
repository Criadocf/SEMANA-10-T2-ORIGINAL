opc = 10


while opc !=0:
    opc = int(input(
'''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM\n'''))

    if opc ==1:
        print('''1 - Olá. Como vai?''')
    elif opc ==2:
        print('''2 - Vamos estudar mais.''')
    elif opc ==3:
        print('''3 - Meus Parabéns!''')
    elif opc ==0:
        print('''0 - Fim de serviço.''')
    else:
        print('''Opção inválida.''')
  


