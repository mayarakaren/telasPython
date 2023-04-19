from tkinter import *
tela = Tk()
tela.title("Login")


#Configuração do tamanho da tela
tela.geometry("900x550")

#Configuração tela central
tela.resizable(True,True)

#Configuração da cor da tela
tela.configure(background='#ffffff')

#dimensoes da janela
largura = 900
altura = 550

#Centralizar a tela
largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Logo
ImageLogo = PhotoImage(file = r"img\logo.png")
logoLabel = Label(bg = "#FFF", image = ImageLogo, compound = "top")
logoLabel.grid(column = 0, row = 0, padx = 60, pady=60)

#Botões
btn_cadastrarcliente = Button(tela, width=25, height=15, text= 'Cadastrar Clientes \n ou Pets', bg="#85D3FF").place(x=60,y=250)

btn_agendarservico = Button(tela, width=25, height=15, text= 'Agende um serviço \n para o Pet', bg="#85D3FF").place(x=260,y=250)

btn_cadastrarservico = Button(tela, width=25, height=15, text= 'Cadastre aqui os serviços \n disponíveis', bg="#85D3FF").place(x=460,y=250)

btn_excluir = Button(tela, width=25, height=15, text= 'Edite ou exclua o cadastro \n do cliente', bg="#85D3FF").place(x=660,y=250)

tela.mainloop()

