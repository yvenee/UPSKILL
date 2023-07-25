from produto import *
from emprestimo import *

class Gestao:
    
    # contrutores
    def __init__(self):
   
        self.produtos = []
        self.emprestimos = []

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
        print("Produto adicionado com sucesso!\n")
        
    
    def obter_produtos(self):
        if self.produtos:
            print("------------ PRODUTOS ------------")
            for p in self.produtos:
                print(p)
            print("----------------------------------")
        else:
            print("Não há produtos no momento!")


    def atualizar_produto(self, produto):
        for p in self.produtos:
            if p["Título"] == produto:
                print("Qual das opções deseja atualizar:")
                print("1. Título")
                print("2. Tipo de Media")
                print("3. Data da Aquisição")
                print("4. Preço")
                print("0. Voltar")

                while True:
                    op = input("Digite a opção desejada: ")

                    if op == "1":
                        novo_titulo = input("Insira o novo título do produto: ").upper() 
                        for pr in self.produtos:
                            if pr["Título"] == novo_titulo:
                                print("Já existe um produto com o mesmo título!")
                                break
                        else:
                            p["Título"] = novo_titulo
                            print("O título do produto foi atualizado com sucesso!") 
                            return    

                    elif op == "2":
                        print("Escolha um dos tipos de media abaixo: ") 
                        print("1. Publicação") 
                        print("2. Vídeo") 
                        print("3. Áudio") 
                        print("0. Voltar")

                        while True:
                            opcao = input("Opção: ")
                            
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
                                print("As informações do produto foram atualizadas com sucesso!") 
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
                                print("As informações do produto foram atualizadas com sucesso!") 
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
                                print("As informações do produto foram atualizadas com sucesso!")
                                return
                            elif opcao == "0":
                                break
                            else:
                                print("Opção incorreta!")

                    elif op == "3":
                        nova_data = input("Insira a nova data de aquisição (dd/mm/aaaa): ") 
                        p["Data_Aquisição"] = nova_data
                        print("A data de aquisição do produto foi atualizada com sucesso!")
                        return

                    elif op == "4":
                        novo_preco = float(input("Insira o novo preço "))
                        p["Preço"] = novo_preco
                        print("O preço do produto foi atualizado com sucesso!")
                        return

                    elif op == "0":
                        break

                    else: 
                        print("Opção incorreta!")
                
            else: 
                print("Produto não encontrado!")
                return
    
    def eliminar_produto(self, produto):
        for p in self.produtos:
            if p["Título"] == produto:
                self.produtos.remove(p)
                print("Produto eliminado com sucesso!")
                return

            else: 
                print("Produto não encontrado!")
        return


############################################################################################# 
##################################  GESTÃO DE EMPRÉSTIMOS  ################################## 
#############################################################################################
 

    def listar_produtos_disponivel(self):
        print("----------- PRODUTOS DISPONÍVEIS PARA EMPRÉSTIMO ----------")
        produtos_disponiveis = [p["Título"] for p in self.produtos if p["Estado"] == "disponível"]
        
        if produtos_disponiveis:
            for titulo in produtos_disponiveis:
                print(titulo)
        else:
            print("Não há produtos disponíveis para empréstimo!")
        print("-----------------------------------------------------------")

    def criar_emprestimo(self, emprestimo):
       
        self.listar_produtos_disponivel()
        produto = input("Digite o título do produto a emprestar: ").upper()  
        for p in self.produtos:
            # verifica se existe o produto na lista produto        
            if p["Título"] == produto:
                # verifica se o produto tem o estado emprestado
                if p["Estado"] == "emprestado":
                    print("Produto possui empréstimo em aberto!")
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
                    print("Empréstimo adicionado com sucesso!\n")
                    return

            else: 
                print("Produto não encontrado!")
                return

    def obter_emprestimos(self):        
        if self.emprestimos:
            print("----------- EMPRÉSTIMOS ----------")
            for e in self.emprestimos:
                print(e)
            print("----------------------------------")
        else:
            print("Não há empréstimos no momento!")

    def atualizar_emprestimo(self, produto):
        for e in self.emprestimos:
            if e["Título"] == produto:
                print("Qual das opções deseja atualizar:")
                print("1. Nome")
                print("2. Produto")
                print("3. Data do Empréstimo")
                print("3. Data da Devolução")
                print("0. Voltar")

                while True:
                    op = input("Digite a opção desejada: ")

                    if op == "1":
                        novo_nome= input("Insira o novo nome do tomador do empréstimo: ").upper() 
                        e["Nome"] = novo_nome
                        print("Empréstimo atualizado com sucesso!")
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
                        print("Empréstimo atualizado com sucesso!")
                        return

                    elif op == "3":
                        nova_data= input("Insira a nova data do empréstimo (dd/mm/aaaa): ")
                        e["Data_emp"] = nova_data
                        print("Empréstimo atualizado com sucesso!")
                        return 

                    elif op == "4":
                        nova_data= input("Insira a nova data de devolução do empréstimo (dd/mm/aaaa): ")
                        e["Data_devol"] = nova_data
                        print("Empréstimo atualizado com sucesso!")
                        return     

                    elif op == "0":
                        break

                    else: 
                        print("Opção incorreta!")
                
            else: 
                print("Produto não encontrado!")
                return

    def entregar_produto(self, produto, data_devol):
        for emprestimo in self.emprestimos:
            if emprestimo["Título"] == produto:
                if emprestimo["Estado"] == Produto.estado[1]:  # Verifica se o produto está emprestado                    
                    opcao = input("Deseja entregar o produto (S/N)? ").upper()
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
                        
                        print("Produto devolvido com sucesso!")
                        return
                                                
                    elif opcao == "N":
                        return
                    else:
                        print("Opção inválida!")
                        return
                else:
                    print("O produto não está emprestado!")
                    return
            else: 
                print("Produto não existe!")
            return
        else:
            print("Não existem produtos emprestados!")
            return
 
    
    def eliminar_emprestimo(self, produto):
        for p in self.emprestimos:
            if p["Título"] == produto:
                self.emprestimos.remove(p)
                print("Empréstimo eliminado com sucesso!")
                return

            else: 
                print("Empréstimo não encontrado!")
        return

############################################################################################# 
######################################  RELARÓRIOS  ######################################### 
############################################################################################# 

    
    def listar_produtos_alfa(self):
        produtos_ordenados_alfa = sorted(self.produtos, key=lambda produto: produto["Título"])
        print(produtos_ordenados_alfa)

    def listar_produtos_data(self):
        produtos_ordenados_data = sorted(self.produtos, key=lambda produto: produto["Data_Aquisição"], reverse=True)
        print(produtos_ordenados_data)

    def listar_produtos_emprestados(self):
        for p in self.produtos:
            if p["Estado"] == "emprestado":
                print(p)

    def historico_emprestimos(self, produto):
        produtos_ordenados_data_emp = sorted(self.emprestimos, key=lambda emprestimo: emprestimo["Data_emp"], reverse=True)
        for p in produtos_ordenados_data_emp:
            if p["Título"] == produto:
                print("Histórico de Empréstimos do Produto ->", produto)
                print(p)
                for prod in self.produtos:
                    if prod["Título"] == produto:
                        print("Estado Atual:", prod["Estado"])
                        

""" def historico_emprestimos(self, produto):
    produtos_ordenados_data_emp = sorted(self.emprestimos, key=lambda emprestimo: emprestimo["Data_emp"], reverse=True)
    for p in produtos_ordenados_data_emp:
        if p["Título"] == produto:
            for prod in self.produtos:
                if prod["Título"] == produto:
                    print("Estado Atual:", prod["Estado"])
                    print("Histórico de Empréstimos do Produto ->", produto)
                    print(p)
                    break  # Adicionado para evitar imprimir histórico de outros produtos
 """
        