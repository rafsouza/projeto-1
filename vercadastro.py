from tabulate import tabulate # biblioteca para criar tabelas

###     Visualizar Produtores     ###
def prodcadastro():
  import customtkinter

  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  janela = customtkinter.CTk()
  janela.geometry("600x400")
  janela.title("Coletivo Morro das Panelas")

  texto = customtkinter.CTkLabel(janela, text="Produtores cadastrados")
  texto.pack(padx=20, pady=20)


  # Criação de tabela de exemplo
  data1 = [["Abel Alves", 11111111,"13 99999 1111", "Rua Um, 10", "abel@exemplo"], 
  ["Beto Bell", 22222222, "13 99999 2222", "Rua Dois, 10", "beto@exemplo"], 
  ["Carlos Correa", 33333333, "13 99999 3333", "Rua Tres, 10", "carlos@exemplo"]]

  # Cabeçalho da tabela
  col_names = ["Nome      ", "CPF             ", "Telefone", "Endereço  ", "Email"]

  # Mostrar tabela
  txt=tabulate(data1, headers=col_names, tablefmt="simple");
  texto = customtkinter.CTkLabel(janela, text=txt)
  texto.pack(padx=10, pady=10)


  janela.mainloop()





###     Visualizar Produtos     ###
def produtocadastro():
  import customtkinter

  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  janela = customtkinter.CTk()
  janela.geometry("600x400")
  janela.title("Coletivo Morro das Panelas")

  texto = customtkinter.CTkLabel(janela, text="Estoque de produtos")
  texto.pack(padx=20, pady=20)

  #define header names
  col_names = ["ID ", "Item ", "Porção", "Preço (por porção)", "Quantidade"]

  data1 = [["0001", "Abricó orgânico             ","300 g  ", "5,00", 14], 
  ["0002", "Banana prata orgânica", "dúzia  ", "4,00", 25]]

  data2 = [["0003", "Abóbora orgânica         ","500 g  ", "5,00", 10], 
  ["0004", "Cambuci orgânico     ", "unidade", "8,00", 15]]

  texto = customtkinter.CTkLabel(janela, text="PRODUTOS IN NATURA FRESCOS")
  texto.pack(padx=5, pady=5)
  #display table
  txt=tabulate(data1, headers=col_names, tablefmt="simple");
  texto = customtkinter.CTkLabel(janela, text=txt)
  texto.pack(padx=15, pady=15)


  texto = customtkinter.CTkLabel(janela, text="VEGANOS CONGELADOS IN NATURA")
  texto.pack(padx=5, pady=5)
  #display table
  txt=tabulate(data2, headers=col_names, tablefmt="simple");
  texto = customtkinter.CTkLabel(janela, text=txt)
  texto.pack(padx=15, pady=15)


  janela.mainloop()