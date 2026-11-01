import tkinter as tk
janela = tk.Tk()
janela.title("Company")
janela.geometry("800x800")

# LABELS
nempresa = tk.Label(janela,text = "Nome da empresa")
nempresa.place(x=50,y=30)
cnpj = tk. Label(janela,text = "CNPJ").place(x=50,y=70)
endereco = tk. Label(janela,text = "Endereço").place(x=50,y=110)
email = tk.Label(janela, text = "email").place(x=53,y=150)
senha = tk.Label(janela, text = "senha").place(x=53,y=190)

#TEXTS AREA
nempresa = tk.Text(janela,width = 15, height= 1).place(x=53,y=50)#colocar os labels como ghost text dentro do text area
idencnpj =  tk.Text(janela,width = 15,height=1).place(x=53,y=90)
endereco =  tk.Text(janela,width = 15,height=1).place(x=53,y=130)
email =  tk.Text(janela,width = 15,height=1).place(x=53,y=170)
senha =  tk.Text(janela,width = 15,height=1).place(x=53,y=210)

#BUTTONS
tk.Button(janela,text = "Cadastrar-se").place(x=53,y=230)


#FUNCTIONS
def pegardados():
    nomempresa = chr
nomempresa = nempresa.get(),

janela.mainloop()
































