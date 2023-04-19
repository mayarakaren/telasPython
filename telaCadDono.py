from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela = Tk()
tela.title("Gestão dos Donos")
var = StringVar()
var.set("M")

tela.geometry("750x500")
tela.resizable(True, True)
tela.configure(background="#ffffff")
largura = 700
altura = 600

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Código-----------------------------------------------------------------------------------------------------
lbl_codigo = Label(tela, text="Código:").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)
txt_codigo.insert(0, "Código")

#Nome-----------------------------------------------------------------------------------------------------
lbl_nome = Label(tela, text="Nome:").place(x=130, y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "Nome do Dono")

#Idade-----------------------------------------------------------------------------------------------------
lbl_idade = Label(tela, text="Idade:").place(x=480, y=170)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=520, y=170)
txt_idade.insert(0, "Idade")

#Sexo-----------------------------------------------------------------------------------------------------
Label(tela, text="Sexo:").place(x=130, y=200)

sexo = StringVar()
sexo.set("M")

rdb_buttonm = Radiobutton(tela, text="M", variable="var", value="m")
rdb_buttonf = Radiobutton(tela, text="F", variable="var", value="f")
rdb_buttonm.place(x=165 , y=200)
rdb_buttonf.place(x=200 , y=200)


#Imagem-----------------------------------------------------------------------------------------------------

pasta_inicial = PhotoImage(file = r"")

def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg; *.jepg; *.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, imagem=imagem_tk)
    lbl_imagem.image= imagem_tk
    lbl_imagem.place(x=10, y=50)

#Botões-----------------------------------------------------------------------------------------------------

btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=200)

#Ícones-----------------------------------------------------------------------------------------------------

foto_salvar = PhotoImage(file=r"img\save.png")
foto_excluir = PhotoImage(file=r"img\delete.png")
foto_alterar = PhotoImage(file=r"img\edit.png")
foto_consultar = PhotoImage(file=r"img\search.png")
foto_sair = PhotoImage(file=r"img\logout.png")

#Botões-----------------------------------------------------------------------------------------------------

btn_salvar = Button(tela, text="Salvar", image= foto_salvar, compound= TOP).place(x=130, y=410)
btn_excluir = Button(tela, text="Excluir", image= foto_excluir, compound= TOP).place(x=200, y=410)
btn_alterar = Button(tela, text="Alterar", image= foto_alterar, compound= TOP).place(x=270, y=410)
btn_consultar = Button(tela, text="Consultar", image= foto_consultar, compound= TOP).place(x=340, y=410)
btn_sair = Button(tela, text="Sair", image= foto_sair, compound= RIGHT).place(x=620, y=440)

tela.mainloop()