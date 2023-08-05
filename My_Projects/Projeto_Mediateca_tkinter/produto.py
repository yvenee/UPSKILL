import uuid
from datetime import datetime


class Produto:

    estado = ("disponível", "emprestado", "devolvido")
    tipo = ("Publicação", "Vídeo", "Áudio")
    id = 4

    def __init__(self, tipo, media, titulo, preco, data):
        self.__id = Produto.criar_id()
        self.titulo = titulo       
        self.tipo = tipo
        self.tipo_media = None
        Produto.escolher_tipo(self, media)           
        self.data = data
        self.preco = preco
        self.estado = Produto.estado[0]

    def criar_id():
        # if Produto.id != 0:
        Produto.id += 1   
        return str(Produto.id)

    def escolher_tipo(self, media):            

            if self.tipo == "Publicação":            
                
                pub_dict = {
                                "Tipo de Media" : self.tipo,
                                "Tipo de Publicação" : media.tipo_pub,
                                "Data da Publicação" : media.data_pub,
                                "Editora" : media.editora,
                                "Autores" : media.autores,
                                "Suporte" : media.suporte,}
                
                self.tipo_media = pub_dict
            

            elif self.tipo == "Vídeo":
                
                video_dict = {
                            "Tipo de Media" : self.tipo,
                            "Duração" : media.duracao,
                            "Tipo de Vídeo" : media.tipo_video,
                            "Atores" : media.atores,
                                                            }
                self.tipo_media = video_dict

            elif self.tipo == "Áudio":
                
                audio_dict = {
                            "Tipo de Media" : self.tipo,
                            "Duração" : media.duracao,
                            "Suporte" : media.suporte,
                            "Trilhas" : media.trilhas,
                                                            }
                self.tipo_media = audio_dict



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
