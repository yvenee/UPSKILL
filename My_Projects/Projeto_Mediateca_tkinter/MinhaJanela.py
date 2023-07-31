import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from gestao import *
from produto import *
from emprestimo import *

class TipoMediaFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.selected_media_widgets = None  # Variável para controlar os widgets selecionados
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

        elif selected_media_type == "Vídeo":
            self.selected_media_widgets = self.video_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame

        elif selected_media_type == "Áudio":
            self.selected_media_widgets = self.audio_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame


        # Mostra os widgets específicos para o tipo de mídia "Publicação"
    def publicacao_widgets(self, master):        
        frame = tk.Frame(master)

        # Label e Entry para Tipo de Publicação
        label_tipo_pub = tk.Label(frame, text="Tipo de Publicação:")
        entry_tipo_pub = tk.Entry(frame)

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

        # Restante dos widgets para "Publicação"...

        # Posicionamento dos widgets para o grid
        label_tipo_pub.grid(row=0, column=0, padx=10, pady=5)
        entry_tipo_pub.grid(row=0, column=1, padx=10, pady=5)

        label_data_pub.grid(row=1, column=0, padx=10, pady=5)
        calendar_data_pub.grid(row=1, column=1, padx=10, pady=5)

        label_editora.grid(row=2, column=0, padx=10, pady=5)
        entry_editora.grid(row=2, column=1, padx=10, pady=5)

        label_autores.grid(row=3, column=0, padx=10, pady=5)
        entry_autores.grid(row=3, column=1, padx=10, pady=5)

        label_suporte.grid(row=4, column=0, padx=10, pady=5)
        combobox_suporte.grid(row=4, column=1, padx=10, pady=5)

        return frame
    
    # Mostra os widgets específicos para o tipo de media "Vídeo"
    def video_widgets(self, master):        
        frame = tk.Frame(master)

        # Label e Combobox para o Tipo de Vídeo
        label_tipo_video = tk.Label(frame, text="Tipo de Vídeo:")
        combobox_tipo_video = ttk.Combobox(frame, values=["Filme", "Documentário", "Série", "Programa de TV", "Outro"])

        # Label e Entry para Duração
        label_duracao = tk.Label(frame, text="Duração:")
        entry_duracao = tk.Entry(frame)

        # Label e Entry para Atores
        label_atores = tk.Label(frame, text="Editora:")
        entry_atores = tk.Entry(frame)

        # Restante dos widgets para "Vídeo"...

        # Posicionamento dos widgets para o grid
        label_tipo_video.grid(row=0, column=0, padx=10, pady=5)
        combobox_tipo_video.grid(row=0, column=1, padx=10, pady=5)

        label_duracao.grid(row=1, column=0, padx=10, pady=5)
        entry_duracao.grid(row=1, column=1, padx=10, pady=5)

        label_atores.grid(row=2, column=0, padx=10, pady=5)
        entry_atores.grid(row=2, column=1, padx=10, pady=5)

        return frame

    # Mostra os widgets específicos para o tipo de mídia "Áudio"
    def audio_widgets(self, master):
        frame = tk.Frame(master)
        print("Áudio")
        # Restante dos widgets para "Áudio"...
        return frame
        
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
            tipo_pub = self.entry_tipo_pub.get().upper()
            data_pub = self.calendar_data_pub.get_date()
            editora = self.entry_editora.get()
            autores = self.entry_autores.get()
            suporte = self.combobox_suporte.get()   
            publicacao = Publicacao(tipo_pub, data_pub, editora, autores, suporte)
            return publicacao

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

###########################################################################

class MediatecaApp:
    @staticmethod
    def validar_float(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def __init__(self, root):
        self.root = root
        self.root.title("Mediateca Grande")
        self.gestao = Gestao()

        # Create a new frame to hold all the components
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Configuração dos botões
        botao_gestao_produtos = ttk.Button(self.main_frame, text="Gestão de Produtos", command=self.menu_gestao_produtos, style="My.TButton")
        botao_gestao_emprestimos = ttk.Button(self.main_frame, text="Gestão de Empréstimos", command=self.menu_gestao_emprestimos, style="My.TButton")
        botao_relatorios = ttk.Button(self.main_frame, text="Relatórios", command=self.menu_relatorios, style="My.TButton")
        botao_sair = ttk.Button(self.main_frame, text="Sair", command=root.destroy, style="My.TButton")

        # Estilo para os botões
        style = ttk.Style()
        style.configure("My.TButton", font=("Arial", 16))

        # Posicionamento dos botões usando o gerenciador de layout pack
        botao_gestao_produtos.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        botao_gestao_emprestimos.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        botao_relatorios.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        botao_sair.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def menu_gestao_produtos(self):
        # Clear any existing frames within the main frame
        self.clear_frames()

        # Create the product management frame within the main frame
        self.tipo_media_frame = TipoMediaFrame(self.main_frame)
        self.tipo_media_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # # Create the product management frame within the main frame
        # self.product_management_frame = GestaoProdutosFrame(self.main_frame)
        # self.product_management_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def clear_frames(self):
        # Remove all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

    def menu_gestao_emprestimos(self):
        # Implemente a lógica para a gestão de empréstimos aqui
        print("Gestão de Empréstimos selecionada!")

    def menu_relatorios(self):
        # Implemente a lógica para os relatórios aqui
        print("Relatórios selecionados!")


if __name__ == "__main__":
    root = tk.Tk()
    app = MediatecaApp(root)
    root.mainloop()
