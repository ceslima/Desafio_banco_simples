# Sistema Bancário v2.1 - Com Limpeza de Tela

# Módulos nativos do Python para interagir com o sistema operacional
import os
import platform
import time

# --- Constantes do Sistema ---
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_POR_SAQUE = 500.00

def limpar_tela():
    """Limpa o terminal, funcionando em Windows, Linux e macOS."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def pausar_e_limpar():
    """Pausa a execução até o usuário pressionar Enter e depois limpa a tela."""
    input("\nPressione Enter para continuar...")
    limpar_tela()

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> """
    return input(menu).lower()

def depositar(saldo, extrato):
    """Realiza a operação de depósito."""
    print("\n--- Operação de Depósito ---")
    try:
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f"Depósito: + R$ {valor_deposito:.2f}")
            print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("\nERRO: O valor do depósito deve ser positivo.")

    except ValueError:
        print("\nERRO: Valor inválido. Por favor, digite um número.")
    
    pausar_e_limpar() # Nova chamada aqui!
    return saldo, extrato

def sacar(*, saldo, extrato, numero_saques):
    """Realiza a operação de saque."""
    print("\n--- Operação de Saque ---")
    try:
        valor_saque = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite_diario = numero_saques >= LIMITE_SAQUES_DIARIOS
        excedeu_limite_por_saque = valor_saque > LIMITE_VALOR_POR_SAQUE

        if excedeu_saldo:
            print(f"\nERRO: Saldo insuficiente. Seu saldo atual é R$ {saldo:.2f}.")
        elif excedeu_limite_diario:
            print(f"\nERRO: Limite de {LIMITE_SAQUES_DIARIOS} saques diários atingido.")
        elif excedeu_limite_por_saque:
            print(f"\nERRO: O valor máximo por saque é de R$ {LIMITE_VALOR_POR_SAQUE:.2f}.")
        elif valor_saque <= 0:
            print("\nERRO: O valor do saque deve ser positivo.")
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato.append(f"Saque:    - R$ {valor_saque:.2f}")
            print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")

    except ValueError:
        print("\nERRO: Valor inválido. Por favor, digite um número.")
    
    pausar_e_limpar() # Nova chamada aqui!
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato completo da conta."""
    print("\n=============== EXTRATO ===============")
    
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    
    print("---------------------------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=======================================")
    
    pausar_e_limpar() # Nova chamada aqui!

def main():
    """Função principal que orquestra a execução do sistema bancário."""
    saldo = 0.0
    extrato = []
    numero_saques = 0
    
    limpar_tela()
    print("Bem-vindo ao nosso novo sistema bancário!")
    time.sleep(2) # Uma pequena pausa para o usuário ler a mensagem de boas-vindas
    limpar_tela()

    while True:
        opcao = exibir_menu()

        if opcao == 'd':
            limpar_tela()
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == 's':
            limpar_tela()
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                extrato=extrato, 
                numero_saques=numero_saques
            )

        elif opcao == 'e':
            limpar_tela()
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'q':
            limpar_tela()
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("\nERRO: Operação inválida. Por favor, selecione uma das opções do menu.")
            time.sleep(2)
            limpar_tela()

if __name__ == "__main__":
    main()
