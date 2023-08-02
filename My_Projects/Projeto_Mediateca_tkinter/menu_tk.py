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
from produto_tk import *


class MediatecaApp(ThemedTk):
    def __init__(self):
        super().__init__()

        self.set_theme("radiance") # Define o tema da página

        self.title("Mediateca")
        self.minsize(530, 400)  # Define o tamanho mínimo da janela
        self.maxsize(700, 800)  # Define o tamanho máximo da janela igual ao tamanho mínimo
        self.resizable(False, False)  # Impede o redimensionamento da janela

        # Cria uma style para os botões
        style = ttk.Style()
        style.configure("My.TButton", width=80, height=100)

        self.create_frames()

    def create_frames(self):
        self.frame_imagem = FrameImagem(self)
        self.frame_gestao_produtos = FrameGestaoProdutos(self)
        self.frame_gestao_emprestimos = FrameGestaoEmprestimos(self)
        self.frame_relatorios = FrameRelatorios(self)
        self.frame_sair = FrameSair(self)
        self.criar_produto_frame = None


        # Posicione os frames usando o gerenciador de geometria grid
        self.frame_imagem.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.frame_gestao_produtos.grid(row=1, column=0, sticky="nsew")
        self.frame_gestao_emprestimos.grid(row=1, column=1, sticky="nsew")
        self.frame_relatorios.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.frame_sair.grid(row=3, column=0, columnspan=2, sticky="nsew")
        

    def clear_frames(self):
        # Remove all frames except the image frame
        for widget in self.winfo_children():
            if widget != self.frame_imagem:
                widget.grid_forget()


class FrameImagem(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        imagem_path = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/mediateca_img.png"
        imagem = Image.open(imagem_path)
        imagem = imagem.resize((500, 200))  # Redimensione a imagem conforme necessário
        imagem = ImageTk.PhotoImage(imagem)

        # Crie um Label para exibir a imagem
        label_imagem = tk.Label(self, image=imagem)
        label_imagem.image = imagem  # Mantenha uma referência para a imagem
        label_imagem.pack(fill=tk.BOTH, expand=True)


class FrameGestaoProdutos(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Botão "Gestão de Produtos"
        botao_gestao_produtos = ttk.Button(self, text="Gestão de Produtos", command=self.menu_gestao_produtos, style="My.TButton", width=10)
        botao_gestao_produtos.pack(fill=tk.BOTH, padx=5, pady=5)

    def menu_gestao_produtos(self):
        # Limpa a frame atual
        self.master.clear_frames()

        # Create the product management frame within the main window
        self.master.menu_gestao_produtos_frame = MenuGestaoProdutos(self.master)
        self.master.menu_gestao_produtos_frame.grid(row=10, column=0, padx=10, pady=5)


class MenuGestaoProdutos(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Remove any existing widgets
        for widget in self.winfo_children():
            widget.pack_forget()
            
        # Botão "Criar Produtos"
        botao_criar_produtos = ttk.Button(self, text="Criar Produto", command=self.criar_produto, style="My.TButton", width=25)        
        botao_criar_produtos.grid(row=0, column=0, padx=5, pady=5)

        # Botão "Listar Produtos"
        botao_listar_produtos = ttk.Button(self, text="Listar Produtos", command=self.listar_produtos, style="My.TButton", width=25)
        botao_listar_produtos.grid(row=0, column=1, padx=5, pady=5)

        # Botão "Atualizar Produto"
        botao_atualizar_produto = ttk.Button(self, text="Atualizar Produto", command=self.atualizar_produto, style="My.TButton", width=25)
        botao_atualizar_produto.grid(row=1, column=0, padx=5, pady=5)

        # Botão "Eliminar Produto"
        botao_eliminar_produto = ttk.Button(self, text="Eliminar Produto", command=self.eliminar_produto, style="My.TButton", width=25)
        botao_eliminar_produto.grid(row=1, column=1, padx=5, pady=5)

        # Botão "Voltar"
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_principal, style="My.TButton", width=25)
        botao_voltar.grid(row=2, column=0, padx=10, pady=5)

        # Botão "Sair"
        botao_sair = ttk.Button(self, text="Sair", command=self.master.destroy, style="My.TButton", width=25)
        botao_sair.grid(row=2, column=1, padx=10, pady=5)


    def criar_produto(self):

        # Limpa a frame atual e cria uma nova instância de Produto_Frame
        self.master.clear_frames()
        self.master.criar_produto_frame = Criar_Produto_Frame(self.master)
        self.master.criar_produto_frame.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")
 
      
    def listar_produtos(self):
        
        self.master.clear_frames()
        self.master.listar_produtos_frame = Listar_Produtos_Frame(self.master, gestao)
        self.master.listar_produtos_frame.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

    def atualizar_produto(self):
        """ self.master.clear_frames()
        self.master.atualizar_produtos_frame = Atualizar_Produto_Frame(self.master)
        self.master.atualizar_produtos_frame.grid(row=1, column=0, padx=3, pady=3, sticky="nsew") """

    def eliminar_produto(self):
        # Implemente a lógica para a eliminação de produtos aqui
        print("Eliminar Produto selecionado!")

    def voltar_menu_principal(self):
        # Clear the current frame and show the main menu frame
        self.master.clear_frames()
        self.master.frame_imagem.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.master.frame_gestao_produtos.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.master.frame_gestao_emprestimos.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.master.frame_relatorios.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.master.frame_sair.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

class FrameGestaoEmprestimos(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Botão "Gestão de Empréstimos"
        botao_gestao_emprestimos = ttk.Button(self, text="Gestão de Empréstimos", command=self.menu_gestao_emprestimos, style="My.TButton", width=10)
        # botao_gestao_emprestimos.pack(fill=tk.BOTH)
        botao_gestao_emprestimos.pack(fill=tk.BOTH, padx=5, pady=5)

    def menu_gestao_emprestimos(self):
         # Clear any existing frames within the main frame
        self.master.clear_frames()

        # Create the product management frame within the main window
        self.master.menu_gestao_emprestimos_frame = MenuGestaoEmprestimos(self.master)
        self.master.menu_gestao_emprestimos_frame.grid(row=1, column=0, padx=10, pady=5)

class MenuGestaoEmprestimos(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Remove any existing widgets
        for widget in self.winfo_children():
            widget.pack_forget()
            
        # Botão "Criar Emréstimo"
        botao_criar_emprestimo = ttk.Button(self, text="Criar Empréstimo", command=self.criar_emprestimo, style="My.TButton", width=25)        
        botao_criar_emprestimo.grid(row=0, column=0, padx=5, pady=5)

        # Botão "Listar Empréstimos"
        botao_listar_emprestimos = ttk.Button(self, text="Listar Empréstimos", command=self.listar_emprestimos, style="My.TButton", width=25)
        botao_listar_emprestimos.grid(row=0, column=1, padx=5, pady=5)

        # Botão "Atualizar Empréstimos"
        botao_atualizar_emprestimo = ttk.Button(self, text="Atualizar Empréstimo", command=self.atualizar_emprestimo, style="My.TButton", width=25)
        botao_atualizar_emprestimo.grid(row=1, column=0, padx=5, pady=5)

         # Botão "Eliminar Empréstimo"
        botao_eliminar_emprestimo = ttk.Button(self, text="Eliminar Empréstimo", command=self.eliminar_emprestimo, style="My.TButton", width=25)
        botao_eliminar_emprestimo.grid(row=1, column=1, padx=5, pady=5)

        # Botão "Entregar Produto"
        botao_entregar_produto = ttk.Button(self, text="Entregar Produto", command=self.entregar_produto, style="My.TButton", width=58)
        botao_entregar_produto.grid(row=2, column=0, columnspan=2, padx=5, pady=5)     

        # Botão "Voltar"
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_principal, style="My.TButton", width=25)
        botao_voltar.grid(row=3, column=0, padx=10, pady=5)

        # Botão "Sair"
        botao_sair = ttk.Button(self, text="Sair", command=self.master.destroy, style="My.TButton", width=25)
        botao_sair.grid(row=3, column=1, padx=10, pady=5)


    def criar_emprestimo(self):
        # Implemente a lógica para a criação de empréstimo aqui
        print("Criar Empréstimo selecionado!")

    def listar_emprestimos(self):
        # Implemente a lógica para a listagem de empréstimos aqui
        print("Listar Empréstimos selecionado!")

    def atualizar_emprestimo(self):
        # Implemente a lógica para a atualização de empréstimo aqui
        print("Atualizar Empréstimo selecionado!")

    def entregar_produto(self):
        # Implemente a lógica para a entrega de produtos aqui
        print("Entregar Produto selecionado!")

    def eliminar_emprestimo(self):
        # Implemente a lógica para a eliminação de empréstimo aqui
        print("Eliminar Empréstimo selecionado!")

    def voltar_menu_principal(self):
        # Clear the current frame and show the main menu frame
        self.master.clear_frames()
        self.master.frame_imagem.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.master.frame_gestao_produtos.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.master.frame_gestao_emprestimos.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.master.frame_relatorios.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.master.frame_sair.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

class FrameRelatorios(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()
   
    def create_widgets(self):
        botao_relatorios = ttk.Button(self, text="Relatórios", command=self.menu_relatorios, style="My.TButton", width=10)
        # botao_relatorios.pack(fill=tk.BOTH)
        botao_relatorios.pack(fill=tk.BOTH, padx=5, pady=5)

    def menu_relatorios(self):
        # Clear any existing frames within the main frame
        self.master.clear_frames()

        # Create the product management frame within the main window
        self.master.menu_relatorios_frame = MenuRelatorios(self.master)
        self.master.menu_relatorios_frame.grid(row=1, column=0, padx=10, pady=5)

class MenuRelatorios(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Remove any existing widgets
        for widget in self.winfo_children():
            widget.pack_forget()
            
        # Botão "Listar Produtos Multimedia"
        botao_listar_produtos_mult = ttk.Button(self, text="Listar Produtos Multimedia", command=self.listar_produtos_mult, style="My.TButton", width=25)        
        botao_listar_produtos_mult.grid(row=0, column=0, padx=5, pady=5)

        # Botão "Listar Produtos Emprestados"
        botao_listar_produtos_emp = ttk.Button(self, text="Listar Produtos Emprestados", command=self.listar_produtos_emp, style="My.TButton", width=25)
        botao_listar_produtos_emp.grid(row=0, column=1, padx=5, pady=5)

        # Botão "Histórico de Empréstimos"
        botao_historico_emprestimos = ttk.Button(self, text="Histórico de Empréstimos", command=self.historico_emprestimos, style="My.TButton", width=58)
        botao_historico_emprestimos.grid(row=1, column=0, columnspan=2, padx=5, pady=5)      

        # Botão "Voltar"
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_principal, style="My.TButton", width=25)
        botao_voltar.grid(row=3, column=0, padx=10, pady=5)

        # Botão "Sair"
        botao_sair = ttk.Button(self, text="Sair", command=self.master.destroy, style="My.TButton", width=25)
        botao_sair.grid(row=3, column=1, padx=10, pady=5)        


    def listar_produtos_mult(self):
        # Implemente a lógica para a listar produtos multimedia aqui
        print("Listar Produtos Multimedia selecionado!")

    def listar_produtos_emp(self):
        # Implemente a lógica para a listagem de Produtos Emprestados aqui
        print("Listar Produtos Emprestados selecionado!")

    def historico_emprestimos(self):
        # Implemente a lógica para o Histórico de Empréstimos aqui
        print("Histórico de Empréstimos selecionado!")

    def voltar_menu_principal(self):
            # Clear the current frame and show the main menu frame
            self.master.clear_frames()
            self.master.frame_imagem.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
            self.master.frame_gestao_produtos.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
            self.master.frame_gestao_emprestimos.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
            self.master.frame_relatorios.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
            self.master.frame_sair.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    

class FrameSair(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        botao_sair = ttk.Button(self, text="Sair", command=self.master.destroy, style="My.TButton", width=20)
        # botao_sair.pack(fill=tk.BOTH, padx=3, pady=3)
        botao_sair.pack(fill=tk.BOTH, padx=5, pady=5)


if __name__ == "__main__":
    app = MediatecaApp()
    app.mainloop()
