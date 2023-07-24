#lista 1 segunda etapa
#nome: Jônatas Fernandes Silva; matrícula: 540089


#questão 01
'''
def soma(a,b,c):
 s=a+b+c
 return s
num1 = int(input('insira um valor: '))
num2 = int(input('insira um valor: '))
num3 = int(input('insira um valor: '))
soma(num1,num2,num3)
'''
#questão 02
'''
def leitura(a):
 print(len(str(a)))
num1 = int(input('insira um valor: '))
leitura(num1)
'''
#questão 03


#questão 04
'''
def recebe(a):
 reverse = a[::-1]
 return reverse
stringuer = str(input('insira a string: '))
recebe(stringuer)
'''
#questão 05
'''
def mista(a,b):
 if a in b:
   print('true')
 else:
   print('false')
stringuer = str(input('insira a string: '))
lista = []
continuar = 's'
while continuar == 's':
 item = str(input('insira algo: '))
 lista.append(item)
 continuar = str(input('deseja continuar? s:sim|n:não->>> '))
mista(stringuer,lista)
'''
#questão 06
'''
def recebe(a):
 reverse = str(a)[::-1]
 return reverse
num1 = int(input('insira um valor: '))
recebe(num1)
'''
#questão 07
'''
def recebe(dd,mm,aaaa):
 if mm == "01":
   mm = "janeiro"
 elif mm == "02":
   mm = "fevereiro"
 elif mm == "03":
   mm = "março"
 elif mm == "04":
   mm = "abril"
 elif mm == "05":
   mm = "maio"
 elif mm == "06":
   mm = "junho"
 elif mm == "07":
   mm = "julho"
 elif mm == "08":
   mm = "agosto"
 elif mm == "09":
   mm = "setembro"
 elif mm == "10":
   mm = "outubro"
 elif mm == "11":
   mm = "novembro"
 elif mm == "12":
   mm = "dezembro"
 print(f"{dd} de {mm} de {aaaa}")
dia = str(input('insira dia: '))
mes = str(input('insira mes: '))
ano = str(input('insira ano: '))
recebe(dia,mes,ano)
'''
#questão 08
'''
stringuer = str(input('insira string: '))
stringuer1 = str(input('insira string: '))
if stringuer1 in stringuer:
   print(stringuer.find(stringuer1))
'''
#questão 09
'''
stringuer = str(input('insira string: '))
for cont in stringuer:
 print(stringuer.count(cont))
'''
#questão 10
'''
for stringuer in input("digite o nome: "):
 print(stringuer)
'''

