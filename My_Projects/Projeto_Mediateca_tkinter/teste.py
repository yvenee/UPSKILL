    def create_widgets(self):
        # Botão "Listar Produtos Multimídia"
        botao_listar_produtos_mult = ttk.Button(self, text="Listar Produtos Multimídia", command=self.listar_produtos_mult, style="My.TButton", width=25)        
        botao_listar_produtos_mult.grid(row=0, column=0, padx=5, pady=5)

    def listar_produtos_mult(self):
        # Cria uma nova janela para listar os produtos multimídia
        top = tk.Toplevel()
        top.title("Listar Produtos Multimídia")
        top.geometry("800x400")

        # Dropdown para selecionar a ordenação
        opcoes_ordenacao = ["Ordem Alfabética", "Ordem de Data de Aquisição Crescente", "Ordem de Data de Aquisição Decrescente"]
        self.var_ordenacao = tk.StringVar(value=opcoes_ordenacao[0])
        dropdown_ordenacao = ttk.OptionMenu(top, self.var_ordenacao, *opcoes_ordenacao, command=self.on_dropdown_change)
        dropdown_ordenacao.grid(row=0, column=0, padx=10, pady=10)

        # Treeview para exibir os produtos
        columns = ("ID", "Título", "Preço", "Data de Aquisição", "Tipo de Media", "Estado")
        self.tree = ttk.Treeview(top, columns=columns, show='headings')

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

        self.tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Popula a treeview inicialmente por ordem alfabética
        self.populate_treeview_ordenado_por("Título")

    def on_dropdown_change(self, selected_option):
        if selected_option == "Ordem Alfabética":
            self.populate_treeview_ordenado_por("Título")
        elif selected_option == "Ordem de Data de Aquisição Crescente":
            self.populate_treeview_ordenado_por("Data_Aquisição", reverse=False)
        elif selected_option == "Ordem de Data de Aquisição Decrescente":
            self.populate_treeview_ordenado_por("Data_Aquisição", reverse=True)

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
