###     Cadastrar Produtor     ###
def codcadastr():
  import customtkinter

  # Função do botão [Cadastrar]
  def clique2():
    print("Cadastrou")


  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  janela = customtkinter.CTk()
  janela.geometry("400x600")
  janela.title("Coletivo Morro das Panelas - Cadastro de produtor")

  texto = customtkinter.CTkLabel(janela, text="Cadastro de produtores")
  texto.pack(padx=10, pady=10)

  nome = customtkinter.CTkEntry(janela, placeholder_text="Nome*")
  nome.pack(padx=10, pady=10)

  cpf = customtkinter.CTkEntry(janela, placeholder_text="CPF*")
  cpf.pack(padx=10, pady=10)

  fone = customtkinter.CTkEntry(janela, placeholder_text="Telefone*")
  fone.pack(padx=10, pady=10)

  ender = customtkinter.CTkEntry(janela, placeholder_text="Endereço")
  ender.pack(padx=10, pady=10)

  email = customtkinter.CTkEntry(janela, placeholder_text="Email")
  email.pack(padx=10, pady=10)

  botao = customtkinter.CTkButton(janela, text="Cadastrar",  command=clique2)
  botao.pack(padx=10, pady=10)

  janela.mainloop()




###     Cadastrar Cliente     ###
def codcliente():
  import customtkinter

  # Função do botão [Cadastrar]
  def clique2():
    print("Cadastrou")


  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  janela = customtkinter.CTk()
  janela.geometry("400x600")
  janela.title("Coletivo Morro das Panelas - Cadastro de cliente")

  texto = customtkinter.CTkLabel(janela, text="Cadastro de clientes")
  texto.pack(padx=10, pady=10)

  nome = customtkinter.CTkEntry(janela, placeholder_text="Nome*")
  nome.pack(padx=10, pady=10)

  cpf = customtkinter.CTkEntry(janela, placeholder_text="CPF*")
  cpf.pack(padx=10, pady=10)

  fone = customtkinter.CTkEntry(janela, placeholder_text="Telefone*")
  fone.pack(padx=10, pady=10)

  ender = customtkinter.CTkEntry(janela, placeholder_text="Endereço")
  ender.pack(padx=10, pady=10)

  email = customtkinter.CTkEntry(janela, placeholder_text="Email")
  email.pack(padx=10, pady=10)

  botao = customtkinter.CTkButton(janela, text="Cadastrar",  command=clique2)
  botao.pack(padx=10, pady=10)

  janela.mainloop()




###    Cadastrar Produto     ###
def codproduto():
  import customtkinter

  # Função do botão [Enviar]
  def clique3():
    print("Enviou")


  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  janela = customtkinter.CTk()
  janela.geometry("400x600")
  janela.title("Coletivo Morro das Panelas - Cadastro de produto")

  texto = customtkinter.CTkLabel(janela, text="Cadastro de produtos")
  texto.pack(padx=10, pady=10)

  nome = customtkinter.CTkEntry(janela, placeholder_text="Nome do produto*", width=250)
  nome.pack(padx=10, pady=10)

  qtd = customtkinter.CTkEntry(janela, placeholder_text="Quantidade*", width=250)
  qtd.pack(padx=10, pady=10)

  prc = customtkinter.CTkEntry(janela, placeholder_text="Porção (unidade, dúzia, kg, ml, ...)*", width=250)
  prc.pack(padx=10, pady=10)

  preco = customtkinter.CTkEntry(janela, placeholder_text="Preço (por porção)", width=250)
  preco.pack(padx=10, pady=10)

  categ = customtkinter.CTkEntry(janela, placeholder_text="Categoria", width=250)
  categ.pack(padx=10, pady=10)

  botao = customtkinter.CTkButton(janela, text="Enviar",  command=clique3)  
  botao.pack(padx=10, pady=10)

  janela.mainloop()
