from datetime import datetime
import uuid

##### Produto ######

class Produto:

    estado = ("disponível", "emprestado", "devolvido")
    tipo = ("Publicação", "Vídeo", "Áudio")

    def __init__(self, titulo, preco, data):
        self.__id = Produto.criar_id()
        self.__titulo = titulo       
        self.__tipo = Produto.escolher_tipo(self)
        self.__data = data
        self.__preco = preco
        self.__estado = Produto.estado[0]

    def criar_id():
        id = uuid.uuid4()    
        return str(id)

    def escolher_tipo(self):
        print("Escolha um tipo de media: ")
        print("1. Publicação em Papel/Eletrónica")
        print("2. Vídeo")
        print("3. Áudio")
        print("0. Sair")

        while True:
            opcao = input("Opção: ")
        
            if opcao == "1":
                self.__tipo = Produto.tipo[0]          
                tipo = input("Indique o tipo de publicação (livro, revista etc.): ").upper()
                data = input("Indique a data de publicação (dd/mm/aaaa): ")
                editora = input("Indique a editora: ").upper()
                autores = input("Indique os autores: ").upper()
                suporte = input("Indique o suporte da publicação (papel ou eletrónica): ").upper()
                publicacao = Publicacao(tipo, data, editora, autores, suporte)
                pub_dict = {
                                "Tipo de Media" : self.__tipo,
                                "Tipo de Publicação" : publicacao.tipo_pub,
                                "Data da Publicação" : publicacao.data_pub,
                                "Editora" : publicacao.editora,
                                "Autores" : publicacao.autores,
                                "Suporte" : publicacao.suporte,
                                                                }
                return pub_dict

            elif opcao == "2":
                self.__tipo = Produto.tipo[1]
                duracao = input("Indique a duração em minutos: ")
                tipo = input("Indique o tipo (filme, documentário etc.): ").upper()
                atores = input("Indique os atores: ").upper()
                video = Video(duracao, tipo, atores)
                video_dict = {
                            "Tipo de Media" : self.__tipo,
                            "Duração" : video.duracao,
                            "Tipo de Vídeo" : video.tipo_video,
                            "Atores" : video.atores,
                                                            }
                return video_dict

            elif opcao == "3":
                self.__tipo = Produto.tipo[2]
                duracao = input("Indique a duração em minutos: ")
                suporte = input("Indique o tipo (CD, DVD etc.): ").upper()
                trilhas = input("Indique as trilhas: ").upper()
                audio = Audio(duracao, suporte, trilhas)
                audio_dict = {
                            "Tipo de Media" : self.__tipo,
                            "Duração" : audio.duracao,
                            "Suporte" : audio.suporte,
                            "Trilhas" : audio.trilhas,
                                                            }
                return audio_dict
            
            elif opcao == "0":
                break

            else: 
                print("Opção incorreta!")



    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data    

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco    

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado 

class Publicacao:

    def __init__(self, tipo_pub, data_pub, editora, autores, suporte):        
        self.tipo_pub = tipo_pub
        self.data_pub = data_pub
        self.editora = editora
        self.autores = autores
        self.suporte = suporte

class Video:

    def __init__(self, duracao, tipo_video, atores):        
        self.duracao = duracao
        self.tipo_video = tipo_video
        self.atores = atores

    
class Audio:

    def __init__(self, duracao, suporte, trilhas):        
        self.duracao = duracao
        self.suporte = suporte
        self.trilhas = trilhas


##### Empréstimos ######

class Emprestimo:


    def __init__(self, nome, data_emp, data_devol):
        self.__id = Emprestimo.criar_id()
        self.__produto = None       
        self.__nome = nome
        self.__data_emp = data_emp
        self.__data_devol = data_devol
    

    def criar_id():
        id = uuid.uuid4()    
        return str(id)
    
    def get_id(self):
        return self.__id

    def get_produto(self):
        return self.__produto

    def set_produto(self, produto):
        self.__produto = produto     
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_data_emp(self):
        return self.__data_emp
    
    def set_data_emp(self, data_emp):
        self.__data_emp = data_emp   

    def get_data_devol(self):
        return self.__data_devol
    
    def set_data_devol(self, data_devol):
        self.__data_devol = data_devol    
  
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado


##### Gestão ######


# Atenção professores : 
# 1. Nos métodos "obter_produtos", "obter_empréstimo" e outros que enviam o dicionário como print para no terminal não foram alteradas nesta fase do projecto, pois a parte da interface será realizada no tkinter.
# 2. A data do empréstimo não foi setada automaticamente para permitir que o utilizador faça registo de empréstimos anteriores à data atual.



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
                        formato = "%d/%m/%Y"  # Formato esperado para a data
                        while True:
                            nova_data = input("Insira a nova data de aquisição (dd/mm/aaaa): ") 
                            if self.validar_data(nova_data):
                                break
                            print("Data inválida. Digite uma data válida no formato dd/mm/aaaa.")
                        data_aqui_date = datetime.strptime(nova_data, formato).date()
                        if data_aqui_date > datetime.now().date():
                            print("A data da aquisição não pode ser maior que a data do dia atual!")
                            return
                        else:                        
                            p["Data_Aquisição"] = nova_data
                            print("A data de aquisição do produto foi atualizada com sucesso!")
                            return

                    elif op == "4":
                        while True:
                            novo_preco = input("Insira o novo preço: ")
                            if self.validar_float(novo_preco):
                                novo_preco = float(novo_preco)
                                break
                            print("Preço inválido. Digite um número válido!")
                                            
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
                          
                        

##### Menu ######

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
