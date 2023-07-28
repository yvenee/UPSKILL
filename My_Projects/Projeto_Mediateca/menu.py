from gestao import *
from produto import *
from emprestimo import *
from datetime import datetime
import time
import os

def limpar_terminal():
    os.system('clear')

if __name__ == "__main__":

    gestao = Gestao()
    formato = "%d/%m/%Y"    

    def validar_float(valor):        
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def validar_data(data):
        try:
            dia, mes, ano = map(int, data.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900:
                return True
            return False
        except:
            return False
        
    
    def menu_principal():
        limpar_terminal()
        print("Bem-vindo à Mediateca!\n")
        while True:
        
            print("Menu\n")
            print("1. Gestão de Produtos")
            print("2. Gestão de Empréstimos")
            print("3. Relatórios")
            print("0. Sair")
       
            opcao = input("\nDigite o número da opção desejada: ")
            print()
            
            if opcao == "1":
                menu_gestão_produtos()      

            elif opcao == "2":
                menu_gestão_emprestimos()

            elif opcao == "3":
                menu_relatorios()
        
            elif opcao == "0":
                while True:
                    val = input("Tem certeza que deseja sair (S/N)? ").upper()
                    if val == "N":
                        menu_principal()
                    elif val == "S":
                        limpar_terminal()
                        print("A sair...\n")
                        break
                    else:
                        print("Opção inválida!\n")
                        time.sleep(1)
                        limpar_terminal()

                return

            else:
                print("Opção inválida. Tente novamente.\n")
                time.sleep(1)
                limpar_terminal()



    def menu_gestão_produtos():
        limpar_terminal()
        
        while True:
            print("Gestão de Produtos\n")
            print("1. Criar Produtos")
            print("2. Obter Produtos")
            print("3. Atualizar Produtos")
            print("4. Eliminar Produtos")
            print("0. Voltar\n")

            opcao = input("Digite o número da opção desejada: ")
            print()
                        
            if opcao == "1":
                limpar_terminal()
                print("CRIAR PRODUTO\n")
                titulo = input("Digite o título do produto: ").upper()
                for p in gestao.produtos:
                    if p["Título"] == titulo:                
                        print("Já existe um produto com o mesmo título!\n")
                        time.sleep(2)
                        limpar_terminal()
                        break
                        
                else:
                    preco = input("Digite o preço do produto: ")
                    while not validar_float(preco):
                        print("\nPreço inválido. Digite um número válido!\n")
                        preco = input("Digite o preço do produto: ")
                    preco = float(preco)
                    formato = "%d/%m/%Y"  # Formato esperado para a data
                    while True:
                        data_aquisicao = input("Indique a data de aquisição (dd/mm/aaaa): ")
                        print()
                        if validar_data(data_aquisicao):
                            break
                        print("\nData inválida. Digite uma data válida no formato dd/mm/aaaa.\n")

                    data_aqui_date = datetime.strptime(data_aquisicao, formato).date()
                    if data_aqui_date > datetime.now().date():
                        print("\nA data da aquisição não pode ser maior que a data do dia atual!\n")
                        return
                    else:
                        produto = Produto(titulo, preco, data_aqui_date)
                        gestao.criar_produto(produto)               

            elif opcao == "2":
                limpar_terminal()
                print("OBTER PRODUTOS\n")                
                gestao.obter_produtos()

            elif opcao == "3":
                limpar_terminal()                                
                print("ATUALIZAR PRODUTOS\n")
                titulo = input("Digite o título do produto: ").upper()               
                gestao.atualizar_produto(titulo)
                
            elif opcao == "4":
                limpar_terminal()
                print("ELIMINAR PRODUTOS\n")
                titulo = input("Digite o título do produto: ").upper()
                print()
                gestao.eliminar_produto(titulo)

            elif opcao == "0":   
                limpar_terminal()             
                break

            else:
                print("Opção inválida. Tente novamente.\n")
                time.sleep(1)                
                limpar_terminal()

    def menu_gestão_emprestimos(): 

        limpar_terminal()      
        
        while True:

            print("Gestão de Empréstimos\n")
            print("1. Criar Empréstimo")
            print("2. Obter Empréstimos")
            print("3. Atualizar Empréstimos")
            print("4. Entregar Produtos Emprestados")
            print("5. Eliminar Empréstimos")
            print("0. Voltar\n")

            opcao = input("Digite o número da opção desejada: ")
            print()
            formato = "%d/%m/%Y"  # Formato esperado para a data

            if opcao == "1":
                limpar_terminal()
                print("CRIAR EMPRÉSTIMO\n")
                print("\nPRODUTOS DISPONÍVEIS PARA EMPRÉSTIMO:\n")
                produtos_disponiveis = [p["Título"] for p in gestao.produtos if p["Estado"] == "disponível"]
                
                if produtos_disponiveis:
                    for titulo in produtos_disponiveis:
                        print(titulo)
                        
                else:
                    print("\nNão há produtos disponíveis para empréstimo!\n")
                    time.sleep(5)
                    limpar_terminal()
                    return
                print("------------------------------------------------\n")
                nome = input("Digite o nome do tomador do empréstimo: ").upper()                
                data_emprestimo = input("Digite a data do empréstimo (dd/mm/aaaa): ")
                data_emp_date = datetime.strptime(data_emprestimo, formato).date()
                # Verifica se a data do empréstimo é posterior que a data atual
                if data_emp_date > datetime.now().date():
                    print("\nA data do empréstimo não pode ser maior que a data do dia atual!\n")
                    return 
                # Verifica se a data de empréstimo é anterior à data de aquisição de algum produto
                for p in gestao.produtos:
                    if data_emp_date < p["Data_Aquisição"]:
                        print("\nA data do empréstimo não pode ser anterior à data da aquisição do produto!\n")
                        return               
            
                data_devolucao = input("Digite a data da devolução do empréstimo (dd/mm/aaaa): ")
                data_devol_date = datetime.strptime(data_devolucao, formato).date()
                # Verifica se a data de devolução é anterior à data de empréstimo
                if data_devol_date < data_emp_date:
                    print("\nA data de devolução do empréstimo não pode ser menor que a data do empréstimo!\n")
                    return
                else:
                    emprestimo = Emprestimo(nome, data_emprestimo, data_devolucao)
                    gestao.criar_emprestimo(emprestimo)
                    

            elif opcao == "2":
                limpar_terminal()  
                print("OBTER EMPRÉSTIMOS\n")  
                gestao.obter_emprestimos()

            elif opcao == "3":
                limpar_terminal()  
                print("ATUALIZAR EMPRÉSTIMO\n") 
                titulo = input("Digite o título do produto: ").upper()          
                gestao.atualizar_emprestimo(titulo)
                
            elif opcao == "4":
                limpar_terminal()  
                print("ENTREGAR PRODUTO\n")  
                titulo = input("Digite o título do produto: ").upper()
                data_devolucao = input("Digite a data da devolução do empréstimo (dd/mm/aaaa): ")
                data_devol_date = datetime.strptime(data_devolucao, formato).date()
                # Verifica se a data de devolução é anterior à data de empréstimo
                for e in gestao.emprestimos:
                    data_emp = datetime.strptime(e["Data_emp"], formato).date()
                    if data_devol_date < data_emp or data_devol_date > datetime.now().date():
                        print("\nA data de devolução do empréstimo não pode ser anterior à data do empréstimo ou superior à data de hoje!\n")
                        return
                    else:        
                        gestao.entregar_produto(titulo, data_devol_date)
                        return

            elif opcao == "5":
                limpar_terminal()  
                print("ELIMINAR EMPRÉSTIMO\n")  
                titulo = input("Digite o título do produto: ").upper()
                gestao.eliminar_emprestimo(titulo)

            elif opcao == "0":
                limpar_terminal()                
                break

            else:
                print("\nOpção inválida. Tente novamente.\n")
                time.sleep(1)                
                limpar_terminal()

    def menu_relatorios():
        
        limpar_terminal()

        while True:

            print("Relatórios\n")    
            print("1. Listar Produtos Multimédia")
            print("2. Listar Produtos Emprestados")
            print("3. Histórico de Empréstimos")   
            print("0. Voltar\n")

            opcao = input("Digite o número da opção desejada: ")
            print()

            if opcao == "1":
                limpar_terminal()
                menu_produtos_multimedia()             

            elif opcao == "2":                
                limpar_terminal()
                gestao.listar_produtos_emprestados()

            elif opcao == "3":
                limpar_terminal()
                titulo = input("Digite o título do produto: ").upper() 
                gestao.historico_emprestimos(titulo)  
        
            elif opcao == "0":  
                limpar_terminal()              
                break

            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(1)                
                limpar_terminal()

    def menu_produtos_multimedia():

        while True:

            print("Relatórios Produtos Mutimédia\n")   
            print("1. Listar Produtos por Ordem Alfabética")
            print("2. Listar Produtos por Data Decrescente")
            print("0. Voltar\n")

            opcao = input("Digite o número da opção desejada: ")
            print()

            if opcao == "1":
                limpar_terminal()
                gestao.listar_produtos_alfa()

            elif opcao == "2":
                limpar_terminal()
                gestao.listar_produtos_data()

            elif opcao == "0":  
                limpar_terminal()              
                break

            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(1)                
                limpar_terminal()


    menu_principal()
