import customtkinter as ctk
from tkinter import ttk

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
        aba_despesas = ctk.CTkFrame(master=self, width=900, height=350, fg_color="#003", bg_color="#013", corner_radius=0)
        aba_despesas.place(x=0, y=150)

        despesas = {
            "despesa 1": {
                "data": "00/00/0000",
                "categoria": "alimentação", 
                "valor": 120.00
            },
            "despesa 2": {
                "data": "11/11/2024",
                "categoria": "transporte",
                "valor": 40.00
            }
        }

        despesas_title = ctk.CTkLabel(master=aba_despesas, text="Despesas", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        despesas_title.place(x=50, y=10)

        data_title = ctk.CTkLabel(master=aba_despesas, text="Data", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        data_title.place(x=250, y=10)

        categoria_title = ctk.CTkLabel(master=aba_despesas, text="Categoria", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        categoria_title.place(x=470, y=10)

        valor_title = ctk.CTkLabel(master=aba_despesas, text="Valor", font=("Roboto bold", 15), bg_color="transparent", text_color="#fff")
        valor_title.place(x=690, y=10)

        y = 50
        for idx, despesa in enumerate(despesas.keys()):
            despesa_label = ctk.CTkLabel(master=aba_despesas, text=despesa, font=("Roboto bold", 12), bg_color="transparent", text_color="#fff")
            despesa_label.place(x=50, y=y + idx * 40)
            divisor = ctk.CTkFrame(master=aba_despesas, width=800, height=2, fg_color="#ccc", bg_color="#014", corner_radius=2, border_color="#ccc", border_width=2)
            divisor.place(x=50, y=y + 30 + idx * 40)
            
        lista_despesas = []

        for chave, dados in despesas.items():
            data = dados['data']
            categoria = dados['categoria']
            valor = dados['valor']
            despesa = (data, categoria, valor)
            lista_despesas.append(despesa)

        x = 250
        y = 50

        for idx1 in range(len(lista_despesas)): 
            for idx2 in range(len(lista_despesas[idx1])):               
                label = ctk.CTkLabel(master=aba_despesas, text=lista_despesas[idx1][idx2], font=("Roboto bold", 12), bg_color="transparent", text_color="#fff")
                label.place(x=x, y=y)
                x += 220
            x = 250
            y += 40





    def interface_adicionar_despesa(self):
        aba_adicionar_despesa = ctk.CTkFrame(master=self, width=900, height=350, fg_color="#004", bg_color="#014", corner_radius=0)
        aba_adicionar_despesa.place(x=0, y=150)


    def interface_gráficos(self):
        aba_gráficos = ctk.CTkFrame(master=self, width=900, height=350, fg_color="#005", bg_color="#014", corner_radius=0)
        aba_gráficos.place(x=0, y=150)

    def limpa_tela(self):
        for item in self.winfo_children():
            item.destroy()


app = InterfaceDespesas()
app.mainloop()