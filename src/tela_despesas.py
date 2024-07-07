import customtkinter as ctk

class InterfaceDespesas(ctk.CTk):
    def __init__(self, nomeUsuário="nomeUsuário"):
        super().__init__()
        self.nomeUsuário = nomeUsuário
        self.layout_config()
        self.aparência()
        self.interface()

    
    def layout_config(self):
        self.geometry("900x500+500+250")
        self.title("Gerenciador de Despesas")
        self.resizable(False, False)


    def aparência(self):
        ctk.set_appearance_mode("dark")

    
    def interface(self):

        head_frame = ctk.CTkFrame(master=self, width=900, height=100, fg_color="#012", corner_radius=0)
        head_frame.place(x=0, y=0)

        head_label = ctk.CTkLabel(master=head_frame, text=f"Despesas de: {self.nomeUsuário}", font=("Roboto bold", 24), bg_color="#012", fg_color="#012")
        head_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        aba_despesas = ctk.CTkFrame(master=self, width=900, height=350, fg_color="#014", bg_color="#014", corner_radius=0)
        aba_despesas.place(x=0, y=150)

        aba_adicionar_despesa = ctk.CTkFrame(master=self)


        aba_gráficos = ctk.CTkFrame(master=self)

        despesas_bt = ctk.CTkButton(master=self, text="Despesas", width=300, height=50, corner_radius=0, fg_color="#014")
        despesas_bt.place(x=0, y=100)

        adicionar_bt = ctk.CTkButton(master=self, text="Adicionar despesa", width=300, height=50, corner_radius=0, fg_color="#016")
        adicionar_bt.place(x=300, y=100)

        gráficos_bt = ctk.CTkButton(master=self, text="Gráficos", width=300, height=50, corner_radius=0, fg_color="#018")
        gráficos_bt.place(x=600, y=100)

    
    def mostrar_despesas(self):
        pass


    def adicionar_despesa(self):
        pass


    def gráficos(self):
        pass

    def limpa_tela(self):
        for item in self.winfo_children():
            item.destroy()


app = InterfaceDespesas()
app.mainloop()