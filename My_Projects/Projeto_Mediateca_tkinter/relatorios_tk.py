import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk  # Importe o ThemedTk do ttkthemes
from tkinter import Frame, Label
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime

from produto import *
from emprestimo import *
from gestao import *
from produto_tk import *

def show_custom_messagebox(title, message, width, height, img):
    top = tk.Toplevel()
    top.title(title)
    top.geometry(f"{width}x{height}")
    top.resizable(False, False)

    image_path = img  # Substitua pelo caminho da imagem que você deseja exibir
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Redimensione a imagem conforme necessário
    photo = ImageTk.PhotoImage(image)

    label_image = tk.Label(top, image=photo)
    label_image.image = photo
    label_image.pack(padx=10, pady=30)

    label_message = tk.Label(top, text=message, wraplength=width - 20)
    label_message.pack(padx=10, pady=5)

    ok_button = ttk.Button(top, text="OK", command=top.destroy)
    ok_button.pack(pady=5)


class Listar_Produtos_Mult_Frame(tk.Frame):
    def __init__(self, master, gestao, **kwargs):
        super().__init__(master, **kwargs)

        self.gestao = gestao
        self.create_widgets()
    
    def create_widgets(self):
        
        # Dropdown para selecionar a ordenação
        opcoes_ordenacao = ["Alfabética Crescente", "Alfabética Decrescente",  "Data de Aquisição Crescente", "Data de Aquisição Decrescente", "Preço Crescente", "Preço Decrescente", "Estado", "Tipo de Media"]
        self.var_ordenacao = tk.StringVar(value=opcoes_ordenacao[0])
        dropdown_ordenacao = ttk.OptionMenu(self, self.var_ordenacao, *opcoes_ordenacao, command=self.on_dropdown_change)
        dropdown_ordenacao.grid(row=1, column=1, padx=10, pady=10)

        dropdown_ordenacao_label = tk.Label(self, text="Tipo de Ordenação")
        dropdown_ordenacao_label.grid(row=1, column=0, padx=10, pady=10)

        # Treeview para exibir os produtos
        columns = ("ID", "Título", "Preço", "Data de Aquisição", "Tipo de Media", "Estado")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Definir o cabeçalho das colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Data de Aquisição", text="Data de Aquisição")
        self.tree.heading("Tipo de Media", text="Tipo de Media")
        self.tree.heading("Estado", text="Estado")

        # Definir a largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Título", width=200)
        self.tree.column("Preço", width=100)
        self.tree.column("Data de Aquisição", width=150)
        self.tree.column("Tipo de Media", width=100)
        self.tree.column("Estado", width=100)

        # Adicionar o widget ttk.Treeview à janela
        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Chamar a função para preencher a treeview com os produtos existentes em ordem alfabética por padrão
        self.populate_treeview_ordenado_por("Título")

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=2, sticky='ns')       
        
        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.grid(row=4, column=0, columnspan=3, padx=10, pady=5) 

    
    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.clear_frames()
        self.master.create_frames()

    def on_dropdown_change(self, selected_option):

        if selected_option == "Ordem Alfabética":
            self.populate_treeview_ordenado_por("Título")
        elif selected_option == "Alfabética Crescente":
            self.populate_treeview_ordenado_por("Título", reverse=True)
        elif selected_option == "Alfabética Decrescente":
            self.populate_treeview_ordenado_por("Título", reverse=False)
        elif selected_option == "Data de Aquisição Crescente":
            self.populate_treeview_ordenado_por("Data_Aquisição", reverse=False)
        elif selected_option == "Data de Aquisição Decrescente":
            self.populate_treeview_ordenado_por("Data_Aquisição", reverse=True)
        elif selected_option == "Preço Crescente":
            self.populate_treeview_ordenado_por("Preço", reverse=False)
        elif selected_option == "Preço Decrescente":
            self.populate_treeview_ordenado_por("Preço", reverse=True)
        elif selected_option == "Estado":
            self.populate_treeview_ordenado_por("Estado", reverse=True)
        elif selected_option == "Tipo de Media":
            self.populate_treeview_ordenado_por("Tipo", reverse=True)
        else:
             self.populate_treeview_ordenado_por("Título")
    
    def populate_treeview_ordenado_por(self, campo_ordem, reverse=True):

        # Limpar os itens existentes no treeview (caso já tenha algum)
        self.tree.delete(*self.tree.get_children())

        # Obter a lista de produtos da gestão
        produtos = self.gestao.produtos

        # Ordenar os produtos com base no campo de ordem
        produtos_ordenados = sorted(produtos, key=lambda p: p[campo_ordem], reverse=reverse)

        # Adicionar os produtos ao treeview
        for produto in produtos_ordenados:
            id = produto["ID"]
            titulo = produto["Título"]
            preco = f"€ {produto['Preço']:.2f}"
            data_aquisicao = produto["Data_Aquisição"].strftime("%d/%m/%Y")
            tipo_midia = produto["Tipo"]
            estado = produto["Estado"]
            self.tree.insert("", "end", values=(id, titulo, preco, data_aquisicao, tipo_midia, estado))

       
class Listar_Produtos_Estado_Frame(tk.Frame):
    def __init__(self, master, gestao, **kwargs):
        super().__init__(master, **kwargs)

        self.gestao = gestao
        self.create_widgets()
    
    def create_widgets(self):
        # Dropdown para selecionar a ordenação
        opcoes_ordenacao = ["Disponível", "Disponível", "Emprestado"]
        self.var_ordenacao = tk.StringVar(value=opcoes_ordenacao[1])
        dropdown_ordenacao = ttk.OptionMenu(self, self.var_ordenacao, *opcoes_ordenacao, command=self.on_dropdown_change)
        dropdown_ordenacao.grid(row=1, column=1, padx=10, pady=10)

        dropdown_ordenacao_label = tk.Label(self, text="Estado")
        dropdown_ordenacao_label.grid(row=1, column=0, padx=10, pady=10)

        # Treeview para exibir os produtos
        columns = ("ID", "Título", "Preço", "Data de Aquisição", "Tipo de Media", "Estado")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Definir o cabeçalho das colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Data de Aquisição", text="Data de Aquisição")
        self.tree.heading("Tipo de Media", text="Tipo de Media")
        self.tree.heading("Estado", text="Estado")

        # Definir a largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Título", width=200)
        self.tree.column("Preço", width=100)
        self.tree.column("Data de Aquisição", width=150)
        self.tree.column("Tipo de Media", width=100)
        self.tree.column("Estado", width=100)

        # Adicionar o widget ttk.Treeview à janela
        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Chamar a função para preencher a treeview com os produtos existentes em ordem alfabética por padrão
        self.on_dropdown_change("Disponível")

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=2, sticky='ns')       
        
        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.grid(row=4, column=0, columnspan=3, padx=10, pady=5) 

        
    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.clear_frames()
        self.master.create_frames()

    def on_dropdown_change(self, selected_option):
        
        # Limpar os itens existentes no treeview (caso já tenha algum)
        self.tree.delete(*self.tree.get_children())

        if selected_option == "Disponível":
            # Ordenar e selecionar apenas os produtos com estado "emprestado"
            produtos_ordenados = [produto for produto in self.gestao.produtos if produto["Estado"] == "disponível"]
            produtos_ordenados = sorted(produtos_ordenados, key=lambda x: x["ID"])     
            # Adicionar os produtos ao treeview
            for produto in produtos_ordenados:
                id = produto["ID"]
                titulo = produto["Título"]
                preco = f"€ {produto['Preço']:.2f}"
                data_aquisicao = produto["Data_Aquisição"].strftime("%d/%m/%Y")
                tipo_midia = produto["Tipo"]
                estado = produto["Estado"]
                self.tree.insert("", "end", values=(id, titulo, preco, data_aquisicao, tipo_midia, estado))
                
        elif selected_option == "Emprestado":
            # Ordenar e selecionar apenas os produtos com estado "emprestado"
            produtos_ordenados = [produto for produto in self.gestao.produtos if produto["Estado"] == "emprestado"]
            produtos_ordenados = sorted(produtos_ordenados, key=lambda x: x["ID"])
            # Adicionar os produtos ao treeview
            for produto in produtos_ordenados:
                id = produto["ID"]
                titulo = produto["Título"]
                preco = f"€ {produto['Preço']:.2f}"
                data_aquisicao = produto["Data_Aquisição"].strftime("%d/%m/%Y")
                tipo_midia = produto["Tipo"]
                estado = produto["Estado"]
                self.tree.insert("", "end", values=(id, titulo, preco, data_aquisicao, tipo_midia, estado))
       
class Historico_Emprestimos_Frame(tk.Frame):
    def __init__(self, master, gestao, **kwargs):
        super().__init__(master, **kwargs)

        self.gestao = gestao
        self.create_widgets()
    
    def create_widgets(self):      

        # Obter os produtos com empréstimos
        produtos_com_emprestimo = self.get_produtos_com_emprestimo()

        # Dropdown dos produtos com empréstimo
        lbl_titulo = ttk.Label(self, text="Título do Produto:")
        lbl_titulo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.combobox_titulo = ttk.Combobox(self, values=produtos_com_emprestimo, state="readonly")
        self.combobox_titulo.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")       

        # Treeview para exibir os produtos
        columns = ("ID", "Título", "Tipo de Media", "Nome", "Data Empréstimo", "Data Devolução", "Estado")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Definir o cabeçalho das colunas
        self.tree.heading("ID", text="ID Empréstimo")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Tipo de Media", text="Tipo de Media")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Data Empréstimo", text="Data Empréstimo")
        self.tree.heading("Data Devolução", text="Data Devolução")
        self.tree.heading("Estado", text="Estado")

        # Definir a largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Título", width=200)
        self.tree.column("Tipo de Media", width=100)
        self.tree.column("Nome", width=100)
        self.tree.column("Data Empréstimo", width=150)
        self.tree.column("Data Devolução", width=150)
        self.tree.column("Estado", width=100)

        # Adicionar o widget ttk.Treeview à janela
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configurar a coluna e a linha para se expandirem corretamente
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Chamar a função para preencher o treeview com os produtos existentes
        #self.populate_treeview()

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky='ns')  

        # Label e Entry para inserir o Título do Produto
        """  lbl_titulo = ttk.Label(self, text="Título do Produto:")
        lbl_titulo.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.entry_titulo = ttk.Entry(self)
        self.entry_titulo.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")   """

        # Botão "Mostrar Histórico" para buscar e mostrar o histórico do produto
        self.mostrar_historico_button = tk.Button(self, text="Mostrar Histórico", command=self.mostrar_historico)
        self.mostrar_historico_button.grid(row=2, column=1,  padx=10, pady=10, sticky="nsew")   
        
        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.grid(row=4, column=0, columnspan=3, padx=10, pady=5) 

        
    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.clear_frames()
        self.master.create_frames()

    def get_produtos_com_emprestimo(self):
        # Obter a lista de produtos com empréstimo da gestão
        emprestimos = self.gestao.emprestimos
        produtos_com_emprestimo = set(emprestimo["Produto"]["Título"] for emprestimo in emprestimos)
        return sorted(produtos_com_emprestimo)

    def mostrar_historico(self):

        titulo = self.combobox_titulo.get()  # Obter o título selecionado no dropdown
        self.populate_treeview(titulo)       # Chamar a função de preencher a treeview com o título selecionado

    def populate_treeview(self, titulo):
        # Limpar os itens existentes no treeview (caso já tenha algum)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obter a lista de produtos da gestão
        emprestimos = self.gestao.emprestimos

        # Exibir na treeview o histórico de empréstimos do produto pesquisado
        for emprestimo in emprestimos:
            if emprestimo["Produto"]["Título"].upper() == titulo.upper():
                id = emprestimo["Empréstimo_ID"]
                titulo = emprestimo["Produto"]["Título"]
                tipo_midia = emprestimo["Produto"]["Tipo"]
                nome = emprestimo['Nome']
                data_emp = emprestimo["Data_emp"].strftime("%d/%m/%Y")
                data_devol = emprestimo["Data_devol"].strftime("%d/%m/%Y")                
                estado = emprestimo["Estado_emp"]

                self.tree.insert("", "end", text=emprestimo["Produto"]["Título"], values=(id, titulo, tipo_midia, nome, data_emp, data_devol, estado))
