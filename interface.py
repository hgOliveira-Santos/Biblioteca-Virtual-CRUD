import customtkinter as ctk
import tkinter as tk
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

        conta_label  = ctk.CTkLabel(master=self, text="Criar conta", font=('Century Gothic', 26), text_color="#000")
        conta_label.place(x=170, y=100)

        imagem = Image.open('images/dinheiro.jpg')
        imagem_dinheiro = ImageTk.PhotoImage(imagem)

        imagem_label = ctk.CTkLabel(master=self, image=imagem_dinheiro)
        imagem_label.place(x=500)

        self.interface_cadastro()

    def interface_cadastro(self):

        self.usuário_value = ctk.StringVar()
        self.senha_value = ctk.StringVar()
        self.confirmar_senha_value = ctk.StringVar()

        usuário_label = ctk.CTkLabel(master=self, text="Usuário:", font=('Roboto', 16), text_color="#000")
        usuário_label.place(x=40, y=150)

        usuário_input = ctk.CTkEntry(master=self, textvariable=self.usuário_value, width=420, corner_radius=10, fg_color="transparent", font=('Century Gothic', 16), text_color="#000")
        usuário_input.place(x=40, y=180)

        senha_label = ctk.CTkLabel(master=self, text="Senha: ", font=('Roboto', 16), text_color="#000")
        senha_label.place(x=40, y=220)

        senha_input = ctk.CTkEntry(master=self, textvariable=self.senha_value, show="*", width=420, corner_radius=10, fg_color="transparent")
        senha_input.place(x=40, y=250)

        confirmar_senha_label = ctk.CTkLabel(master=self, text="Confirme sua senha: ", font=('Roboto', 16), text_color="#000")
        confirmar_senha_label.place(x=40, y=290)

        confirmar_senha_input = ctk.CTkEntry(master=self, textvariable=self.confirmar_senha_value, show="*", width=420, corner_radius=10, fg_color="transparent")
        confirmar_senha_input.place(x=40, y=320)        

        cadastrar_bt = ctk.CTkButton(master=self, text="Cadastrar", command=self.verificar_senha, width=420, height=35, corner_radius=10, fg_color="#039999", hover_color="#046979")
        cadastrar_bt.place(x=40, y=360)

        possui_conta_label = ctk.CTkLabel(master=self, text="Já possui uma conta?", text_color="#012", font=("Roboto", 12))
        possui_conta_label.place(x=90, y=410)

        fazer_login_button = ctk.CTkButton(master=self, text="Faça login aqui", text_color="#012", font=("Roboto bold", 12), width=210, corner_radius=10, hover_color="#5aa0a0", fg_color="#acc", bg_color="transparent")
        fazer_login_button.place(x=250, y=410)

    def interface_login(self):

        self.usuário_value = ctk.StringVar()
        self.senha_value = ctk.StringVar()

        usuário_label = ctk.CTkLabel(master=self, text="Usuário:", font=('Roboto', 16), text_color="#000")
        usuário_label.place(x=40, y=160)

        usuário_input = ctk.CTkEntry(master=self, textvariable=self.usuário_value, width=420, corner_radius=10, fg_color="transparent", font=('Century Gothic', 16), text_color="#000")
        usuário_input.place(x=40, y=190)

        senha_label = ctk.CTkLabel(master=self, text="Senha: ", font=('Roboto', 16), text_color="#000")
        senha_label.place(x=40, y=230)

        senha_input = ctk.CTkEntry(master=self, textvariable=self.senha_value, show="*", width=420, corner_radius=10, fg_color="transparent")
        senha_input.place(x=40, y=260)

        cadastrar_bt = ctk.CTkButton(master=self, text="Entrar", command=None, width=420, height=35, corner_radius=10, fg_color="#039999", hover_color="#046979")
        cadastrar_bt.place(x=40, y=310)

        não_possui_conta_label = ctk.CTkLabel(master=self, text="Não possui uma conta?", text_color="#012", font=("Roboto", 12))
        não_possui_conta_label.place(x=90, y=360)

        fazer_cadastro_button = ctk.CTkButton(master=self, text="Cadastre-se aqui", text_color="#012", font=("Roboto bold", 12), width=210, corner_radius=10, hover_color="#5aa0a0", fg_color="#acc", bg_color="transparent")
        fazer_cadastro_button.place(x=250, y=360)

    def verifica_cadastro(self):
        pass


    def verificar_senha(self):
        if self.senha_value.get() == self.confirmar_senha_value.get():
            print("tudo certo")
        else:
            print("Senhas diferentes")

        



teste = Interface()
teste.mainloop()