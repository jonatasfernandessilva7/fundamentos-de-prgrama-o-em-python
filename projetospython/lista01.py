#nome: Jônatas Fernandes Silva, matrícula: 540089

#questão 01->imprimir nome
'''
nome = str(input('digite seu nome: '))
print ('seu nome é: {}'.format(nome))
'''

#questão 02->imprimir o produto de 30 e 27
'''
print ('o resultado do produto de 30 e 27 é: {}'.format(30*27))
'''

#questão 03->média aritimética entre 5,8,12
'''
media_aritmetica = (5+8+12)/3
print('a media entre: 5,8 e 12 é de: {}'.format(media_aritmetica))
'''

#questão 04->imprimir um número do tipo int
'''
numero = int(input('digite um némuro: ')) 
print('o número digitado foi: ',numero)
'''

#questão 05->ler e imprimir dois números flutuantes
'''
num_1 = float(input('digite um valor: '))
num_2 = float(input('digite outro valor: '))
print (num_1, 'e', num_2 )
'''

#questão 06->ler um número int e imprimir o sucessor e o antecesor
'''
num = int(input('insira um numero inteiro: '))
print('antecesor = {} \nsucessor = {}'.format(num-1 , num+1))
'''

#questão 07->ler nome,endereço,telefone e imprimir os dados
'''
nome = str(input('insira seu nome: '))
endereco = str(input('insira seu endereço: '))
telefone = int(input('insira seu nome: '))
print('nome: {}\nenderecço: {}\ntelefone:{}'.format(nome,endereco,telefone))
'''

#questão 08->ler dois números int e imprimir subtração
'''
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
print('a subtração entre os numeros {} e {} tem como resultado {}'.format(n1,n2,n1-n2))
'''

#questão 09->ler um numero float e imprimir 1/4 dese numero
'''
numero = float(input('insira o valor: '))
print(numero * 0.25)
'''

#questão 10->ler 3 numeros float e calcular a media aritimetica (imprimir resultado)
'''
n1 = float(input('insira um valor: '))
n2 = float(input('insira outro valor: '))
n3 = float(input('insira o ultimo valor: '))
media = (n1+n2+n3)/3
print(media)
'''

#questão 11->ler dois float,calcular as quatro operações,imprimir os resultados
'''
n1 = float(input('insira o valor: '))
n2 = float(input('insira o valor: '))
while (1):
        operações = int(input('escolha a operação que deseja realizar: 1->soma, 2->subtração, 3->divisão ou 4->multiplicação: '))
        if (operações == 1):
            resultado = n1 + n2
            print (resultado)
        elif (operações == 2):
            resultado = n1 - n2
            print (resultado)
        elif (operações == 3):
            resultado = n1 * n2
            print (resultado)
        elif (operações == 4):
            resultado = n1 / n2
            print (resultado)
        else:
            print('erro, escolha novamente')
'''

#questão 12->ler num float e imprimir seu quadrado
'''
n1 = float(input('insira o valor: '))
print (n1 ** 2)
'''

#questão 13->ler saldo de conta poupança e imprimir saldo novo, reajuste de 2%
'''
saldo_poupança = float (input('digite seu saldo: '))
reajuste = int(input('se o reajuste for para mais digite 1, se for para menos digite 2: '))
if (reajuste == 1):
    saldo_novo = saldo_poupança + (saldo_poupança * 0.2)
    print('sua poupança agora é de: ',saldo_novo)
else:
    saldo_novo = saldo_poupança - (saldo_poupança * 0.2)
    print('sua poupança agora é de: ',saldo_novo)
'''

#questão 14->ler base,altura, imprimir perimetro e area
'''
base = float (input('digite o tamanho da base: '))
altura = float (input('digite o tamanho da altura: '))
perimetro = ((base*2)+(altura*2))
area = base * altura
print('o perimetro desse retangulo é de: {}\na area do retangulo é de: {}'.format(perimetro,area))
'''

#questão 15->ler valor do produto,percentual do desconto e imprime o valor após o desconto
'''
valor_produto = float (input('digiteo valor do produto: '))
desconto = float (input('digite o percentual de desconto: '))
valor_novo = valor_produto - (valor_produto * desconto)
print ('o valor apos o desconto é de: ',valor_novo)
'''

#questão 16->ler salario, ler percentual e calcular o novo valor apos o reajuste salarial
'''
salario = float (input('digite seu salario: '))
valor_reajuste = float(input('digite o valor percentual de reajuste: '))
reajuste = int(input('se o reajuste for para mais digite 1, se for para menos digite 2: '))
if (reajuste == 1 ):
    valor_novo_salario = salario + (salario*valor_reajuste)
    print (valor_novo_salario)
else:
    valor_novo_salario = salario - (salario*valor_reajuste)
    print (valor_novo_salario)
'''