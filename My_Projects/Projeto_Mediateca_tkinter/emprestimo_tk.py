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


class Produtos_Disponiveis_Frame(tk.Frame):
    def __init__(self, master, gestao):
        super().__init__(master)
       
        self.gestao = gestao
        self.create_widgets()

    def create_widgets(self):
        
        # Criar o widget ttk.Treeview
        columns = ("ID", "Título", "Preço", "Data de Aquisição", "Tipo de Media", "Estado")
        self.tree_disponiveis = ttk.Treeview(self, columns=columns, show='headings')

        # Definir o cabeçalho das colunas
        self.tree_disponiveis.heading("ID", text="ID")
        self.tree_disponiveis.heading("Título", text="Título")
        self.tree_disponiveis.heading("Preço", text="Preço")
        self.tree_disponiveis.heading("Data de Aquisição", text="Data de Aquisição")
        self.tree_disponiveis.heading("Tipo de Media", text="Tipo de Media")
        self.tree_disponiveis.heading("Estado", text="Estado")
        
        # Definir a largura das colunas
        self.tree_disponiveis.column("ID", width=50)
        self.tree_disponiveis.column("Título", width=200)
        self.tree_disponiveis.column("Preço", width=100)
        self.tree_disponiveis.column("Data de Aquisição", width=100)
        self.tree_disponiveis.column("Tipo de Media", width=100)
        self.tree_disponiveis.column("Estado", width=100)    

        self.tree_disponiveis.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew") 

        # Configurar a coluna e a linha para se expandirem corretamente
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Chamar a função para preencher o treeview com os produtos existentes
        self.populate_treeview()

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree_disponiveis.yview)
        self.tree_disponiveis.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')       
        
        # Botão para chamar a Frame de Criar Empréstimo
        botao_criar_emprestimo_frame = ttk.Button(self, text="Criar Empréstimo", command=self.criar_emprestimo_frame)
        botao_criar_emprestimo_frame.grid(row=3, column=0, padx=10, pady=5)

        
        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.grid(row=4, column=0, columnspan=3, padx=10, pady=5)        


    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.clear_frames()
        self.master.create_frames()

    def populate_treeview(self):
        # Limpar os itens existentes no treeview (caso já tenha algum)
        for item in self.tree_disponiveis.get_children():
            self.tree_disponiveis.delete(item)
        
        # Obter a lista de produtos da gestão
        produtos = self.gestao.produtos

        # Adicionar os produtos ao treeview
        for produto in produtos:
            if produto["Estado"] == "disponível":
                id = produto["ID"]
                titulo = produto["Título"]
                estado = produto["Estado"]
                preco = f"€ {produto['Preço']:.2f}"
                data_aquisicao = produto["Data_Aquisição"].strftime("%d/%m/%Y")
                tipo_midia = produto["Tipo"]
                self.tree_disponiveis.insert("", "end", values=(id, titulo, preco, data_aquisicao, tipo_midia, estado))

    def criar_emprestimo_frame(self):
        selected_item = self.tree_disponiveis.focus()

        if not selected_item:
            messagebox.showwarning("Nenhum Produto Selecionado", "Por favor, selecione um produto para criar o empréstimo.")
            return

        # Obter o ID do produto selecionado
        produto_id = self.tree_disponiveis.item(selected_item, "values")[0]
        data_aquisicao = self.tree_disponiveis.item(selected_item, "values")[3]

        # Limpa a frame atual e cria uma nova instância de Produto_Frame
        self.master.clear_frames()
        self.master.criar_emprestimo_frame = Criar_Emprestimo_Frame(self.master, self.gestao, produto_id, data_aquisicao)
        self.master.criar_emprestimo_frame.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")


class Criar_Emprestimo_Frame(tk.Frame):
    def __init__(self, master, gestao, produto_id, data_aquisicao):
        super().__init__(master)

        self.gestao = gestao
        self.produto_id = produto_id
        self.data_aquisicao = data_aquisicao
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para inserir o nome do usuário
        lbl_nome_usuario = ttk.Label(self, text="Nome do Usuário:")
        lbl_nome_usuario.pack(pady=10)

        self.entry_nome_usuario = ttk.Entry(self)
        self.entry_nome_usuario.pack(pady=5)

        # Label e Entry para inserir a data do empréstimo
        lbl_data_emprestimo = ttk.Label(self, text="Data do Empréstimo:")
        lbl_data_emprestimo.pack(pady=10)

        self.entry_data_emprestimo = DateEntry(self, date_pattern='dd/mm/Y')
        self.entry_data_emprestimo.pack(pady=5)

        # Label e Entry para inserir a data de devolução
        lbl_data_devolucao = ttk.Label(self, text="Data de Devolução:")
        lbl_data_devolucao.pack(pady=10)

        self.entry_data_devolucao =DateEntry(self, date_pattern='dd/mm/Y')
        self.entry_data_devolucao.pack(pady=5)
        
        # Label para avisos
        self.label_aviso = tk.Label(self, text="", fg="red")
        self.label_aviso.pack(pady=10)
        
        # Botão para confirmar o empréstimo
        btn_confirmar_emprestimo = ttk.Button(self, text="Confirmar Empréstimo", command=self.confirmar_emprestimo)
        btn_confirmar_emprestimo.pack(pady=20)

        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.pack(pady=20)

    def confirmar_emprestimo(self):
        # Obter as informações do empréstimo inseridas pelo usuário
        nome_usuario = self.entry_nome_usuario.get().upper()
        data_emprestimo = self.entry_data_emprestimo.get_date()
        data_devolucao = self.entry_data_devolucao.get_date()
        data_aquisicao = datetime.strptime(self.data_aquisicao, "%d/%m/%Y").date()

        # Validação do nome do usuário
        if not nome_usuario:
            self.label_aviso.config(text="Insira o nome!", fg="red")
            return
        self.label_aviso.config(text="")

        # Validação da data para não aceitar inserção de uma data de emprestimo anterior à data de aquisicao do produto
        if data_emprestimo < data_aquisicao:
            self.label_aviso.config(text="A data do empréstimo não pode ser inferior à data de aquisição do produto!", fg="red")
            return
        self.label_aviso.config(text="")

        # Validação da data para não aceitar inserção de uma data de devolução anterior à data do empréstimo
        if data_emprestimo > data_devolucao:
            self.label_aviso.config(text="A data de devolução do empréstimo não pode ser inferior à data do empréstimo!", fg="red")
            return
        self.label_aviso.config(text="")

        # Validação da data para não aceitar inserção de uma data posterior a data atual
        today = datetime.today().date()
        if data_emprestimo > today:
            self.label_aviso.config(text="A data do empréstimo não pode ser posterior à data atual!", fg="red")
            return
        self.label_aviso.config(text="")     

        # Cria o objeto empréstimo
        emprestimo = Emprestimo(nome_usuario, data_emprestimo, data_devolucao)
        gestao.criar_emprestimo(emprestimo, self.produto_id)

        # Fechar a janela de diálogo
        self.destroy()

        # Exibir uma mensagem de sucesso
        title = "Empréstimo Criado"
        message = "O empréstimo foi criado com sucesso!"
        img =  "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/success_icon.png"
        show_custom_messagebox(title, message, 350, 350, img)

        # Atualizar as frames para refletir o novo estado
        self.master.create_frames()


    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.clear_frames()
        self.master.create_frames()



class Gerir_Emprestimos_Frame(tk.Frame):
    def __init__(self, master, gestao, **kwargs):
        super().__init__(master, **kwargs)

        self.gestao = gestao
        self.create_widgets()
    
    def create_widgets(self):
        # Criar o widget ttk.Treeview
        columns = ("ID",  "Nome",  "Título", "Data Empréstimo", "Data Devolução", "Tipo de Media", "Estado")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Definir o cabeçalho das colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Data Empréstimo", text="Data do Empréstimo")
        self.tree.heading("Data Devolução", text="Data da Devolução")
        self.tree.heading("Tipo de Media", text="Tipo de Media")
        self.tree.heading("Estado", text="Estado")

        # Definir a largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=50)
        self.tree.column("Título", width=150)
        self.tree.column("Data Empréstimo", width=100)
        self.tree.column("Data Devolução", width=100)
        self.tree.column("Tipo de Media", width=100)
        self.tree.column("Estado", width=100)

        # Adicionar o widget ttk.Treeview à janela
        self.tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew") 

        # Configurar a coluna e a linha para se expandirem corretamente
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Chamar a função para preencher o treeview com os produtos existentes
        self.populate_treeview()

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky='ns') 

        # # Label para avisos
        self.label_aviso = tk.Label(self, text="", fg="red")
        self.label_aviso.grid(row=2, column=0, sticky='ns') 

        # Botão "Mais Detalhes"
        botao_mais_detalhes = ttk.Button(self, text="Mais Detalhes", command=self.ver_mais_detalhes)
        botao_mais_detalhes.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

         # Botão "Devolver Produto"
        botao_devolver_produto = ttk.Button(self, text="Devolver Produto", command=self.devolver_produto)
        botao_devolver_produto.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Botão "Atualizar"
        botao_atualizar = ttk.Button(self, text="Atualizar", command=self.atualizar_emprestimo)
        botao_atualizar.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        # Botão "Excluir"
        botao_excluir = ttk.Button(self, text="Excluir", command=self.excluir_emprestimo)
        botao_excluir.grid(row=6, column=0, padx=5, pady=5, sticky="ew")     

        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.grid(row=7, column=0, padx=5, pady=5, sticky="ew")      
        #botao_voltar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)      


    def populate_treeview(self):
        # Limpar os itens existentes no treeview (caso já tenha algum)
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obter a lista de produtos da gestão
        emprestimos = self.gestao.emprestimos

        # Adicionar os produtos ao treeview
        for emprestimo in emprestimos:
            id = emprestimo["Empréstimo_ID"]
            nome = emprestimo["Nome"]
            titulo = emprestimo["Produto"]["Título"]             
            data_emp = emprestimo["Data_emp"].strftime("%d/%m/%Y")
            data_devol = emprestimo["Data_devol"].strftime("%d/%m/%Y")
            tipo_midia = emprestimo["Produto"]["Tipo"]
            estado = emprestimo["Estado_emp"]
            self.tree.insert("", "end", values=(id, nome, titulo, data_emp, data_devol, tipo_midia, estado))


    def ver_mais_detalhes(self):

        # Obter o item selecionado na treeview
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Nenhum Produto Selecionado", "Por favor, selecione um produto.")
            return  # Nenhum item selecionado, não fazer nada

        # Obter os valores da linha selecionada
        item_values = self.tree.item(selected_item)["values"]

        # Obter o ID do tipo de mídia da linha selecionada
        emprestimo_id = item_values[0] # O índice 0 corresponde à coluna "ID"

        # Buscar as informações completas do tipo de mídia usando o ID
        emprestimo_info = self.gestao.obter_emprestimos(emprestimo_id)
        
     
        if not emprestimo_info:
            return  # Tipo de mídia não encontrado, não fazer nada     
       
        message = f"Produto_ID: {emprestimo_info['Produto_ID']}\n"


        if emprestimo_info['Produto']["Tipo"] == "Publicação":
         
            message += f"Tipo de Publicação: {emprestimo_info['Produto']['Media']['Tipo de Publicação']}\n"
            message += f"Data da Publicação: {emprestimo_info['Produto']['Media']['Data da Publicação']}\n"
            message += f"Editora: {emprestimo_info['Produto']['Media']['Editora']}\n"
            message += f"Autores: {emprestimo_info['Produto']['Media']['Autores']}\n"
            message += f"Suporte: {emprestimo_info['Produto']['Media']['Suporte']}\n" 
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/publication_icon.png"       
            
            show_custom_messagebox("Mais Detalhes", message, 300, 350, img)

        elif emprestimo_info['Produto']["Tipo"] == "Vídeo":   

            message += f"Tipo de Vídeo: {emprestimo_info['Produto']['Media']['Tipo de Vídeo']}\n"
            message += f"Duração: {emprestimo_info['Produto']['Media']['Duração']}\n"
            message += f"Atores: {emprestimo_info['Produto']['Media']['Atores']}\n"
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/video_icon.png"   
            
            
            show_custom_messagebox("Mais Detalhes", message, 300, 350, img)


        elif emprestimo_info['Produto']["Tipo"] =="Áudio":

            message += f"Tipo de Áudio: {emprestimo_info['Produto']['Media']['Suporte']}\n"
            message += f"Duração: {emprestimo_info['Produto']['Media']['Duração']}\n"
            message += f"Trilhas: {emprestimo_info['Produto']['Media']['Trilhas']}\n"
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/audio_icon.png"   

            show_custom_messagebox("Mais Detalhes", message, 300, 350, img)



    def atualizar_emprestimo(self):

        # Obter o item selecionado na treeview
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Nenhum Produto Selecionado", "Por favor, selecione um produto.")
            return  # Nenhum item selecionado, não fazer nada

        # Obter os valores da linha selecionada
        values = self.tree.item(selected_item)["values"]

        # Obter o ID do tipo de mídia da linha selecionada
        emprestimo_id = values[0] # O índice 0 corresponde à coluna "ID"

        # Buscar as informações completas do tipo de mídia usando o ID
        emprestimo_info = self.gestao.obter_emprestimos(emprestimo_id)
        
     
        if not emprestimo_info:
            return  # Emprestimo não encontrado, não fazer nada     
       
        produto_id = emprestimo_info['Produto_ID']
        data_aquisicao = emprestimo_info['Produto']['Data_Aquisição']

       
        # Cria o novo frame para a página de atualizar empréstimo
        self.atualizar_emprestimo_frame = Criar_Emprestimo_Frame(self.master, gestao, produto_id, data_aquisicao)  # Passa o self.master como parâmetro
        self.atualizar_emprestimo_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Preenche os campos com as informações do empréstimo selecionado
        self.atualizar_emprestimo_frame.entry_nome_usuario.insert(0, values[1])
        self.atualizar_emprestimo_frame.entry_data_emprestimo.set_date(values[3])
        self.atualizar_emprestimo_frame.entry_data_devolucao.set_date(values[4])

        # Botão "Atualizar Emprestimo" para executar a atualização       
        botao_atualizar_emprestimo = ttk.Button(
            self.atualizar_emprestimo_frame,
            text="Atualizar Empréstimo",
            command=lambda: self.atualizar_emprestimo_info(emprestimo_id, self.atualizar_emprestimo_frame, data_aquisicao),
            style="My.TButton",
            width=68
        )
        botao_atualizar_emprestimo.pack()
        #botao_atualizar_emprestimo.grid(row=10, column=0, columnspan=2, padx=10, pady=3)



    def atualizar_emprestimo_info(self, item_id, frame, data_aquisicao):

        # Obtem os valores dos campos de entrada
        nome_usuario = frame.entry_nome_usuario.get().upper()
        data_emprestimo = frame.entry_data_emprestimo.get_date()
        data_devolucao = frame.entry_data_devolucao.get_date()
        
        # Validação do nome do usuário
        if not nome_usuario:
            self.label_aviso.config(text="Insira o nome!", fg="red")
            return
        self.label_aviso.config(text="")

        # Validação da data para não aceitar inserção de uma data de emprestimo anterior à data de aquisicao do produto
        if data_emprestimo < data_aquisicao:
            self.label_aviso.config(text="A data do empréstimo não pode ser inferior à data de aquisição do produto!", fg="red")
            return
        self.label_aviso.config(text="")

        # Validação da data para não aceitar inserção de uma data de devolução anterior à data do empréstimo
        if data_emprestimo > data_devolucao:
            self.label_aviso.config(text="A data de devolução do empréstimo não pode ser inferior à data do empréstimo!", fg="red")
            return
        self.label_aviso.config(text="")

        # Validação da data para não aceitar inserção de uma data posterior a data atual
        today = datetime.today().date()
        if data_emprestimo > today:
            self.label_aviso.config(text="A data do empréstimo não pode ser posterior à data atual!", fg="red")
            return
        self.label_aviso.config(text="")     

        # Atualizar informações do emprestimo    
        emprestimo = self.gestao.obter_emprestimos(item_id)
    
        if emprestimo is None:
            messagebox.showerror("Empréstimo não encontrado", "O empréstimo selecionado não foi encontrado na lista.")

        else:            
        
            emprestimo['Nome'] = nome_usuario
            emprestimo['Data_emp'] = data_emprestimo
            emprestimo['Data_devol']= data_devolucao
           
            # Exibir mensagem de sucesso
            title = "Atualização de Empréstimo"
            message = "Empréstimo atualizado com sucesso!"
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/success_icon.png" 
            show_custom_messagebox(title, message, 350, 350, img)

            # Retornar ao menu anterior
            # self.master.clear_frames()
            # self.master.create_frames()

    
    def devolver_produto(self):  

        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Nenhum Empréstimo Selecionado", "Por favor, selecione um empréstimo para devolver o produto.")
            return

        # Obter dados da tree
        emprestimo_id = self.tree.item(selected_item, "values")[0]        
        data_emprestimo = datetime.strptime(self.tree.item(selected_item, "values")[3], "%d/%m/%Y").date()
        estado = self.tree.item(selected_item, "values")[6]

        # Atualizar informações do emprestimo    
        emprestimo = self.gestao.obter_emprestimos(emprestimo_id)
        produto_id = emprestimo["Produto_ID"]
      

        def confirmar_devolucao():

            data_devolucao = entry_data_devolucao.get_date()
                
            emprestimos = self.gestao.emprestimos
            produtos = self.gestao.produtos

            if data_devolucao < data_emprestimo or data_devolucao > datetime.now().date():
                self.label_aviso.config(text="A data de devolução do empréstimo não pode ser anterior à data do empréstimo ou superior à data de hoje!", fg="red")
                return

            if estado == "Emprestado":
                # Atualizar o estado e data de devolução na lista de empréstimos
                for emp in emprestimos:
                    if str(emp["Empréstimo_ID"]) == str(emprestimo_id):
                        emp["Estado_emp"] = "Devolvido"
                        emp["Produto"]["Estado"] = "Devolvido"
                        emp["Data_devol"] = data_devolucao
                        # Atualizar o estado na lista de produtos        
                        for prod in produtos:
                            if str(prod["ID"]) == str(produto_id):
                                prod["Estado"] = "disponível"
                        #emprest = Emprestimo(emp["Nome"], emp["Data_emp"], data_devolucao)
                        emprestimo_devolvido = {
                            "Produto_ID": emp["Produto_ID"],
                            "Título": emp["Produto"]["Título"],
                            "Estado_prod": emp["Produto"]["Estado"],
                            #"Devolução_ID": emprest.get_id(),
                            "Nome": emp["Nome"],
                            "Data_emp": emp["Data_emp"],
                            "Data_devol": data_devolucao,
                            "Estado_emp": emp["Estado_emp"]
                        }       
                        self.gestao.historico_emprestimos.append(emprestimo_devolvido)
                
                # Exibir mensagem de sucesso
                title = "Produto Devolvido"
                message = "Produto devolvido com sucesso!"
                img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/success_icon.png" 
                show_custom_messagebox(title, message, 350, 350, img)
            
            else:
                # Exibir mensagem de sucesso
                title = "Produto Devolvido"
                message = "Não é possível devolver o produto"
                img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/success_icon.png" 
                show_custom_messagebox(title, message, 350, 350, img)
                
    
            # Fechar a janela de devolução
            top.destroy()

            # Atualizar a exibição do treeview com os empréstimos
            self.populate_treeview()

        top = tk.Toplevel()
        top.title("Devolução do Produto")
        top.geometry("300x150")

        # Label e Entry para inserir a data de devolução
        lbl_data_devolucao = tk.Label(top, text="Nova Data de Devolução:")
        lbl_data_devolucao.pack(pady=10)

        entry_data_devolucao = DateEntry(top, date_pattern='dd/mm/Y')
        entry_data_devolucao.pack(pady=5)

        # Botão para confirmar a devolução
        btn_confirmar_devolucao = tk.Button(top, text="Confirmar Devolução", command=confirmar_devolucao)
        btn_confirmar_devolucao.pack(pady=20)


    def excluir_emprestimo(self):
        # Obter o item selecionado na treeview
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Nenhum Produto Selecionado", "Por favor, selecione um produto para excluir.")
            return  # Nenhum item selecionado, não fazer nada

        # Obter o ID do emprestimo selecionado
        emprestimo_id = self.tree.item(selected_item, "values")[0]

        # Excluir o produto da gestao.emprestimo usando o ID
        for emprestimo in self.gestao.emprestimos:           
           
            if str(emprestimo["Empréstimo_ID"]) == str(emprestimo_id):
                if emprestimo["Estado_emp"] == "Devolvido":
                    message = "Não é possível excluir um empréstimo já devolvido!"
                    img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/error_icon.png" 
                    show_custom_messagebox("Produto", message, 300, 300, img)                 
                    return
                    
                else: 
                    for produto in self.gestao.produtos:
                        if produto["ID"] == emprestimo["Produto_ID"]:
                            produto["Estado"] = "disponível"
                            self.gestao.eliminar_emprestimo(emprestimo_id)                    
                            message = "Produto excluído com sucesso!"
                            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/img/success_icon.png" 
                            show_custom_messagebox("Produto", message, 300, 300, img)  
                    

        # Excluir o item selecionado na treeview
        self.tree.delete(selected_item)

    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.clear_frames()
        self.master.create_frames()
