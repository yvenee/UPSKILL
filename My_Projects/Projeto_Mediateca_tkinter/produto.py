import uuid
from datetime import datetime


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
