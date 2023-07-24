# lista 02
# nome: Jônatas Fernandes Silva ; matrícula: 540089


# questão 01
'''
lista_letras = []
cont = 0


while cont < 10:
  letras = str(input('digite uma letra: '))
  lista_letras.append(letras)
  cont += 1


for ind, itens in enumerate(lista_letras):
  print("\n{}-->{}".format(ind,itens))
'''

# questão 02
'''
lista_numeros = []
total_multiplos_de_seis = 0
cont = 0
cont_for = 5


while cont < 8:
  numero = int(input('digite um numero: '))
  lista_numeros.append(numero)
  if cont_for in range (cont_for,numero):
    total_multiplos_de_seis +=1
  cont += 1


print(lista_numeros)
print(total_multiplos_de_seis," essa é a quantidade de multiplos de seis")
'''

# questão 03
'''
aluno = []
notas_AV1 = []
notas_AV2 = []
media = []
aprovados = []
reprovados = []
cont = 0


while cont < 5:
  nome = str(input(f'insira o nome do aluno: '))
  aluno.append(nome)
  av1 = float(input('insira a nota 1 do aluno {}: '.format(aluno[cont])))
  notas_AV1.append(av1)
  av2 = float(input('insira a nota 1 do aluno {}: '.format(aluno[cont])))
  notas_AV2.append(av2)
  media_aritimetica = (notas_AV1[cont] + notas_AV2[cont])/2
  print(media_aritimetica)
  media.append(media_aritimetica)
  if media_aritimetica >= 6:
    print('APROVADO')
    aprovados.append(nome)
  else:
    print("REPROVADO")
    reprovados.append(nome)


  cont += 1


print("\n\nAV1\n",notas_AV1,"\n\nAV2\n",notas_AV2,"\n\nmedias\n",media,"\n\nalunos aprovados\n",aprovados,"\n\nreprovados\n",reprovados)
'''

# questão 04
'''
salario = []
novo_salario = []
reajuste = 0.8
cont = 0


while cont < 6:
  val = float(input('o valor do salario é de: '))
  salario.append(val)
  new_val = val + ( val * reajuste)
  novo_salario.append(new_val)
  cont += 1


for ind, salarios in enumerate(salario):
  print('\n\nSALÀRIO ANTIGO\n{}-->{:.2f}'.format(ind,salarios))


for ind, salarios_novos in enumerate(novo_salario):
  print('\nSALÀRIO NOVO\n{}-->{:.2f}'.format(ind,salarios_novos))
'''

# questão 05
'''
precoDeCompra = []
precoDeVenda = []
lucro_10Percent = 0
lucro_1020Percent = 0
lucro_20Percent = 0
cont = 0


for cont in range (5):
  mercadoria = str(input("digite o nome da mercadoria: "))
  compra = float (input("insira o preço de compra da mercadoria: "))
  precoDeCompra.append(compra)
  venda = float (input("insira o preço de venda da mercadoria: "))
  precoDeVenda.append(venda)
  lucro = venda - compra
  margemLucro = ((lucro/venda) * 100)
  if (margemLucro < 10):
    lucro_10Percent += 1
  elif (margemLucro >= 10 and margemLucro <= 20):
    lucro_1020Percent += 1
  else:
    lucro_20Percent += 1
  cont += 1


print("quantidade merdacorias com menos de 10% de lucro\n",lucro_10Percent)
print("quantidade merdacorias com mais de 10% e menos de 20% de lucro\n",lucro_1020Percent)
print("quantidade merdacorias com mais de 20% de lucro\n",lucro_20Percent)
'''
# questão 06-A CORRIGIR
'''
produto = []
código = []
quantidade = []
valorCompra = []
valorVenda = []
cont = 0


for cont in range(5):
  prod = str(input('insira o nome do produto: '))
  produto.append(prod)
  cod = str(input('insira o código do produto: '))
  código.append(cod)
  qtd = int(input('insira a quantidade de unidades do produto:' ))
  quantidade.append(qtd)
  compra = float (input('insira o valor de compra do do produto: '))
  valorCompra.append(compra)
  venda = float (input('insira o valor de venda do do produto: '))
  valorVenda.append(venda)
  cont += 1


while True:
  mostrar = int(input('se você quiser ver todos os produtos digite 1, se quiser ver um especifico digite 2: '))
  if mostrar == 1:
    print('----------------')
    for cont in range(5):
      print('\n')
      print('produtos\t\t{}\ncodigo\t\t{}\nquantidade\t\t{}\nvalor de compra\t\t{}\nvalor de venda\t\t{}'.format(produto,código,quantidade,valorCompra,valorVenda))
    print('----------------')
    break
  else:
    insertCod = int(input('insira o codigo do produto que deseja ver: '))
    if insertCod not in código:
      print('codigo não encontrado, tente novamente')
    else:
      print('produtos\t\t{}\ncodigo\t\t{}\nquantidade\t\t{}\nvalor de compra\t\t{}\nvalor de venda\t\t{}'.format(produto[insertCod],código[insertCod],quantidade[insertCod],valorCompra[insertCod],valorVenda[insertCod]))
      continue
'''

# questão 07
'''
conjunto_one = []
conjunto_two = []
conjunto_uniao = []
cont = 0


for cont in range(10):
  one = int(input('digite um valor para o conjunto one: '))
  conjunto_one.append(one)
  two = int(input('insira um valor para o conjunto two: '))
  conjunto_two.append(two)


  if (one == two):
    conjunto_uniao.append(one)
  else:
    continue

print('\n',conjunto_uniao,'esses são os numeros que se repetem nos dois conjuntos')
'''

# questão 08-no rumo, corrigir a logica
'''
lista_A = []
lista_w = []
cont = 0
resultado = 1
i = 1


for cont in range(10):
  a = int(input('insira o valor: '))
  lista_A.append(a)
  while i <= a:
    resultado *= i
    lista_w.append(resultado)
    i += 1
  cont += 1


print(lista_w)
'''

# questão 09
'''
lista = []
cont = 0
soma = 0


for cont in range(10):
  insert = int(input('insira um valor: '))
  lista.append(insert)
cont += 1


media = sum(lista)/10
print(min(lista),max(lista),media)
'''

# questão 10
'''
lista_x = []
lista_Y = []
cont = 0


while cont < 10:
  insert = int (input('insira um valor: '))
  if insert not in lista_x:
    lista_Y.append(insert)
  lista_x.append(insert)
  cont += 1

lista_Y.sort()
print(lista_Y)
print(lista_x)
'''