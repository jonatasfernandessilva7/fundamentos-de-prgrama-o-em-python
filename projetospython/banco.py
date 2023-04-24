listadeUsuarios = {}
infosDosUsuarios = []

def criarConta():
    continuarAdicionandoConta = "s"
    codigoDoUsuario = 1001
    saldo = 100
    while continuarAdicionandoConta == "s":
        nomeDoUsuario = str(input("insia seu nome completo aqui: "))
        continuarAdicionandoConta = str(input("para adicionar outra conta digite»»s\ncaso não queira mais adcionar digite»»n\n"))
        infosDosUsuarios = []
        infosDosUsuarios.append(nomeDoUsuario)
        infosDosUsuarios.append(saldo)
        listadeUsuarios.update({codigoDoUsuario : infosDosUsuarios})
        codigoDoUsuario += 1
    return listadeUsuarios

def saque(users):
    while True:
        numDaConta = int(input("insira o numero da conta que deseja fazer o saque: "))
        if numDaConta in users: 
            valorASacar = float(input("insira o valor de saque: "))
            if valorASacar > users[numDaConta][1]:
                print("valor maior que seu saldo, seu saldo é de {}".format(users[numDaConta][1]))
                continue
            users[numDaConta][1] -= valorASacar
            break
        else:
            print("usuario nao existe")

def deposito(usuarios):
    while True:
        numDaContaDoUsuario = int(input("insira o numero da conta que deseja fazer o deposito: "))
        if numDaContaDoUsuario in usuarios: 
            valorADepositar = float(input("insira o valor de saque: "))
            usuarios[numDaContaDoUsuario][1] += valorADepositar
            break
        else:
            print("usuario nao existe")

def transferencia(listinhaDePessoas):
    while True:
        numDaContaDoTransferidor = int(input("insira o numero da conta que deseja fazer o envio: "))
        if numDaContaDoTransferidor in listinhaDePessoas: 
            numDaContaASerReceber = int(input("insira o numero da conta que ira receber a grana: "))
            if numDaContaASerReceber in listinhaDePessoas:
                valorDeTrasferencia = float(input("insira o valor a ser transferido: "))
                if valorDeTrasferencia > listinhaDePessoas[numDaContaDoTransferidor][1]:
                    print("valor acima do saldo, seu saldo eh de {}".format(listinhaDePessoas[numDaContaDoTransferidor][1]))
                    continue
                listinhaDePessoas[numDaContaDoTransferidor][1] -= valorDeTrasferencia
                listinhaDePessoas[numDaContaASerReceber][1] += valorDeTrasferencia
                break
            else:
                print("usuario nao existe")
        else:
            print("usuario nao existe")

def listarContas(agendaDeUsuarios):
    print(agendaDeUsuarios)

def sairDoSistema(informacoes):
    print(informacoes)
    print("volte sempre")

def escolha(escolha):
    if escolha == 1:
        criarConta()
    elif escolha == 2:
        saque(listadeUsuarios)
    elif escolha == 3:
        deposito(listadeUsuarios)
    elif escolha == 4:
        transferencia(listadeUsuarios)
    elif escolha == 5:
        listarContas(listadeUsuarios)
    elif escolha == 6:
        sairDoSistema(listadeUsuarios)

def main():
    while True:
        print("="*33)
        print("="*14,"ATM","="*14)
        print("="*10,"Itapajé Bank","="*10)
        print("selecione uma opção menu:\n")
        print("1-criar conta\n2-efetuar saque\n3-efetuar depósito\n4-efetuar transferência\n5-listar contas\n6-sair do sistema")
        opcao = int(input(""))
        if opcao == 6:
            escolha(opcao)
            break
        if opcao >= 7:
            print("opcao invalida, escolha novamente")
        escolha(opcao)

main()