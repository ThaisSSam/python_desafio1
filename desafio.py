menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[i] Imprimir Lista de Clientes
[n] Criar Conta Corrente
[m] Imprimir Lista de Contas
[q] Sair
=> """

def saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato): 
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# juntar o endereço em uma só variavel
def endereco_completo():
    print("Digite o endereço do cliente:")
    logradouro = str(input("Digite o logradouro do endereço do cliente: "))
    nro = int(input("Digite o número do endereço do cliente: "))
    bairro = str(input("Digite o bairro do endereço do cliente: "))
    cidade = str(input("Digite a cidade do endereço do cliente: "))
    estado = str(input("Digite o estado do endereço do cliente: "))
    return f"{logradouro}, {nro} - {bairro} - {cidade}/{estado}"

# retornando de forma que dá para usar kwargs
def solicitar_dados_cliente():
    print("Cadastro de Cliente \n")
    nome = str(input("Digite o nome do cliente: "))
    dtNasc = str(input("Digite a data de nascimento do cliente: "))
    endereco = endereco_completo()
    cpf = str(input("Digite o cpf do cliente: "))

    return {'nome': nome, 'dtNasc': dtNasc, 'endereco': endereco, 'cpf': cpf}


def cadastrar_cliente(lista, **kwargs):
    cpf = kwargs.get('cpf')
    
    # Verificar se o CPF já está na lista
    for cliente in lista:
        if cliente['cpf'] == cpf:
            print("\nCPF já utilizado")
            return
    
    # Adicionar os dados do cliente na lista
    cliente = {
        'nome': kwargs.get('nome'),
        'dtNasc': kwargs.get('dtNasc'),
        'endereco': kwargs.get('endereco'),
        'cpf': cpf
    }
    
    lista.append(cliente)
    print("Cliente cadastrado com sucesso!")


def imprimir_lista(lista):
    if not lista:
        print("Nenhum cliente cadastrado.")
        return

    print("\nLista de Clientes:")
    for i, cliente in enumerate(lista, start=1):
        print(f"\nCliente {i}:")
        print(f"Nome: {cliente['nome']}")
        print(f"Data de Nascimento: {cliente['dtNasc']}")
        print(f"Endereço: {cliente['endereco']}")
        print(f"CPF: {cliente['cpf']}")


# Variável global para rastrear o número da conta
numero_conta_sequencial = 1

def criar_conta_corrente(clientes, contas):
    global numero_conta_sequencial
    
    cpf = str(input("Informe o CPF do cliente: "))
    
    # Verificar se o cliente está cadastrado
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return
    
    agencia = "0001"
    numero_conta = numero_conta_sequencial
    numero_conta_sequencial += 1
    
    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': cliente_encontrado
    }
    
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")


def imprimir_contas(**kwargs):
    contas = kwargs.get('contas', [])
    
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\nLista de Contas:")
    for i, conta in enumerate(contas, start=1):
        usuario = conta['usuario']
        print(f"\nConta {i}:")
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Nome do Cliente: {usuario['nome']}")
        print(f"CPF do Cliente: {usuario['cpf']}")


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = ""
nome = ""
dtNasc = ""
cpf = ""
endereco = ""
lista_clientes = []
lista_contas = []

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "c":
        dados_cliente = solicitar_dados_cliente()
        cadastrar_cliente(lista_clientes, **dados_cliente)

    elif opcao == "i":
        imprimir_lista(lista_clientes)

    elif opcao == "n":
        criar_conta_corrente(lista_clientes, lista_contas)

    elif opcao == "m":
        imprimir_contas(contas=lista_contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
