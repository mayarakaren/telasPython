from tkinter import *
import subprocess

tela = Tk()
tela.title("Petz")

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela.geometry("750x500")
tela.resizable(True,True)
tela.configure(background='#ffffff')
largura = 700
altura = 600

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Abrir telas-----------------------------------------------------------------------------------------------------

def abrir_tela_clientes():
    subprocess.run(["python", "telaCadDono.py"])

def abrir_tela_animais():
    subprocess.run(["python", "telaCadAnimal.py"])

def abrir_tela_servico():
    subprocess.run(["python", "telaServico.py"])

tela.title("Petz")

#Menu-----------------------------------------------------------------------------------------------------

barra_menus = Menu(tela)
opcoes_menus_cliente = Menu(barra_menus)
opcoes_menus_animal = Menu(barra_menus)
opcoes_menus_servicos = Menu(barra_menus)

barra_menus.add_cascade(label="Cadastrar Cliente", menu=opcoes_menus_cliente)
barra_menus.add_cascade(label="Cadastrar Animal", menu=opcoes_menus_animal)
barra_menus.add_cascade(label="Serviços", menu=opcoes_menus_servicos)

opcoes_menus_cliente.add_command(label="Abrir", command=abrir_tela_clientes)
opcoes_menus_cliente.add_separator()
opcoes_menus_cliente.add_command(label="Sair", command=tela.quit)

opcoes_menus_animal.add_command(label="Abrir", command=abrir_tela_animais)
opcoes_menus_animal.add_separator()
opcoes_menus_animal.add_command(label="Sair", command=tela.quit)

opcoes_menus_servicos.add_command(label="Abrir", command=abrir_tela_servico)
opcoes_menus_servicos.add_separator()
opcoes_menus_servicos.add_command(label="Sair", command=tela.quit)

tela.config(menu=barra_menus)


#Logo-------------------------------------------------------------------------------------------------------------
ImageLogo = PhotoImage(file = r"img\logo.png")
logoLabel = Label(bg = "#FFF", image = ImageLogo, compound = "top")
logoLabel.grid(column = 0, row = 0, padx = 60, pady=60)

#Botões-----------------------------------------------------------------------------------------------------

btn_cadastrarcliente = Button(tela, width=25, height=15, text= 'Cadastrar Clientes', bg="#f9e6b3", command=abrir_tela_clientes).place(x=60,y=250)
btn_cadastrarAnimal = Button(tela, width=25, height=15, text= 'Cadastrar Animal', bg="#f9e6b3", command=abrir_tela_animais).place(x=260,y=250)
btn_cadastrarservico = Button(tela, width=25, height=15, text= 'Cadastro de serviços', bg="#f9e6b3", command=abrir_tela_servico).place(x=460,y=250)


tela.mainloop()