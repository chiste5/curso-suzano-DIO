import datetime

saldo = 2000
extrato_saque = []
extrato_deposito = []
data_hora_saque = []
data_hora_deposito = []
saque_do_dia = 1500
limite_saque_dia = 10


def saque_dia(saque_atual, valor):
    return saque_atual - valor

def sacar(saldo, saque_do_dia,limite_saque_dia):  # 👈 agora recebe dois argumentos!
    valor = float(input("Digite o valor que deseja sacar: "))
    saque_restante = saque_dia(saque_do_dia, valor)

    if saldo > 0 and saque_restante >= 0:
        if valor > 500:
            print("Você não pode sacar um valor acima de R$500,00")
        else:
            print("Você sacou R$", valor)
            saldo -= valor
            saque_do_dia = saque_restante  # 👈 atualiza o limite restante
            limite_saque_dia -= 1
            extrato_saque.append(-valor)
            data_atual = datetime.datetime.today()
            data_formatada = data_atual.strftime("%d-%m-%Y %H:%M")
            data_hora_saque.append(data_formatada)
    else:
        print("Você está sem saldo ou excedeu o limite diário de saque.")

    return saldo, saque_do_dia, limite_saque_dia  # 👈 retorna os dois valores atualizados

def depositar(saldo):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito > 0:
        print("Você depositou o valor de", valor_deposito)
        extrato_deposito.append(valor_deposito)
        saldo += valor_deposito
        data_atual = datetime.datetime.today()
        data_formatada = data_atual.strftime("%d-%m-%Y %H:%M")
        data_hora_deposito.append(data_formatada)
    else:
        print("Não é possível depositar valores negativos")
    return saldo

def extrato():
    print("Esse é o extrato")


menu = """========== MENU ==========

1. Sacar
2. Depositar
3. Extrato
4. Sair

==========================\n"""

opcao = 0

while opcao != 4:
    opcao = int(input(menu))

    if opcao == 1:
        saldo, saque_do_dia, limite_saque_dia = sacar(saldo, saque_do_dia,limite_saque_dia)
        print("Extrato de saques:", extrato_saque)
        print("Saldo atual:", saldo)
        print("Limite restante de saque diário:", saque_do_dia)
        print("Limite de saques diário:",limite_saque_dia)
        print(data_hora_saque)
    elif opcao == 2:
        saldo = depositar(saldo)
        print("Saldo atual:", saldo)
    elif opcao == 3:
        extrato_final = extrato_saque + extrato_deposito
        print("========== EXTRATO BANCÁRIO ==========")
        for item in extrato_final:
            print(f"{data_hora_saque}R$ {item:.2f}")
        print("Saldo Final:",saldo)
        print("======================================")
    elif opcao == 4:
        print("Saindo... Volte sempre!")
        break
    else:
        print("Digite uma opção válida!")