from produto import *
from emprestimo import *
import os
import time

# Atenção professores : 
# 1. Nos métodos "obter_produtos", "obter_empréstimo" e outros que enviam o dicionário como print para no terminal não foram alteradas nesta fase do projecto, pois a parte da interface será realizada no tkinter.
# 2. A data do empréstimo não foi setada automaticamente para permitir que o utilizador faça registo de empréstimos anteriores à data atual.

def limpar_terminal():
    os.system('clear')


class Gestao:
    
    # contrutores
    def __init__(self):
   
        self.produtos = []
        self.emprestimos = []

    @staticmethod # usado para não ser necessário passar o self como argumento       
    def validar_float(valor):        
        try:
            float(valor)
            return True
        except ValueError:
            return False

    @staticmethod
    def validar_data(data):
        try:
            dia, mes, ano = map(int, data.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900:
                # Verifica se a data é válida usando o datetime.strptime
                formato = "%d/%m/%Y"
                datetime.strptime(data, formato)
                return True
            return False
        except ValueError:
            return False
            
############################################################################################# 
####################################  GESTÃO DE PRODUTOS  ################################### 
############################################################################################# 

    def criar_produto(self, produto):
        dict_produtos = {
                            "ID" : produto.get_id(),
                            "Título" : produto.get_titulo(),
                            "Media" : produto.get_tipo(),
                            "Data_Aquisição" : produto.get_data(),
                            "Preço" : produto.get_preco(),
                            "Estado" : produto.get_estado()
                                                            }
        self.produtos.append(dict_produtos) 
        print("\nProduto adicionado com sucesso!\n")
        time.sleep(1)
        limpar_terminal()
        
        
    
    def obter_produtos(self):
        if self.produtos:
            print("PRODUTOS:\n")
            for p in self.produtos:
                print(p)
            print("-------------------------------------------------------------------------------------------------------------\n")
            time.sleep(5)
            return
        else:
            print("Não há produtos no momento!\n")


    def atualizar_produto(self, produto):
        for p in self.produtos:
            if p["Título"] == produto:
                print("\nQual das opções deseja atualizar:")
                print("1. Título")
                print("2. Tipo de Media")
                print("3. Data da Aquisição")
                print("4. Preço")
                print("0. Voltar\n")

                while True:
                    op = input("Digite a opção desejada: ")
                    print()

                    if op == "1":
                        novo_titulo = input("Insira o novo título do produto: ").upper() 
                        for pr in self.produtos:
                            if pr["Título"] == novo_titulo:
                                print("Já existe um produto com o mesmo título!\n")
                                break
                        else:
                            p["Título"] = novo_titulo
                            print("O título do produto foi atualizado com sucesso!\n")
                            time.sleep(2)
                            limpar_terminal() 
                            return    

                    elif op == "2":
                        print("\nEscolha um dos tipos de media abaixo: ") 
                        print("1. Publicação") 
                        print("2. Vídeo") 
                        print("3. Áudio") 
                        print("0. Voltar\n")

                        while True:
                            opcao = input("Opção: ")
                            print()
                            
                            if opcao == "1":                           
                                # Limpa o dicionário atual
                                p["Media"].clear()
                                # Adiciona as novas chaves e respetivos valores
                                tipo = input("Indique o tipo de publicação (livro, revista etc.): ").upper()
                                data = input("Indique a data de publicação (dd/mm/aaaa): ")
                                editora = input("Indique a editora: ").upper()
                                autores = input("Indique os autores: ").upper()
                                suporte = input("Indique o suporte da publicação (papel ou eletrónica): ").upper()
                                p["Media"]["Tipo de Media"] = Produto.tipo[0]
                                p["Media"]["Tipo de Publicação"] = tipo
                                p["Media"]["Data da Publicação"] = data
                                p["Media"]["Editora"] = editora
                                p["Media"]["Autores"] = autores
                                p["Media"]["Suporte"] = suporte
                                print("\nAs informações do produto foram atualizadas com sucesso!\n")
                                time.sleep(2)
                                limpar_terminal()
                                return

                            elif opcao == "2":
                                # Limpa o dicionário atual
                                p["Media"].clear()
                                # Adiciona as novas chaves e respetivos valores
                                duracao = input("Indique a duração em minutos: ")
                                tipo = input("Indique o tipo (filme, documentário etc.): ").upper()
                                atores = input("Indique os atores: ").upper()
                                p["Media"]["Tipo de Media"] = Produto.tipo[1]
                                p["Media"]["Duração"] = duracao
                                p["Media"]["Tipo de Vídeo"] = tipo
                                p["Media"]["Atores"] = atores
                                print("\nAs informações do produto foram atualizadas com sucesso!\n")
                                time.sleep(2)
                                limpar_terminal()
                                return 
                                
                            elif opcao == "3":
                                # Limpa o dicionário atual
                                p["Media"].clear()
                                # Adiciona as novas chaves e respetivos valores
                                duracao = input("Indique a duração em minutos: ")
                                suporte = input("Indique o tipo (CD, DVD etc.): ").upper()
                                trilhas = input("Indique as trilhas: ").upper()
                                p["Media"]["Tipo de Media"] = Produto.tipo[2]
                                p["Media"]["Duração"] = duracao
                                p["Media"]["Suporte"] = suporte
                                p["Media"]["Trilhas"] = trilhas
                                print("\nAs informações do produto foram atualizadas com sucesso!\n")
                                time.sleep(2)
                                limpar_terminal()
                                return
                            elif opcao == "0":
                                break
                            else:
                                print("Opção incorreta!\n")

                    elif op == "3":
                        formato = "%d/%m/%Y"  # Formato esperado para a data
                        while True:
                            nova_data = input("Insira a nova data de aquisição (dd/mm/aaaa): ") 
                            if self.validar_data(nova_data):
                                break
                            print("\nData inválida. Digite uma data válida no formato dd/mm/aaaa.\n")
                        data_aqui_date = datetime.strptime(nova_data, formato).date()
                        if data_aqui_date > datetime.now().date():
                            print("\nA data da aquisição não pode ser maior que a data do dia atual!\n")
                            return
                        else:                        
                            p["Data_Aquisição"] = nova_data
                            print("\nA data de aquisição do produto foi atualizada com sucesso!\n")
                            time.sleep(2)
                            limpar_terminal()
                            return

                    elif op == "4":
                        while True:
                            novo_preco = input("Insira o novo preço: ")
                            if self.validar_float(novo_preco):
                                novo_preco = float(novo_preco)
                                break
                            print("\nPreço inválido. Digite um número válido!\n")
                                            
                        p["Preço"] = novo_preco
                        print("\nO preço do produto foi atualizado com sucesso!\n")
                        time.sleep(2)
                        limpar_terminal()
                        return

                    elif op == "0":
                        break

                    else: 
                        print("\nOpção incorreta!\n")
                
        print("\nProduto não encontrado!\n")
        time.sleep(1)
        limpar_terminal()
        
    
    def eliminar_produto(self, produto):
        for p in self.produtos:
            if p["Título"] == produto:
                if p["Estado"] == "emprestado" or p["Estado"] == "devolvido":
                    print("Não é possível eliminar o produto uma vez emprestado!\n")
                    time.sleep(1)
                    limpar_terminal()
                    return
                else: 
                    self.produtos.remove(p)
                    print("Produto eliminado com sucesso!\n")
                    time.sleep(1)
                    limpar_terminal()
                    return
        print("Produto não encontrado!\n")
        time.sleep(1)
        limpar_terminal()
        


############################################################################################# 
##################################  GESTÃO DE EMPRÉSTIMOS  ################################## 
#############################################################################################
        

    def criar_emprestimo(self, emprestimo):       
        
        produto = input("Digite o título do produto a emprestar: ").upper()  
        for p in self.produtos:
            # verifica se existe o produto na lista produto        
            if p["Título"] == produto:
                # verifica se o produto tem o estado emprestado
                if p["Estado"] == "emprestado":
                    print("\nProduto possui empréstimo em aberto!\n")
                    time.sleep(2)
                    limpar_terminal()
                    return
                else:
                    emprestimo.set_produto(produto)                   
                    p["Estado"] = Produto.estado[1]
                    
                    dict_emprestimo = {
                                        "Produto_ID" : p["ID"],
                                        "Título" : emprestimo.get_produto(),
                                        "Estado" : p["Estado"],
                                        "Empréstimo_ID" : emprestimo.get_id(),
                                        "Nome" : emprestimo.get_nome(),
                                        "Data_emp" : emprestimo.get_data_emp(),
                                        "Data_devol" : emprestimo.get_data_devol()
                                    }
                    self.emprestimos.append(dict_emprestimo) 
                    print("\nEmpréstimo adicionado com sucesso!\n")
                    time.sleep(2)
                    limpar_terminal()
                    return

        print("Produto não encontrado!\n")
        time.sleep(1)
        limpar_terminal()
              

    def obter_emprestimos(self):        
        if self.emprestimos:
            print("EMPRÉSTIMOS:\n")
            for e in self.emprestimos:
                print(e)
            print("----------------------------------------------------------------------------------------------------------\n")
            time.sleep(5)
            limpar_terminal()
        else:
            print("Não há empréstimos no momento!")
            time.sleep(2)
            limpar_terminal()

    def atualizar_emprestimo(self, produto):
        for e in self.emprestimos:
            if e["Título"] == produto:
                print("\nQual das opções deseja atualizar:")
                print("1. Nome")
                print("2. Produto")
                print("3. Data do Empréstimo")
                print("3. Data da Devolução")
                print("0. Voltar\n")

                while True:
                    op = input("Digite a opção desejada: ")
                    print()

                    if op == "1":
                        novo_nome= input("Insira o novo nome do tomador do empréstimo: ").upper() 
                        e["Nome"] = novo_nome
                        print("\nEmpréstimo atualizado com sucesso!\n")
                        time.sleep(2)
                        limpar_terminal()
                        return    

                    elif op == "2":
                        novo_produto = input("Insira o título do novo produto a ser emprestado: ").upper()
                        for p in self.produtos:
                            if p["Título"] == novo_produto:
                                e["Título"] = novo_produto
                                e["Produto_ID"] = p["ID"]
                                p["Estado"] = Produto.estado[1] #altera o estado do novo produto para emprestado
                                
                            if p["Título"] == produto:
                                p["Estado"] = Produto.estado[0] #altera o estado do antigo produto para disponível
                        print("\nEmpréstimo atualizado com sucesso!\n")
                        time.sleep(2)
                        limpar_terminal()
                        return

                    elif op == "3":
                        nova_data= input("Insira a nova data do empréstimo (dd/mm/aaaa): ")
                        e["Data_emp"] = nova_data
                        print("\nEmpréstimo atualizado com sucesso!\n")
                        time.sleep(2)
                        limpar_terminal()
                        return 

                    elif op == "4":
                        nova_data= input("Insira a nova data de devolução do empréstimo (dd/mm/aaaa): ")
                        e["Data_devol"] = nova_data
                        print("\nEmpréstimo atualizado com sucesso!\n")
                        time.sleep(2)
                        limpar_terminal()
                        return     

                    elif op == "0":
                        limpar_terminal()
                        break

                    else: 
                        print("Opção incorreta!\n")
                        time.sleep(1)
                        limpar_terminal()
        print("Produto não encontrado!\n")
        time.sleep(3)
        limpar_terminal()

    def entregar_produto(self, produto, data_devol):
        for emprestimo in self.emprestimos:
            if emprestimo["Título"] == produto:
                if emprestimo["Estado"] == Produto.estado[1]:  # Verifica se o produto está emprestado                    
                    opcao = input("Deseja entregar o produto (S/N)? ").upper()
                    print()
                    if opcao == "S":
                        # Atualiza o estado do produto na lista de produtos
                        for produto_lista in self.produtos:
                            if produto_lista["Título"] == produto:
                                produto_lista["Estado"] = Produto.estado[0]  # estado disponível

                        # Adiciona o empréstimo devolvido à lista de empréstimos
                        emp = Emprestimo(emprestimo["Nome"], emprestimo["Data_emp"], data_devol)
                        emprestimo_devolvido = {
                            "Produto_ID": emprestimo["Produto_ID"],
                            "Título": emprestimo["Título"],
                            "Estado": Produto.estado[2],  # estado devolvido
                            "Devolução_ID": emp.get_id(),
                            "Nome": emprestimo["Nome"],
                            "Data_emp": emprestimo["Data_emp"],
                            "Data_devol": data_devol
                        }
                        self.emprestimos.append(emprestimo_devolvido)
                        
                        print("\nProduto devolvido com sucesso!\n")
                        time.sleep(2)
                        limpar_terminal()
                        return
                                                
                    elif opcao == "N":
                        time.sleep(1)
                        limpar_terminal()
                        return
                    else:
                        print("\nOpção inválida!\n")
                        time.sleep(1)
                        limpar_terminal()
                        return
                else:
                    print("\nO produto não está emprestado!\n")
                    time.sleep(3)
                    limpar_terminal()
                    return
            else: 
                print("\nProduto não existe!\n")
                time.sleep(3)
                limpar_terminal()
            return
        else:
            print("\nNão existem produtos emprestados!\n")
            time.sleep(3)
            limpar_terminal()
            return
 
    
    def eliminar_emprestimo(self, produto):
        for p in self.emprestimos:
            if p["Título"] == produto:
                self.emprestimos.remove(p)
                print("\nEmpréstimo eliminado com sucesso!\n")
                time.sleep(4)
                limpar_terminal()
                return
        print("\nEmpréstimo não encontrado!\n")
        time.sleep(3)
        limpar_terminal()
        

############################################################################################# 
######################################  RELARÓRIOS  ######################################### 
############################################################################################# 

    
    def listar_produtos_alfa(self):
        print("Lista de Produtos por Ordem Alfabética:")
        produtos_ordenados_alfa = sorted(self.produtos, key=lambda produto: produto["Título"])
        print(produtos_ordenados_alfa)
        print()

    def listar_produtos_data(self):
        print("Lista de Produtos por Ordem Decrescente de Data:")
        produtos_ordenados_data = sorted(self.produtos, key=lambda produto: produto["Data_Aquisição"], reverse=True)
        print(produtos_ordenados_data)
        print()

    def listar_produtos_emprestados(self):
        print("Lista de Produtos Emprestados:")
        for p in self.produtos:
            if p["Estado"] == "emprestado":
                print(p)
                print()

    def historico_emprestimos(self, produto):
        print("Histórico de Empréstimos:")
        produtos_ordenados_data_emp = sorted(self.emprestimos, key=lambda emprestimo: emprestimo["Data_emp"], reverse=True)
        for p in produtos_ordenados_data_emp:
            if p["Título"] == produto:
                print("Histórico de Empréstimos do Produto ->", produto)
                print(p)
                for prod in self.produtos:
                    if prod["Título"] == produto:
                        print("Estado Atual:", prod["Estado"],"\n")
                        
                          