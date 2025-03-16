# título sistema
titulo = " Internet Banking 1.0 ".center(70, "=")

# nome usuário
login = input(f"{titulo}\n\n#LOGIN\nInforme seu Nome: ").strip()

# padrão mensagem erro
def mensagem_erro(msg):
    print(f" {msg} ".center(10,"!"))

# padrão mensagem sucesso
def mensagem_sucesso(msg):
    print(f" {msg} ".center(10,"$"))

# menu principal
def menu(login, titulo, mostrar_saudacao=True):
    # saudação somente na primeira vez
    saudacao = f"\nOlá {login}, sejam bem-vindo à sua conta" if mostrar_saudacao else ""

    # opções menu
    opcoes_menu = [
        ("d", "Depositar"),
        ("s", "Sacar"),
        ("e", "Extrato"),
        ("q", "Sair")
    ]

    # Formata opcoes
    opcoes_formatadas = "\t".join([f"[{opcao[0]}] {opcao[1]}" for opcao in opcoes_menu])
    
    # Menu formatado
    return input(f"""
    \n{titulo}
    {saudacao}
    \n{opcoes_formatadas}
    \n=> """)

# Função depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0: 
        saldo += valor  
        extrato += f"Depósito:\t+ R$ {valor:.2f}\n"
        mensagem_sucesso("Depósito realizado com sucesso")
    else:
        mensagem_erro("Valor inválido") 
    return saldo, extrato

# Função saques
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # condicoes
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        mensagem_erro("Saldo suficiente")
    elif excedeu_limite:
        mensagem_erro("Valor por saque excedido")
    elif excedeu_saques:  
        mensagem_erro("Limite de saques excedido")

    elif valor > 0:  
        saldo -= valor  
        extrato += f"Saque:\t\t- R$ {valor:.2f}\n"  
        numero_saques += 1
        mensagem_sucesso("Saque realizado com sucesso")
    else:
        mensagem_erro("Valor inválido")  
    return saldo, extrato

# Função extrato
def exibir_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(40, "-")) 
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("".center(40, "-"))  

# Função parametros
def main():
    LIMITE_SAQUES = 3  
    saldo = 0  
    limite = 500  
    extrato = ""  
    numero_saques = 0  
    inicio = True  

    # Loop principal do sistema
    while True:  
        
        opcao = menu(login, titulo, mostrar_saudacao=inicio)
        inicio = False  # Após a primeira exibição, desativa a saudação

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s": 
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q": 
            mensagem_sucesso("Obrigado por usar o Internet Banking. Até logo!")
            break 

        else:  # Caso o usuário insira uma opção inválida
            mensagem_erro("Operação inválida, por favor tente novamente")

# Executa o programa principal
main()

