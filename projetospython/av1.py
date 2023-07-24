'''
nome: Jônatas Fernandes Silva
matrícula: 540089
fundamentos de programação-prova 01
'''


#questão 01
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


#questão 02
'''
lista_A = [] 
lista_B = []


for cont in range (10):
  num = int(input('insira um valor: '))
  if num not in lista_A:
    lista_B.append(num)
  lista_A.append(num)


print(lista_A,'\n',lista_B)
'''


#questão 03
'''
continuar = 1
cont_py =0
cont_java = 0
cont_cpp = 0
cont_js = 0
cont_otrs = 0
cont_tot = 0


while continuar != 0:
  print('---------------------------')
  print('ESCOLHA A MELHOR LINGUAGEM')
  print('---------------------------')
  opção= int(input('OPÇÕES\n1->python\n2->java\n3->c++\n4->javascript\n5->outra\n'))
  if opção == 1:
    cont_py += 1
  elif opção == 2:
    cont_java += 1
  elif opção == 3:
    cont_cpp += 1
  elif opção == 4:
    cont_js += 1
  elif opção == 5:
    cont_otrs += 1
  else:
    print('numero invalido, insira novamente')
  cont_tot += 1
  continuar = int(input('deseja continuar? 1=sim|0=não: '))
percentpy = (cont_py/cont_tot)*100 
percentjava = (cont_java/cont_tot)*100 
percentcpp = (cont_cpp/cont_tot)*100 
percentjs = (cont_js/cont_tot)*100 
percentotrs = (cont_otrs/cont_tot)*100 
total = cont_py+cont_java+cont_js+cont_otrs+cont_cpp
print('LINGUAGEM DE PROGRAMAÇÃO\tvotos\t\t\t\t%')
print('-----------------------\t\t-------\t\t\t\t----')
print('python\t\t\t\t',cont_py,'\t\t\t\t',percentpy,'\njava\t\t\t\t',cont_java,'\t\t\t\t',percentjava,'\nc++\t\t\t\t',cont_cpp,'\t\t\t\t',percentcpp,'\njavascript\t\t\t',cont_js,'\t\t\t\t',percentjs,'\noutra\t\t\t\t',cont_otrs,'\t\t\t\t',percentotrs)
print('----------------\t-------\t------')
print('TOTAL\t\t\t\t',total)
'''


#questão 04
'''
lista = []
cont_par = 0


for cont in range(10):
  num = int(input('insira um valor: '))
  lista.append(num)
  if num % 2 == 0:
    cont_par += 1


percent_par = (cont_par/10)*100
media=sum(lista)/10
print(min(lista),'\n',max(lista),'\n',percent_par,'%','\n',media)
'''