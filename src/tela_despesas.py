import customtkinter as ctk
import tkinter as tk
from despesas_ex import lista_despesas as lst_despesas 

class InterfaceDespesas(ctk.CTk):
    def __init__(self, nomeUsuário="nomeUsuário"):
        super().__init__()
        self.nomeUsuário = nomeUsuário
        self.layout_config()
        self.interface()
        self.bind("<Configure>", self.atualizar_tamanho_janela)

    
    def layout_config(self):
        self.geometry("900x500+500+250")
        self.title("Gerenciador de Despesas")
        self.resizable(True, True)
        ctk.set_appearance_mode("dark")
    
    def interface(self):
        head_frame = ctk.CTkFrame(master=self, width=900, height=100, fg_color="#012", corner_radius=0)
        head_frame.place(x=0, y=0)

        head_label = ctk.CTkLabel(master=head_frame, text=f"Despesas de: {self.nomeUsuário}", font=("Roboto bold", 24), bg_color="#012", fg_color="#012")
        head_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        despesas_bt = ctk.CTkButton(master=self, command=self.interface_despesas, text="Despesas", width=225, height=50, corner_radius=0, fg_color="#003")
        despesas_bt.place(x=0, y=100)

        adicionar_bt = ctk.CTkButton(master=self, command=self.interface_adicionar_despesa, text="Adicionar despesa", width=225, height=50, corner_radius=0, fg_color="#004")
        adicionar_bt.place(x=225, y=100)

        gráficos_bt = ctk.CTkButton(master=self, command=self.interface_gráficos, text="Gráficos", width=225, height=50, corner_radius=0, fg_color="#005")
        gráficos_bt.place(x=450, y=100)

        outro_bt = ctk.CTkButton(master=self, command=None, text="outro botão", width=225, height=50, corner_radius=0, fg_color="#006")
        outro_bt.place(x=675, y=100)

        self.interface_despesas()

    
    def interface_despesas(self):

        despesas = lst_despesas

        aba_despesas = ctk.CTkScrollableFrame(master=self, width=885, height=500, fg_color="#003", bg_color="#014", corner_radius=0)
        aba_despesas.place(x=0, y=200)

        head_frame = ctk.CTkFrame(master=self, width=900, height=50, fg_color="#003", bg_color="#014", corner_radius=0)
        head_frame.place(x=0, y=150)

        despesas_title = ctk.CTkLabel(master=head_frame, text="Despesas", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        despesas_title.place(x=50, y=10)

        data_title = ctk.CTkLabel(master=head_frame, text="Data", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        data_title.place(x=250, y=10)

        categoria_title = ctk.CTkLabel(master=head_frame, text="Categoria", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        categoria_title.place(x=470, y=10)

        valor_title = ctk.CTkLabel(master=head_frame, text="Valor", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        valor_title.place(x=690, y=10)

        for idx, chave in enumerate(despesas.keys()):

            despesa_frame = ctk.CTkFrame(master=aba_despesas, width=225, height=50, fg_color="red")
            despesa_frame.pack(padx=0, pady=10, anchor="w")

            despesa_label = ctk.CTkLabel(master=despesa_frame, text="Despesa", 
                                         font=("Roboto bold", 12), 
                                         bg_color="transparent", 
                                         text_color="#fff")
            despesa_label.pack(padx=20, pady=10)

            data_frame = ctk.CTkFrame(master=aba_despesas, width=225, height=50, fg_color="green")
            data_frame.pack(padx=240, pady=10, anchor="w")

            data_label = ctk.CTkLabel(master=data_frame, text="Data", 
                                         font=("Roboto bold", 12), 
                                         bg_color="transparent", 
                                         text_color="#fff")
            data_label.pack(padx=20, pady=10)
            




            divisor = ctk.CTkFrame(master=aba_despesas, 
                                   width=800, 
                                   height=2, 
                                   fg_color="#ccc", 
                                   bg_color="#014", 
                                   corner_radius=2, 
                                   border_color="#ccc", 
                                   border_width=2)

        

    def interface_adicionar_despesa(self):
        aba_adicionar_despesa = ctk.CTkFrame(master=self, width=900, height=350, fg_color="#004", bg_color="#014", corner_radius=0)
        aba_adicionar_despesa.place(x=0, y=150)


    def interface_gráficos(self):
        aba_gráficos = ctk.CTkFrame(master=self, width=900, height=350, fg_color="#005", bg_color="#014", corner_radius=0)
        aba_gráficos.place(x=0, y=150)

    def atualizar_tamanho_janela(self, event):
        largura = self.winfo_width()
        altura = self.winfo_height()
        
    def limpa_tela(self):
        for item in self.winfo_children():
            item.destroy()


app = InterfaceDespesas()
app.mainloop()