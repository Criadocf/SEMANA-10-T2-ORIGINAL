num_pessoas = 0
idade = 1
menor_idade = 999999
maior_idade = -9999
soma_idade = 0


while idade !=0:
    idade = int(input())
    if idade !=0:
      num_pessoas += 1
      soma_idade += idade
      if idade > maior_idade:
        maior_idade = idade
      if idade < menor_idade:
        menor_idade = idade

if num_pessoas !=0:
  print(f'{num_pessoas}\n{soma_idade/num_pessoas:.2f}\n{menor_idade}\n{maior_idade}')