menu = """
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair
=>"""

saldo = 0
limite = 500.00
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while(True):
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Ddigite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:0.2f}\n"
        else:
            print("Opçao falhou! valor informado é invalido.")
        print(f"Saldo atual: {saldo}")
    elif opcao == "s":
        valor = float(input("Ddigite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE
        if excedeu_saldo:
            print("Operacao falhou! saldo insulficiente.")
        elif excedeu_limite:
            print("Operacao falhou: Limite para saque exedido.")
        elif excedeu_saques:
            print("Operacao falhou: Número máximo de saque exedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:0.2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou valor informado é inválido.")
        print(f"Saldo atual: {saldo}")
    elif opcao == "e":
        print("\n############### EXTRATO ################")
        print("Não foram realizadas movimentação." if not extrato else extrato)
        print(f"\nSando: {saldo:0.2f}")
        print("###########################################")

    elif opcao == "q":
        break
    else:
        print("Operacao invalida, por favor selecione uma opçao")

    



    

