from tkinter import *
import subprocess

janela = Tk()
janela.title("Petz")

#Configuração da tela-----------------------------------------------------------------------------------------------------

janela.geometry("750x500")
janela.resizable(True,True)
janela.configure(background='#ffffff')
largura = 700
altura = 600

largura_screen= janela.winfo_screenwidth()
altura_screen= janela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Abrir telas-----------------------------------------------------------------------------------------------------

def abrir_tela_clientes():
    subprocess.run(["python", "telaCadDono.py"])

def abrir_tela_animais():
    subprocess.run(["python", "telaCadAnimal.py"])

def abrir_tela_servico():
    subprocess.run(["python", "telaServico.py"])

janela.title("Petz")


#Logo-------------------------------------------------------------------------------------------------------------
ImageLogo = PhotoImage(file = r"img\logo.png")
logoLabel = Label(bg = "#FFF", image = ImageLogo, compound = "top")
logoLabel.grid(column = 0, row = 0, padx = 60, pady=60)

#Botões-----------------------------------------------------------------------------------------------------

btn_cadastrarcliente = Button(janela, width=15, height=10, text= 'Cadastrar Clientes', fg="white", bg="#6495ED", font=("Arial", 14, "bold"), pady=2, command=abrir_tela_clientes).place(x=60,y=250)
btn_cadastrarAnimal = Button(janela, width=15, height=10, text= 'Cadastrar Animal', fg="white", bg="#6495ED", font=("Arial", 14, "bold"), command=abrir_tela_animais).place(x=260,y=250)
btn_cadastrarservico = Button(janela, width=15, height=10, text= 'Serviços', fg="white", bg="#6495ED", font=("Arial", 14, "bold"), command=abrir_tela_servico).place(x=460,y=250)


janela.mainloop()