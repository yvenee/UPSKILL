from gestao import *
from produto import *
from emprestimo import *
from datetime import datetime

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

        while True:
        
            print("#############  Menu  #####################")
            print("1. Gestão de Produtos")
            print("2. Gestão de Empréstimos")
            print("3. Relatórios")
            print("0. Sair")
       
            opcao = input("Digite o número da opção desejada: ")
            print()
            
            if opcao == "1":
                menu_gestão_produtos()      

            elif opcao == "2":
                menu_gestão_emprestimos()

            elif opcao == "3":
                menu_relatorios()
        
            elif opcao == "0":
                print("A sair...")
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_gestão_produtos():
        
        while True:
            print("#############  Menu Gestão de Produtos  #####################")
            print("1. Criar Produtos")
            print("2. Obter Produtos")
            print("3. Atualizar Produtos")
            print("4. Eliminar Produtos")
            print("0. Voltar")

            opcao = input("Digite o número da opção desejada: ")
            print()
            
            if opcao == "1":
                titulo = input("Digite o título do produto: ").upper()
                for p in gestao.produtos:
                    if p["Título"] == titulo:                
                        print("Já existe um produto com o mesmo título!")
                        break
                        
                else:
                    preco = input("Digite o preço do produto: ")
                    while not validar_float(preco):
                        print("Preço inválido. Digite um número válido!")
                        preco = input("Digite o preço do produto: ")
                    preco = float(preco)
                    formato = "%d/%m/%Y"  # Formato esperado para a data
                    while True:
                        data_aquisicao = input("Indique a data de aquisição (dd/mm/aaaa): ")
                        if validar_data(data_aquisicao):
                            break
                        print("Data inválida. Digite uma data válida no formato dd/mm/aaaa.")
                    data_aqui_date = datetime.strptime(data_aquisicao, formato).date()
                    if data_aqui_date > datetime.now().date():
                        print("A data da aquisição não pode ser maior que a data do dia atual!")
                        return
                    else:
                        produto = Produto(titulo, preco, data_aqui_date)
                        gestao.criar_produto(produto)               

            elif opcao == "2":                
                gestao.obter_produtos()

            elif opcao == "3":
                titulo = input("Digite o título do produto: ").upper()               
                gestao.atualizar_produto(titulo)
                
            elif opcao == "4":
                titulo = input("Digite o título do produto: ").upper()
                gestao.eliminar_produto(titulo)

            elif opcao == "0":                
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_gestão_emprestimos():        
        
        while True:

            print("#############  Menu Gestão de Empréstimos  #####################")
            print("1. Criar Empréstimo")
            print("2. Obter Empréstimos")
            print("3. Atualizar Empréstimos")
            print("4. Entregar Produtos Emprestados")
            print("5. Eliminar Empréstimos")
            print("0. Voltar")

            opcao = input("Digite o número da opção desejada: ")
            print()
            formato = "%d/%m/%Y"  # Formato esperado para a data

            if opcao == "1":
                nome = input("Digite o nome do tomador do empréstimo: ").upper()                
                data_emprestimo = input("Digite a data do empréstimo (dd/mm/aaaa): ")
                data_emp_date = datetime.strptime(data_emprestimo, formato).date()
                # Verifica se a data do empréstimo é posterior que a data atual
                if data_emp_date > datetime.now().date():
                    print("A data do empréstimo não pode ser maior que a data do dia atual!")
                    return 
                # Verifica se a data de empréstimo é anterior à data de aquisição de algum produto
                for p in gestao.produtos:
                    if data_emp_date < p["Data_Aquisição"]:
                        print("A data do empréstimo não pode ser anterior à data da aquisição do produto!")
                        return               
            
                data_devolucao = input("Digite a data da devolução do empréstimo (dd/mm/aaaa): ")
                data_devol_date = datetime.strptime(data_devolucao, formato).date()
                # Verifica se a data de devolução é anterior à data de empréstimo
                if data_devol_date < data_emp_date:
                    print("A data de devolução do empréstimo não pode ser menor que a data do empréstimo!")
                    return
                else:
                    emprestimo = Emprestimo(nome, data_emprestimo, data_devolucao)
                    gestao.criar_emprestimo(emprestimo)
                    

            elif opcao == "2":    
                gestao.obter_emprestimos()

            elif opcao == "3":
                titulo = input("Digite o título do produto: ").upper()          
                gestao.atualizar_emprestimo(titulo)
                
            elif opcao == "4":
                titulo = input("Digite o título do produto: ").upper()
                data_devolucao = input("Digite a data da devolução do empréstimo (dd/mm/aaaa): ")
                data_devol_date = datetime.strptime(data_devolucao, formato).date()
                # Verifica se a data de devolução é anterior à data de empréstimo
                for e in gestao.emprestimos:
                    data_emp = datetime.strptime(e["Data_emp"], formato).date()
                    if data_devol_date < data_emp or data_devol_date > datetime.now().date():
                        print("A data de devolução do empréstimo não pode ser anterior à data do empréstimo ou superior à data de hoje!")
                        return
                    else:        
                        gestao.entregar_produto(titulo, data_devol_date)
                        return

            elif opcao == "5":
                titulo = input("Digite o título do produto: ").upper()
                gestao.eliminar_emprestimo(titulo)

            elif opcao == "0":                
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_relatorios():

        while True:

            print("#############  Menu Relatórios  #####################")    
            print("1. Listar Produtos Multimédia")
            print("2. Listar Produtos Emprestados")
            print("3. Histórico de Empréstimos")   
            print("0. Voltar")

            opcao = input("Digite o número da opção desejada: ")
            print()

            if opcao == "1":
                menu_produtos_multimedia()             

            elif opcao == "2":
                gestao.listar_produtos_emprestados()

            elif opcao == "3":
                titulo = input("Digite o título do produto: ").upper() 
                gestao.historico_emprestimos(titulo)  
        
            elif opcao == "0":                
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_produtos_multimedia():

        while True:

            print("#############  Menu Produtos Mutimédia  #####################")   
            print("1. Listar Produtos por Ordem Alfabética")
            print("2. Listar Produtos por Data Decrescente")
            print("0. Voltar")

            opcao = input("Digite o número da opção desejada: ")
            print()

            if opcao == "1":
                gestao.listar_produtos_alfa()

            elif opcao == "2":
                gestao.listar_produtos_data()

            elif opcao == "0":                
                break

            else:
                print("Opção inválida. Tente novamente.")


    menu_principal()
