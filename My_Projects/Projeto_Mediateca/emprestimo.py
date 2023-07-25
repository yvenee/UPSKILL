from produto import *
import uuid
from datetime import datetime


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