import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk  # Importe o ThemedTk do ttkthemes
from tkinter import Frame, Label
from PIL import Image, ImageTk

from tkcalendar import DateEntry
from datetime import datetime
from gestao import *
from produto import *
from emprestimo import *

class TipoMediaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.selected_media_widgets = None  # Variável para controlar os widgets selecionados
        self.tipo_pub = None
        self.create_widgets()        

    def create_widgets(self):
        # Label e Combobox para o tipo de media
        self.label_tipo_media = tk.Label(self, text="Tipo de Media:")
        self.combobox_tipo_media = ttk.Combobox(self, values=["Publicação", "Vídeo", "Áudio"])        

        # Vincula a função "<<ComboboxSelected>>" ao evento
        self.combobox_tipo_media.bind("<<ComboboxSelected>>", self.on_combobox_selected)

        # Posição dos widgets para o grid
        self.label_tipo_media.grid(row=0, column=0, padx=10, pady=5)
        self.combobox_tipo_media.grid(row=0, column=1, padx=10, pady=5)

        # Frame para exibir os widgets específicos da seleção do usuário
        self.selected_media_frame = tk.Frame(self)
        self.selected_media_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Crie todos os widgets de cada tipo de mídia e oculte-os inicialmente
        self.publicacao_widgets(self.selected_media_frame)
        self.video_widgets(self.selected_media_frame)
        self.audio_widgets(self.selected_media_frame)
        self.hide_all_widgets()
    
    
    # Oculta todos os widgets de mídia
    def hide_all_widgets(self):
        if self.selected_media_widgets is not None:
            self.selected_media_widgets.pack_forget()

    # Esta função será chamada quando o usuário selecionar uma opção no Combobox  
    def on_combobox_selected(self, event):
        selected_media_type = self.combobox_tipo_media.get()
        self.hide_all_widgets()

        if selected_media_type == "Publicação":
            self.selected_media_widgets = self.publicacao_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame
            self.tipo_pub = self.entry_tipo_pub.get()  # Atualiza o valor de self.tipo_pub

        elif selected_media_type == "Vídeo":
            self.selected_media_widgets = self.video_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame

        elif selected_media_type == "Áudio":
            self.selected_media_widgets = self.audio_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame


    # Mostra os widgets específicos para o tipo de mídia "Publicação"
    def publicacao_widgets(self, master):

        frame = tk.Frame(self.selected_media_frame)
        #frame = tk.Frame(master)

        # Label e Entry para Tipo de Publicação
        self.label_tipo_pub = tk.Label(frame, text="Tipo de Publicação:")
        self.entry_tipo_pub = tk.Entry(frame)

        # Label e Calendar para data da publicação
        label_data_pub = tk.Label(frame, text="Data da Publicação:")
        calendar_data_pub = DateEntry(frame, date_pattern='dd/mm/Y')

        # Label e Entry para Editora
        label_editora = tk.Label(frame, text="Editora:")
        entry_editora = tk.Entry(frame)

        # Label e Entry para Autores
        label_autores = tk.Label(frame, text="Autores:")
        entry_autores = tk.Entry(frame)

        # Label e Combobox para o Suporte
        label_suporte = tk.Label(frame, text="Suporte:")
        combobox_suporte = ttk.Combobox(frame, values=["Papel", "Eletrónico"])

        # Posicionamento dos widgets para o grid
        self.label_tipo_pub.grid(row=0, column=0, padx=10, pady=5)
        self.entry_tipo_pub.grid(row=0, column=1, padx=10, pady=5)

        label_data_pub.grid(row=1, column=0, padx=10, pady=5)
        calendar_data_pub.grid(row=1, column=1, padx=10, pady=5)

        label_editora.grid(row=2, column=0, padx=10, pady=5)
        entry_editora.grid(row=2, column=1, padx=10, pady=5)

        label_autores.grid(row=3, column=0, padx=10, pady=5)
        entry_autores.grid(row=3, column=1, padx=10, pady=5)

        label_suporte.grid(row=4, column=0, padx=10, pady=5)
        combobox_suporte.grid(row=4, column=1, padx=10, pady=5)

        self.create_products_widgets(frame)

        return frame
    
    # Mostra os widgets específicos para o tipo de media "Vídeo"
    def video_widgets(self, master):   

        frame = tk.Frame(self.selected_media_frame)
        #frame = tk.Frame(master)

        # Label e Combobox para o Tipo de Vídeo
        label_tipo_video = tk.Label(frame, text="Tipo de Vídeo:")
        combobox_tipo_video = ttk.Combobox(frame, values=["Filme", "Documentário", "Série", "Programa de TV", "Outro"])

        # Label e Entry para Duração
        label_duracao_video = tk.Label(frame, text="Duração:")
        entry_duracao_video = tk.Entry(frame)

        # Label e Entry para Atores
        label_atores = tk.Label(frame, text="Atores:")
        entry_atores = tk.Entry(frame)

        # Posicionamento dos widgets para o grid
        label_tipo_video.grid(row=0, column=0, padx=10, pady=5)
        combobox_tipo_video.grid(row=0, column=1, padx=10, pady=5)

        label_duracao_video.grid(row=1, column=0, padx=10, pady=5)
        entry_duracao_video.grid(row=1, column=1, padx=10, pady=5)

        label_atores.grid(row=2, column=0, padx=10, pady=5)
        entry_atores.grid(row=2, column=1, padx=10, pady=5)

        self.create_products_widgets(frame)

        return frame

    # Mostra os widgets específicos para o tipo de mídia "Áudio"
    def audio_widgets(self, master):

        frame = tk.Frame(self.selected_media_frame)
        
        # Label e Combobox para o Tipo de Áudio
        label_tipo_audio = tk.Label(frame, text="Tipo de Áudio:")
        combobox_tipo_audio = ttk.Combobox(frame, values=["CD", "DVD", "Blu-ray", "K7", "Vinil", "Outro"])

        # Label e Entry para Duração
        label_duracao_audio = tk.Label(frame, text="Duração:")
        entry_duracao_audio = tk.Entry(frame)

        # Label e Entry para Trilhas
        label_trilhas = tk.Label(frame, text="Trilhas:")
        entry_trilhas = tk.Entry(frame)

        # Posicionamento dos widgets para o grid
        label_tipo_audio.grid(row=0, column=0, padx=10, pady=5)
        combobox_tipo_audio.grid(row=0, column=1, padx=10, pady=5)

        label_duracao_audio.grid(row=1, column=0, padx=10, pady=5)
        entry_duracao_audio.grid(row=1, column=1, padx=10, pady=5)

        label_trilhas.grid(row=2, column=0, padx=10, pady=5)
        entry_trilhas.grid(row=2, column=1, padx=10, pady=5)

        self.create_products_widgets(frame)

        return frame

    # Widgets de produto
    def create_products_widgets(self, master):
        # Label e Entry para o título do produto
        self.label_titulo = tk.Label(master, text="Título do Produto:")
        self.entry_titulo = tk.Entry(master)

        # Label e Entry para o preço do produto
        self.label_preco = tk.Label(master, text="Preço €:")
        self.entry_preco = tk.Entry(master)

        # Label e Calendar para data de aquisição
        self.label_data_aquisicao = tk.Label(master, text="Data de Aquisição:")
        self.calendar_data_aquisicao = DateEntry(master, date_pattern='dd/mm/Y')        

        # Label para avisos
        self.label_aviso = tk.Label(master, text="", fg="red")
       
        # Posicionamento dos widgets para o grid
        self.label_titulo.grid(row=6, column=0, padx=10, pady=5)
        self.entry_titulo.grid(row=6, column=1, padx=10, pady=5)

        self.label_preco.grid(row=7, column=0, padx=10, pady=5)
        self.entry_preco.grid(row=7, column=1, padx=10, pady=5)

        self.label_data_aquisicao.grid(row=8, column=0, padx=10, pady=5)
        self.calendar_data_aquisicao.grid(row=8, column=1, padx=10, pady=5)

        self.label_aviso.grid(row=9, column=0, columnspan=2, padx=10, pady=5)  # Usamos columnspan=2 para ocupar 2 colunas

        # Botão para criar o produto
        botao_criar = ttk.Button(master, text="Criar Produto", command=self.criar_produto, style="My.TButton")
        botao_criar.grid(row=10, column=0, columnspan=2, padx=10, pady=10)  # Usamos columnspan=2 para ocupar 2 colunas
        
    
    def verificar_titulo(self):
        titulo = self.entry_titulo.get().upper()
        for produto in self.gestao.produtos:
            if produto["Título"] == titulo:
                self.label_aviso.config(text="O produto já existe!", fg="red")
                return True
        self.label_aviso.config(text="")
        return False

    @staticmethod
    def validar_float(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False

    # Função para criar o produto
    def criar_produto(self):
           
        # Guarda o valores dos inputs nas respetivas variáveis
        titulo = self.entry_titulo.get().upper()
        preco = self.entry_preco.get()
        data_aquisicao = self.calendar_data_aquisicao.get_date()

        if self.verificar_titulo():
            return            

        # Validação do preço para não permitir inserção de um input diferente de um float
        if not self.validar_float(preco):
            self.label_aviso.config(text="Preço inválido. Digite um número válido!", fg="red")
            return
        self.label_aviso.config(text="")
        preco = float(preco)

        # Validação da data para não aceitar inserção de uma data posterior a data atual
        today = datetime.today().date()
        if data_aquisicao > today:
            self.label_aviso.config(text="A data de aquisição não pode ser posterior à data atual!", fg="red")
            return
        self.label_aviso.config(text="")  

         # Acesso ao Input de Tipo de Media 
        tipo_media = self.combobox_tipo_media.get()       

        
        if tipo_media == "Publicação":
            tipo_media = Produto.set_tipo(Produto.tipo[0])
            tipo_pub = self.entry_tipo_pub.get().upper()
            data_pub = self.calendar_data_pub.get_date()
            editora = self.entry_editora.get()
            autores = self.entry_autores.get()
            suporte = self.combobox_suporte.get()   
            publicacao = Publicacao(tipo_pub, data_pub, editora, autores, suporte)
            produto = Produto(tipo_media, publicacao, titulo, preco, data_aquisicao)

            return produto

        
        elif tipo_media == "Vídeo":
            Produto.set_tipo(Produto.tipo[1])
            duracao = self.entry_duracao_video.get()
            tipo = self.combobox_tipo_video.get()            
            atores = self.entry_atores.get().upper()
            suporte = self.combobox_suporte.get()   
            video = Video(duracao, tipo, atores)
            return video

        else:
            Produto.set_tipo(Produto.tipo[2])
            Produto.set_tipo(Produto.tipo[1])
            duracao = self.entry_duracao_audio.get()
            tipo = self.combobox_tipo_audio.get()            
            trilhas = self.entry_trilhas.get().upper()            
            audio = Video(duracao, tipo, trilhas)
            return audio  

        produto = Produto(titulo, preco, data_aquisicao)
        self.gestao.criar_produto(produto)
        self.janela_produtos.destroy() 


  
    
    # Função para criar tipo de media
    def criar_tipo_media(self):

        # Acesso ao Input de Tipo de Media 
        tipo_media = self.combobox_tipo_media.get()       

        
        if tipo_media == "Publicação":
            Produto.set_tipo(Produto.tipo[0])
            tipo_pub = self.entry_tipo_pub.get().upper()
            data_pub = self.calendar_data_pub.get_date()
            editora = self.entry_editora.get()
            autores = self.entry_autores.get()
            suporte = self.combobox_suporte.get()   
            publicacao = Publicacao(tipo_pub, data_pub, editora, autores, suporte)

            return publicacao

        
        elif tipo_media == "Vídeo":
            Produto.set_tipo(Produto.tipo[1])
            duracao = self.entry_duracao_video.get()
            tipo = self.combobox_tipo_video.get()            
            atores = self.entry_atores.get().upper()
            suporte = self.combobox_suporte.get()   
            video = Video(duracao, tipo, atores)
            return video

        else:
            Produto.set_tipo(Produto.tipo[2])
            Produto.set_tipo(Produto.tipo[1])
            duracao = self.entry_duracao_audio.get()
            tipo = self.combobox_tipo_audio.get()            
            trilhas = self.entry_trilhas.get().upper()            
            audio = Video(duracao, tipo, trilhas)
            return audio

#################################################################################        

class GestaoProdutosFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.gestao = Gestao()
        self.create_widgets()

    @staticmethod
    def validar_float(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def create_widgets(self):    
    
        # Label e Entry para o título do produto
        self.label_titulo = tk.Label(self, text="Título do Produto:")
        self.entry_titulo = tk.Entry(self)

        # Label e Entry para o preço do produto
        self.label_preco = tk.Label(self, text="Preço €:")
        self.entry_preco = tk.Entry(self)

        # Label e Calendar para data de aquisição
        self.label_data_aquisicao = tk.Label(self, text="Data de Aquisição:")
        self.calendar_data_aquisicao = DateEntry(self, date_pattern='dd/mm/Y')        

        # Label para avisos
        self.label_aviso = tk.Label(self, text="", fg="red")

        # Botão para criar o produto
        botao_criar = ttk.Button(self, text="Criar Produto", command=self.criar_produto, style="My.TButton")

        # Posição dos widgets para o pack   
        self.label_titulo.pack(side=tk.TOP, padx=10, pady=5)
        self.entry_titulo.pack(side=tk.TOP, padx=10, pady=5)
        self.label_preco.pack(side=tk.TOP, padx=10, pady=5)
        self.entry_preco.pack(side=tk.TOP, padx=10, pady=5)
        self.label_data_aquisicao.pack(side=tk.TOP, padx=10, pady=5)
        self.calendar_data_aquisicao.pack(side=tk.TOP, padx=10, pady=5)               
        self.label_aviso.pack(side=tk.TOP, padx=10, pady=5)
        botao_criar.pack(side=tk.TOP, padx=10, pady=10)

    def verificar_titulo(self):
        titulo = self.entry_titulo.get().upper()
        for produto in self.gestao.produtos:
            if produto["Título"] == titulo:
                self.label_aviso.config(text="O produto já existe!", fg="red")
                return True
        self.label_aviso.config(text="")
        return False

    # Função para criar o produto após verificar os dados
    def criar_produto(self):

        # Inputs   
        titulo = self.entry_titulo.get().upper()
        preco = self.entry_preco.get()
        data_aquisicao = self.calendar_data_aquisicao.get_date()
  

        if self.verificar_titulo():
            return            

        # Validação do preço para não permitir inserção de um input diferente de um float
        if not self.validar_float(preco):
            self.label_aviso.config(text="Preço inválido. Digite um número válido!", fg="red")
            return
        self.label_aviso.config(text="")
        preco = float(preco)

        # Validação da data para não aceitar inserção de uma data posterior a data atual
        today = datetime.today().date()
        if data_aquisicao > today:
            self.label_aviso.config(text="A data de aquisição não pode ser posterior à data atual!", fg="red")
            return
        self.label_aviso.config(text="")
             

        produto = Produto(titulo, preco, data_aquisicao)
        self.gestao.criar_produto(produto)
        self.janela_produtos.destroy()


if __name__ == "__main__":
    app = MediatecaApp()
    app.mainloop()
