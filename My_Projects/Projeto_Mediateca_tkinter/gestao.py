from produto import *
from emprestimo import *
from datetime import datetime


# Atenção professores : 
# 1. A data do empréstimo não foi setada automaticamente para permitir que o utilizador faça registo de empréstimos anteriores à data atual.



class Gestao:
    
    # contrutores
    def __init__(self):
   
        self.produtos = []
        self.emprestimos = []
        self.historico_emprestimos = []

        # Adicione alguns produtos iniciais à lista
        self.produtos.append({
            "ID": 1,
            "Título": "Livro A",
            "Tipo" : "Publicação",
            "Preço": 29.99,
            "Data_Aquisição": datetime(2022, 12, 1).date(),
            "Estado": "disponível",
            "Media": {
                "Tipo de Media": "Publicação",
                "Tipo de Publicação": "Livro",
                "Data da Publicação": datetime(2023, 7, 1).date(),
                "Editora": "Editora XYZ",
                "Autores": "Autor 1, Autor 2",
                "Suporte": "Papel",
            }
        })

        self.produtos.append({
            "ID": 2,
            "Título": "Filme B",
            "Tipo" : "Vídeo",
            "Preço": 19.99,
            "Data_Aquisição": datetime(2020, 7, 4).date(),
            "Estado": "disponível",
            "Media": {
                "Tipo de Media": "Vídeo",
                "Duração": 120,
                "Tipo de Vídeo": "Blu-Ray",
                "Atores": "Ator 1, Ator 2",
            }
        })

        self.produtos.append({
            "ID": 3,
            "Título": "Álbum C",
            "Tipo" : "Áudio",
            "Preço": 9.99,
            "Data_Aquisição": datetime(2000, 1, 4).date(),
            "Estado": "disponível",
            "Media": {
                "Tipo de Media": "Áudio",
                "Duração": 45,
                "Suporte": "CD",
                "Trilhas": "Trilha 1, Trilha 2",
            }
        })

        self.produtos.append({
            "ID": 4,
            "Título": "Álbum D",
            "Tipo" : "Áudio",
            "Preço": 20.99,
            "Data_Aquisição": datetime(2000, 1, 4).date(),
            "Estado": "emprestado",
            "Media": {
                "Tipo de Media": "Áudio",
                "Duração": 34,
                "Suporte": "CD",
                "Trilhas": "Trilha 1, Trilha 2",
            }
        })

  

####################################  GESTÃO DE PRODUTOS  ################################### 
 
    
    def criar_produto(self, produto):
        dict_produtos = {
                            "ID" : produto.get_id(),
                            "Título" : produto.titulo,
                            "Tipo" : produto.tipo,
                            "Media" : produto.tipo_media,
                            "Data_Aquisição" : produto.data,
                            "Preço" : produto.preco,
                            "Estado" : produto.estado
                                                            }
        self.produtos.append(dict_produtos) 
        
    
    def obter_produto(self, produto_id):
        for p in self.produtos:
            if str(p["ID"]) == str(produto_id):
                return p
    
    def eliminar_produto(self, produto_id):
        for p in self.produtos:
            if str(p["ID"]) == str(produto_id):
                self.produtos.remove(p)
            

##################################  GESTÃO DE EMPRÉSTIMOS  ################################## 

 

    def criar_emprestimo(self, emprestimo, produto_id):

        for p in self.produtos:             
            if str(p["ID"]) == produto_id:               
                emprestimo.set_produto(p)                   
                p["Estado"] = Produto.estado[1]

                dict_emprestimo = {
                                    "Produto_ID" : p["ID"],
                                    "Produto" : emprestimo.get_produto(),
                                    "Empréstimo_ID" : emprestimo.get_id(),
                                    "Nome" : emprestimo.get_nome(),
                                    "Data_emp" : emprestimo.get_data_emp(),
                                    "Data_devol" : emprestimo.get_data_devol(),
                                    "Estado_emp" : "Emprestado"
                                }
                self.emprestimos.append(dict_emprestimo) 
                self.historico_emprestimos.append(dict_emprestimo) 
                    

    def obter_emprestimos(self, emprestimo_id):        
        for p in self.emprestimos:
            if str(p["Empréstimo_ID"]) == str(emprestimo_id):
                return p

    
    def eliminar_emprestimo(self, emprestimo):
        for e in self.emprestimos:
            if str(e["Empréstimo_ID"]) == str(emprestimo):                
                self.emprestimos.remove(e)
          
 
######################################  RELARÓRIOS  ######################################### 
    
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

    def listar_historico_emprestimos(self, produto):
        produtos_ordenados_data_emp = sorted(self.emprestimos, key=lambda emprestimo: emprestimo["Data_emp"], reverse=True)
        for p in produtos_ordenados_data_emp:
            if p["Título"] == produto:
                print("Histórico de Empréstimos do Produto ->", produto)
                print(p)
                for prod in self.produtos:
                    if prod["Título"] == produto:
                        print("Estado Atual:", prod["Estado"])
                        
