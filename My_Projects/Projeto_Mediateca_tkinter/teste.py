import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk  # Importe o ThemedTk do ttkthemes
from tkinter import Frame, Label
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime

from produto import *
from gestao import *

gestao = Gestao()

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

class Criar_Produto_Frame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        self.selected_media_widgets = None  # Variável para controlar os widgets selecionados
        self.calendar_data_pub = None  # Adicione esse atributo para acessá-lo em outros métodos
        self.editora = None
        self.autores = None
        self.suporte = None
        self.duracao = None
        self.atores = None
        self.tipo_video = None
        self.tipo_audio = None
        self.trilhas = None        
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

    def set_theme(self, theme_name):
        self.master.set_theme(theme_name)

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
            #self.tipo_pub = self.tipo_pub.get()  # Atualiza o valor de self.tipo_pub

        elif selected_media_type == "Vídeo":
            self.selected_media_widgets = self.video_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame

        elif selected_media_type == "Áudio":
            self.selected_media_widgets = self.audio_widgets(self.selected_media_frame)
            self.selected_media_widgets.pack()  # Adiciona e mostra os widgets no frame


    # Mostra os widgets específicos para o tipo de mídia "Publicação"
    def publicacao_widgets(self, master):
        frame = tk.Frame(master)

        # Label and Entry for Tipo de Publicação
        self.label_tipo_pub = tk.Label(frame, text="Tipo de Publicação:")
        self.label_tipo_pub.grid(row=0, column=0, padx=10, pady=5)

        self.tipo_pub = tk.Entry(frame)  # Store the Entry widget in self.tipo_pub
        self.tipo_pub.grid(row=0, column=1, padx=10, pady=5)

        # Label and Calendar for data da publicação
        label_data_pub = tk.Label(frame, text="Data da Publicação:")
        label_data_pub.grid(row=1, column=0, padx=10, pady=5)

        self.calendar_data_pub = DateEntry(frame, date_pattern='dd/mm/Y')
        self.calendar_data_pub.grid(row=1, column=1, padx=10, pady=5)

        # Label and Entry for Editora
        label_editora = tk.Label(frame, text="Editora:")
        label_editora.grid(row=2, column=0, padx=10, pady=5)

        self.editora = tk.Entry(frame)
        self.editora.grid(row=2, column=1, padx=10, pady=5)

        # Label and Entry for Autores
        label_autores = tk.Label(frame, text="Autores:")
        label_autores.grid(row=3, column=0, padx=10, pady=5)

        self.autores = tk.Entry(frame)
        self.autores.grid(row=3, column=1, padx=10, pady=5)

        # Label and Combobox for the Suporte
        label_suporte = tk.Label(frame, text="Suporte:")
        label_suporte.grid(row=4, column=0, padx=10, pady=5)

        self.suporte = ttk.Combobox(frame, values=["Papel", "Eletrónico"])
        self.suporte.grid(row=4, column=1, padx=10, pady=5)

        self.create_products_widgets(frame)

        return frame

    
    # Mostra os widgets específicos para o tipo de media "Vídeo"
    def video_widgets(self, master):   

        frame = tk.Frame(self.selected_media_frame)
        #frame = tk.Frame(master)

        # Label e Combobox para o Tipo de Vídeo
        label_tipo_video = tk.Label(frame, text="Tipo de Vídeo:")
        self.tipo_video = ttk.Combobox(frame, values=["Filme", "Documentário", "Série", "Programa de TV", "Outro"])

        # Label e Entry para Duração
        label_duracao_video = tk.Label(frame, text="Duração:")
        self.duracao = tk.Entry(frame)

        # Label e Entry para Atores
        label_atores = tk.Label(frame, text="Atores:")
        self.atores = tk.Entry(frame)

        # Posicionamento dos widgets para o grid
        label_tipo_video.grid(row=0, column=0, padx=10, pady=5)
        self.tipo_video.grid(row=0, column=1, padx=10, pady=5)

        label_duracao_video.grid(row=1, column=0, padx=10, pady=5)
        self.duracao.grid(row=1, column=1, padx=10, pady=5)

        label_atores.grid(row=2, column=0, padx=10, pady=5)
        self.atores.grid(row=2, column=1, padx=10, pady=5)

        self.create_products_widgets(frame)

        return frame

    # Mostra os widgets específicos para o tipo de mídia "Áudio"
    def audio_widgets(self, master):

        frame = tk.Frame(self.selected_media_frame)
        
        # Label e Combobox para o Tipo de Áudio
        label_tipo_audio = tk.Label(frame, text="Tipo de Áudio:")
        self.tipo_audio = ttk.Combobox(frame, values=["CD", "DVD", "Blu-ray", "K7", "Vinil", "Outro"])

        # Label e Entry para Duração
        label_duracao_audio = tk.Label(frame, text="Duração:")
        self.duracao = tk.Entry(frame)

        # Label e Entry para Trilhas
        label_trilhas = tk.Label(frame, text="Trilhas:")
        self.trilhas = tk.Entry(frame)

        # Posicionamento dos widgets para o grid
        label_tipo_audio.grid(row=0, column=0, padx=10, pady=5)
        self.tipo_audio.grid(row=0, column=1, padx=10, pady=5)

        label_duracao_audio.grid(row=1, column=0, padx=10, pady=5)
        self.duracao.grid(row=1, column=1, padx=10, pady=5)

        label_trilhas.grid(row=2, column=0, padx=10, pady=5)
        self.trilhas.grid(row=2, column=1, padx=10, pady=5)

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
        botao_criar = ttk.Button(master, text="Criar Produto", command=self.criar_produto, style="My.TButton", width=68)
        botao_criar.grid(row=10, column=0, columnspan=2, padx=10, pady=3)  # Usamos columnspan=2 para ocupar 2 colunas

        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton", width=68)
        botao_voltar.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

    def voltar_menu_anterior(self):
        # Chame a função na classe MenuGestaoProdutos que retorna ao menu principal
        self.master.clear_frames()
        self.master.create_frames()
               
    
    def verificar_titulo(self):
        titulo = self.entry_titulo.get().upper()
        for produto in gestao.produtos:
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

    def show_product_details_message(self, produto, media):
        message = f"Produto criado com sucesso!\n\n"
        message += f"Título: {produto.titulo}\n"
        message += f"Preço: €{produto.preco:.2f}\n"
        message += f"Data de Aquisição: {produto.data.strftime('%d/%m/%Y')}\n"
        message += f"Tipo de Media: {produto.tipo}\n"
        img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/success_icon.png"

        if produto.tipo == "Publicação":
            message += f"Tipo de Publicação: {media.tipo_pub}\n"
            message += f"Data da Publicação: {media.data_pub.strftime('%d/%m/%Y')}\n"
            message += f"Editora: {media.editora}\n"
            message += f"Autores: {media.autores}\n"
            message += f"Suporte: {media.suporte}\n"
            # You can add more attributes to display here based on your product class

            #messagebox.showinfo("Produto Criado", message)
            
            show_custom_messagebox("Produto Criado", message, 400, 400, img)

        
        elif produto.tipo == "Vídeo":
            message += f"Tipo de Vídeo: {media.tipo_video}\n"
            message += f"Duração: {media.duracao}\n"
            message += f"Atores: {media.atores}\n"
            # You can add more attributes to display here based on your product class

            #messagebox.showinfo("Produto Criado", message)
            show_custom_messagebox("Produto Criado", message, 400, 400, img)


        elif produto.tipo == "Áudio":
            message += f"Tipo de Áudio: {media.suporte}\n"
            message += f"Duração: {media.duracao}\n"
            message += f"Trilhas: {media.trilhas}\n"
            # You can add more attributes to display here based on your product class

            #messagebox.showinfo("Produto Criado", message)
            show_custom_messagebox("Produto Criado", message, 400, 400, img)

       
    # Função para criar o produto
    def criar_produto(self):

        # Oculta o frame atual da janela principal
        self.master.criar_produto_frame.grid_forget() 

        # Mostra o novo frame criado para a página de criar produto
        self.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
           
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
            tipo_media = Produto.tipo[0]
            tipo_pub = self.tipo_pub.get()
            data_pub = self.calendar_data_pub.get_date()
            editora = self.editora.get()
            autores = self.autores.get()
            suporte = self.suporte.get()
        
            publicacao = Publicacao(tipo_pub, data_pub, editora, autores, suporte)
            produto = Produto(tipo_media, publicacao, titulo, preco, data_aquisicao)
            gestao.criar_produto(produto)
            gestao.obter_produto("1")
            self.show_product_details_message(produto, publicacao)
            
            
        
        elif tipo_media == "Vídeo":            
        
            tipo_media = Produto.tipo[1]
            duracao = self.duracao.get()
            
            # Validação do preço para não permitir inserção de um input diferente de um float
            if not self.validar_float(duracao):
                self.label_aviso.config(text="Duração inválida. Digite uma número válido!", fg="red")
                return
            self.label_aviso.config(text="")            
            duracao = float(duracao)

            tipo = self.tipo_video.get()            
            atores = self.atores.get().upper() 
            video = Video(duracao, tipo, atores)
            produto = Produto(tipo_media, video, titulo, preco, data_aquisicao)
            gestao.criar_produto(produto)
            self.show_product_details_message(produto, video)

        else:
            tipo_media = Produto.tipo[2]            
            duracao = self.duracao.get()

            # Validação do preço para não permitir inserção de um input diferente de um float
            if not self.validar_float(duracao):
                self.label_aviso.config(text="Duração inválida. Digite um número válido!", fg="red")
                return
            self.label_aviso.config(text="")            
            duracao = float(duracao)
            tipo = self.tipo_audio.get()             
            trilhas = self.trilhas.get().upper()            
            audio = Audio(duracao, tipo, trilhas)
            produto = Produto(tipo_media, audio, titulo, preco, data_aquisicao)
            gestao.criar_produto(produto)
            self.show_product_details_message(produto, audio)


class OpcoesProdutoFrame(tk.Frame):
    def __init__(self, master, treeview, gestao):
        super().__init__(master)
        self.treeview = treeview
        self.gestao = gestao
        self.create_widgets()

    def create_widgets(self):
    
        # Botão "Mais Detalhes"
        botao_mais_detalhes = ttk.Button(self, text="Mais Detalhes", command=self.ver_mais_detalhes)
        botao_mais_detalhes.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Botão "Atualizar"
        botao_atualizar = ttk.Button(self, text="Atualizar", command=self.atualizar_produto)
        botao_atualizar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Botão "Excluir"
        botao_excluir = ttk.Button(self, text="Excluir", command=self.excluir_produto)
        botao_excluir.grid(row=0, column=2, padx=5, pady=5, sticky="ew")     

        # Botão "Voltar" para retornar ao menu anterior
        botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_menu_anterior, style="My.TButton")
        botao_voltar.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

            
    def ver_mais_detalhes(self):
        # Obter o item selecionado na treeview
        selected_item = self.treeview.selection()

        if not selected_item:
            return  # Nenhum item selecionado, não fazer nada

        # Obter os valores da linha selecionada
        item_values = self.treeview.item(selected_item)["values"]

        # Obter o ID do tipo de mídia da linha selecionada
        produto_id = item_values[0]  # O índice 0 corresponde à coluna "ID"

        # Buscar as informações completas do tipo de mídia usando o ID
        tipo_midia_info = self.gestao.obter_produto(produto_id)

        if not tipo_midia_info:
            return  # Tipo de mídia não encontrado, não fazer nada     
       

        if tipo_midia_info["Tipo"] == "Publicação":    
            message = f"Tipo de Publicação: {tipo_midia_info['Media']['Tipo de Publicação']}\n"
            message += f"Data da Publicação: {tipo_midia_info['Media']['Data da Publicação']}\n"
            message += f"Editora: {tipo_midia_info['Media']['Editora']}\n"
            message += f"Autores: {tipo_midia_info['Media']['Autores']}\n"
            message += f"Suporte: {tipo_midia_info['Media']['Suporte']}\n" 
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/publication_icon.png"       
            
            show_custom_messagebox("Mais Detalhes", message, 300, 350, img)

        elif tipo_midia_info["Tipo"] == "Vídeo":   

            message = f"Tipo de Vídeo: {tipo_midia_info['Media']['Tipo de Vídeo']}\n"
            message += f"Duração: {tipo_midia_info['Media']['Duração']}\n"
            message += f"Atores: {tipo_midia_info['Media']['Atores']}\n"
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/video_icon.png"   
            
            
            show_custom_messagebox("Mais Detalhes", message, 300, 350, img)


        elif tipo_midia_info["Tipo"] =="Áudio":

            message = f"Tipo de Áudio: {tipo_midia_info['Media']['Suporte']}\n"
            message += f"Duração: {tipo_midia_info['Media']['Duração']}\n"
            message += f"Trilhas: {tipo_midia_info['Media']['Trilhas']}\n"
            img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/audio_icon.png"   

            show_custom_messagebox("Mais Detalhes", message, 300, 350, img)

    def abrir_atualizar_produto_popup(self, produto_id):
        # Obter as informações completas do produto usando o ID
        produto_info = self.gestao.obter_produto(produto_id)

        if not produto_info:
            return  # Produto não encontrado, não fazer nada

        # Verificar o estado do produto antes de permitir a atualização
        if produto_info["Estado"] not in ["disponível"]:
            messagebox.showwarning("Atualização não permitida",
                                   "Não é possível atualizar o produto com estado diferente de 'Disponível'.")
            return

        # Criar a janela popup para atualizar o produto
        atualizar_popup_window = tk.Toplevel(self)
        atualizar_popup_window.title("Atualizar Produto")

        # Criar uma instância do frame Criar_Produto_Frame passando o master como a janela popup de atualização
        criar_produto_frame = Criar_Produto_Frame(atualizar_popup_window)

        # Preencher os campos do frame Criar_Produto_Frame com as informações do produto selecionado
        criar_produto_frame.combobox_tipo_media.set(produto_info["Tipo"])
        criar_produto_frame.entry_titulo.insert(0, produto_info["Título"])
        criar_produto_frame.entry_preco.insert(0, f"{produto_info['Preço']:.2f}")
        criar_produto_frame.calendar_data_aquisicao.set_date(produto_info["Data_Aquisição"])

        # Dependendo do tipo de mídia, preencher os campos específicos da mídia
        if produto_info["Tipo"] == "Publicação":
            # Para produtos do tipo Publicação
            media_info = produto_info["Media"]
            criar_produto_frame.tipo_pub.insert(0, media_info["Tipo de Publicação"])
            criar_produto_frame.calendar_data_pub.set_date(media_info["Data da Publicação"])
            criar_produto_frame.editora.insert(0, media_info["Editora"])
            criar_produto_frame.autores.insert(0, media_info["Autores"])
            criar_produto_frame.suporte.set(media_info["Suporte"])

        elif produto_info["Tipo"] == "Vídeo":
            # Para produtos do tipo Vídeo
            media_info = produto_info["Media"]
            criar_produto_frame.duracao.insert(0, str(media_info["Duração"]))
            criar_produto_frame.tipo_video.set(media_info["Tipo de Vídeo"])
            criar_produto_frame.atores.insert(0, media_info["Atores"])

        elif produto_info["Tipo"] == "Áudio":
            # Para produtos do tipo Áudio
            media_info = produto_info["Media"]
            criar_produto_frame.duracao.insert(0, str(media_info["Duração"]))
            criar_produto_frame.tipo_audio.set(media_info["Tipo de Áudio"])
            criar_produto_frame.trilhas.insert(0, media_info["Trilhas"])

        # Adicionar um botão "Atualizar" que chama a função para atualizar o produto com as informações alteradas
        botao_atualizar = ttk.Button(atualizar_popup_window, text="Atualizar",
                                    command=lambda: self.atualizar_produto_info(criar_produto_frame, produto_id))
        botao_atualizar.pack(padx=10, pady=5)

        # Adicionar um botão "Fechar" para fechar a janela popup de atualização
        botao_fechar = ttk.Button(atualizar_popup_window, text="Fechar", command=atualizar_popup_window.destroy)
        botao_fechar.pack(padx=10, pady=5)

    def atualizar_produto(self):
        # Obter o item selecionado na treeview
        selected_item = self.tree.selection()

        if not selected_item:
            return  # Nenhum item selecionado, não fazer nada

        # Obter os valores da linha selecionada
        item_values = self.tree.item(selected_item)["values"]

        # Obter o ID do produto selecionado
        produto_id = item_values[0]

        # Chamar o novo método para abrir a janela de atualização do produto
        self.abrir_atualizar_produto_popup(produto_id)

            
    def excluir_produto(self):
        # Obter o item selecionado na treeview
        selected_item = self.treeview.selection()

        if not selected_item:
            return  # Nenhum item selecionado, não fazer nada

        # Obter o ID do produto selecionado
        produto_id = self.treeview.item(selected_item, "values")[0]

        # Excluir o produto da gestao.produtos usando o ID
        for produto in self.gestao.produtos:
            if produto["ID"] == produto_id:
                if produto["Estado"] == "emprestado" or produto["Estado"] == "devolvido":
                    message = "Não é possível exluir um produto que já foi emprestado!"
                    img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/error_icon.png" 
                    show_custom_messagebox("Produto", message, 300, 300, img)                 
                    return
                else:                     
                    self.gestao.eliminar_produto(produto_id)
                    message = "Produto excluído com sucesso!"
                    img = "/Users/yveneeschneider/UPSKILL/My_Projects/Projeto_Mediateca_tkinter/success_icon.png" 
                    show_custom_messagebox("Produto", message, 300, 300, img)    

        # Excluir o item selecionado na treeview
        self.treeview.delete(selected_item)

    def voltar_menu_anterior(self):
        # Chame a função na classe mestre (ou seja, a janela principal) que retorna ao menu anterior
        self.master.master.clear_frames()
        self.master.master.create_frames()

class Listar_Produtos_Frame(tk.Frame):
    def __init__(self, master, gestao, **kwargs):
        super().__init__(master, **kwargs)
        self.gestao = gestao
        self.create_widgets()
    
    def create_widgets(self):
        # Criar o widget ttk.Treeview
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
        self.tree.column("Data de Aquisição", width=100)
        self.tree.column("Tipo de Media", width=100)
        self.tree.column("Estado", width=100)

        # Adicionar o widget ttk.Treeview à janela
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew") 

        # Configurar a coluna e a linha para se expandirem corretamente
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Chamar a função para preencher o treeview com os produtos existentes
        self.populate_treeview()

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')       

        # Adicionar a frame de opções (Atualizar e Excluir)
        opcoes_frame = OpcoesProdutoFrame(self, self.tree, self.gestao)
        
        #opcoes_frame = OpcoesProdutoFrame(self, self.trees)
        opcoes_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")


    def populate_treeview(self):
        # Limpar os itens existentes no treeview (caso já tenha algum)
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obter a lista de produtos da gestão
        produtos = self.gestao.produtos

        # Adicionar os produtos ao treeview
        for produto in produtos:
            id = produto["ID"]
            titulo = produto["Título"]
            estado = produto["Estado"]
            preco = f"€ {produto['Preço']:.2f}"
            data_aquisicao = produto["Data_Aquisição"].strftime("%d/%m/%Y")
            tipo_midia = produto["Tipo"]
            self.tree.insert("", "end", values=(id, titulo, preco, data_aquisicao, tipo_midia, estado))

   