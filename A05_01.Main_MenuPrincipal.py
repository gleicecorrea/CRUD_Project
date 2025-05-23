
import os


# MENU PRINCIPAL:

def show_menu():
        print("****************************")
        print("        MENU PRINCIPAL     ")
        print("  Gestão - Loja Just Balls")
        print("****************************")
        print()
        print("1. Gestão de produtos")
        print("2. Gestão de vendas")
        print("3. Sair do programa")
        print()

def main():
    while True:
        show_menu()
        opcao = input("Escolha uma opção (1 - 3): ")

        if opcao == "1":
            os.system('python A05_02.SubMenu_GestaoProdutos.py')
        elif opcao == "2":
            os.system('python A05_03.SubMenu_GestaoVendas.py')
        elif opcao == "3":
            print("Obrigado por utilizar o nosso programa!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
