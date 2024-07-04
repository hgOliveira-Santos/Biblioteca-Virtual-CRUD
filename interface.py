import customtkinter as ctk
from PIL import Image, ImageTk

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.aparência()
        self.sistema()

    def layout_config(self):
        self.geometry("1000x550+450+200")
        self.title("Despesas Pessoais")
        self.resizable(False, False)

    def aparência(self):
        ctk.set_appearance_mode("light")

    def sistema(self):
        #head_frame = ctk.CTkFrame(master=self, width=1000, height=80, bg_color="#037899", fg_color="#037899")
        #head_frame.place(x=0, y=0)

        head_label  = ctk.CTkLabel(master=self, text="Criar conta", font=('Century Gothic', 26), text_color="#000")
        head_label.place(x=20, y=60)

        imagem = Image.open('images/dinheiro.jpg')
        imagem_dinheiro = ImageTk.PhotoImage(imagem)

        imagem_label = ctk.CTkLabel(master=self, image=imagem_dinheiro)
        imagem_label.place(x=500)

        self.criar_conta()

    def login(self):
        self.usuário_value = ctk.StringVar()
        self.senha_value = ctk.StringVar()

        usuário_label = ctk.CTkLabel(master=self, text="Usuário:", font=('Century Gothic', 21), text_color="#000")
        usuário_label.place(x=20, y=100)

        usuário_input = ctk.CTkEntry(master=self, textvariable=self.usuário_value, fg_color="transparent", font=('Century Gothic', 21), text_color="#000")
        usuário_input.place(x=20, y=250)

        senha_label = ctk.CTkLabel(master=self, text="Senha: ", font=('Century Gothic', 21), text_color="#000")
        senha_label.place(x=20, y=140)

        senha_input = ctk.CTkEntry(master=self, textvariable=self.senha_value, fg_color="transparent", font=('Century Gothic', 21), text_color="#000")
        senha_input.place(x=20, y=350)

        confirmar_senha_input = ctk.CTkEntry(master=self, textvariable=self.senha_value, fg_color="transparent", font=('Century Gothic', 21), text_color="#000")
        confirmar_senha_input.place(x=20, y=500)
        
        """cadastrar_bt = ctk.CTkButton(master=self, text="Cadastrar", command=None, fg_color="#039999", hover_color="#046979")
        cadastrar_bt.place(x=60, y=400)"""

    def criar_conta(self):

        self.usuário_value = ctk.StringVar()
        self.senha_value = ctk.StringVar()

        usuário_label = ctk.CTkLabel(master=self, text="Usuário:", font=('Century Gothic', 21), text_color="#000")
        usuário_label.place(x=20, y=100)

        usuário_input = ctk.CTkEntry(master=self, textvariable=self.usuário_value, fg_color="transparent", font=('Century Gothic', 21), text_color="#000")
        usuário_input.place(x=20, y=250)

        senha_label = ctk.CTkLabel(master=self, text="Senha: ", font=('Century Gothic', 21), text_color="#000")
        senha_label.place(x=20, y=140)

        senha_input = ctk.CTkEntry(master=self, textvariable=self.senha_value, fg_color="transparent", font=('Century Gothic', 21), text_color="#000")
        senha_input.place(x=20, y=350)

        cadastrar_bt = ctk.CTkButton(master=self, text="Cadastrar", command=None, fg_color="#039999", hover_color="#046979")
        cadastrar_bt.place(x=60, y=400)

        



teste = Interface()
teste.mainloop()