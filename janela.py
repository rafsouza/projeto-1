###     Janela de Login     ###

def codjanela():
  import customtkinter

  # Função do botão [Entrar]
  def clique():
    a=1 # Login aceito
    print("Funcionou")   
    login.destroy() # Fecha a janela de login
    return a # Era para retornar a variável de login aceito (1) ou não aceito (0), mas não está retornando, ainda não investiguei o porquê

  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("dark-blue")

  login = customtkinter.CTk()
  login.geometry("400x400")
  login.title("Coletivo Morro das Panelas")

  texto = customtkinter.CTkLabel(login, text="Fazer Login")
  texto.pack(padx=10, pady=10)

  email = customtkinter.CTkEntry(login, placeholder_text="Digite seu Email")
  email.pack(padx=10, pady=10)

  senha = customtkinter.CTkEntry(login, placeholder_text= "Digite sua Senha", show="#")
  senha.pack(padx=10, pady=10)

  botao = customtkinter.CTkButton(login, text="Clique para Entrar",  command=clique)
  botao.pack(padx=10, pady=10)

  login.mainloop()