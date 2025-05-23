import os

# SUBMENU GESTÃO DE VENDAS:

def menu_vendas():

        print("**************************")
        print(" MENU - GESTÃO DE VENDAS")
        print("**************************")
        print()                                        #CRUD          SQL
        print("1. Registar Venda")                    #CREATE     #INSERT INTO
        print("2. Listar Vendas")                     #READ       #SELECT
        print("3. Vendas por dia")                    #READ       #SELECT
        print("4. Vendas por produto")                #READ       #SELECT
        print("5. Vendas por mês")                    #READ       #SELECT
        print("6. Anular Venda")                      #DELETE     #DELETE
        print("7. Voltar ao menu anterior")
        print()

def main_vendas():
    while True:
        menu_vendas()
        opcao = input("Escolha uma opção (1 - 7): ")

        if opcao == "1":
            os.system('python A03_01.Create.py venda')
        elif opcao == "2":
            os.system('python A03_02.Read.py venda1')
        elif opcao == "3":
            os.system('python A03_02.Read.py venda2')
        elif opcao == "4":
            os.system('python A03_02.Read.py venda3')
        elif opcao == "5":
            os.system('python A03_02.Read.py venda4')
        elif opcao == "6":
            os.system('python A03_04.Delete.py venda')
        elif opcao == "7":
            os.system('python A05_01.Main_MenuPrincipal.py')
        else:
            print("Opção inválida! Deve ser de 1 a 7.")

if __name__ == "__main__":
    main_vendas()