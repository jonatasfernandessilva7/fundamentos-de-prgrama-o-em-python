#AULA 05-trabalho
#questão 01
'''
cont = 0
total_astrogildo = 0
total_bode = 0
total_branco_nulo = 0
total_eleitores = int(input("quantos eleitores tem na cidade? "))


while cont < total_eleitores:
  opcao_voto = int(input("em qual candidato deseja votar?\n1-Astrogildo\n2-Bode\n3-Branco/nulo\nvoto: "))
  if (opcao_voto == 1):
    print("\n\nvocê votou no astrogildo!")
    print("\n\nvotação concluída")
    total_astrogildo+= 1
  elif (opcao_voto == 2):
    print("você votou no bode!")
    print("\n\nvotação concluída")
    total_bode += 1
  elif (opcao_voto == 3):
    print("você votou em braco ou nulo!")
    print("\n\nvotação concluída")
    total_branco_nulo += 1
  else:
    print("\n\nerro, opção inválida, vote novamente!")
  cont += 1


print("\n\nquantidade de votos de astrogildo:\t\t{}".format(total_astrogildo))
print("\n\nquantidade de votos de bode:\t\t\t{}".format(total_bode))
print("\n\nquantidade de votos brancos e nulos:\t\t{}".format(total_branco_nulo))


if (total_astrogildo > total_bode):
  print("\n\no novo prefeito é o astrogildo!!!!")
else:
  print("\n\no novo prefeito é o bode!!!!!")
'''


#questão 02
'''
deposito_i = float(input('digite o deposito inicial: '))
taxa_juro = float(input('insira a taxa de juros a ser cobrada: '))
saldo = deposito_i
cont = 1


for cont in range (36):
  saldo += (saldo * (taxa_juro/100))
  print('o saldo do mês {} foi de: {}'.format(cont,saldo))
  cont += 1
'''


#questão 03
'''
valor_inicial = float(input('insira o valor inicial da sua divida: '))
juros = float(input('insira o valor de juros a ser cobrado: '))
juros_porcent = juros/100
valor_mensal = float(input('insira o valor a ser pago mensalmente: '))
num_meses_pg = valor_inicial/valor_mensal
cont = 0


while (valor_inicial != 0):
  valor_inicial -= (valor_mensal * juros_porcent)
  print('\n\no saldo da divida no mes {} é de {}'.format(cont,valor_inicial))
  cont+=1
  if (valor_inicial == 0):
    print('divida paga')


print("a divida deverá ser paga em ate {} meses".format(num_meses_pg))
'''


#questão 04
'''
num_pessoas = int(input('qual a quantidade de pessoas: '))
tot_menor21 = 0
tot_maior21 = 0
cont = 0


while cont < num_pessoas:
  idade = int(input('insira sua idade: '))
  if (idade > 21):
    tot_maior21 += 1
  else:
    tot_menor21 += 1


  cont += 1


print('pessoas com menos de 21: {}'.format(tot_menor21))
print('pessoas com mais de 21: {}'.format(tot_maior21))
print('total de pessoas: {}'.format(num_pessoas))
'''