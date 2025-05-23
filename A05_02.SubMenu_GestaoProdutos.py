import os

# SUBMENU GESTÃO DE PRODUTOS:

def menu_produtos():
        print("*********************************")
        print("    MENU - GESTÃO DE PRODUTOS")
        print("*********************************")
        print()                                            #CRUD          SQL
        print("1. Inserir produto")                       #CREATE    #INSERT INTO
        print("2. Listar produtos")                       #READ      #SELECT
        print("3. Atualizar preço do produto")            #UPDATE    #UPDATE
        print("4. Registar reposição de produto")         #UPDATE    #UPDATE
        print("5. Eliminar produto")                      #DELETE    #DELTE
        print("6. Voltar ao menu anterior")
        print()

def main_produtos():
    while True:
        menu_produtos()
        opcao = input("Escolha uma opção (1 - 6): ")

        if opcao == "1":
            os.system('python A03_01.Create.py produto') #Passando 'produto' como argumento da linha de comandos para
        elif opcao == "2":                                 # que a funcao main do arquivo A03_01.Create.py possa
            os.system('python A03_02.Read.py produto')     #identificar se o comando veio do submenu produto ou venda
        elif opcao == "3":                                 #e para que possa executar a funcao correta.
            os.system('python A03_03.Update.py produtoUp1')
        elif opcao == "4":
            os.system('python A03_03.Update.py produtoUp2')
        elif opcao == "5":
            os.system('python A03_04.Delete.py produto')
        elif opcao == "6":
            os.system('python A05_01.Main_MenuPrincipal.py')
        else:
            print("Opção inválida! Deve ser de 1 a 6.")


if __name__ == "__main__":
    main_produtos()






