from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela = Tk()
tela.title("Gestão de Animais")
var = StringVar()
var.set("M")

tela.geometry("750x500")
tela.resizable(True, True)
tela.configure(background="#ffffff")
largura = 700
altura = 500

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#Título-----------------------------------------------------------------------------------------------------
lbl_tit = Label(tela, text="Gestão de Donos", font=("Arial", 30, "bold")).place(x=200, y=50)

#Código-----------------------------------------------------------------------------------------------------
lbl_codigo = Label(tela, text="Código:").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)
txt_codigo.insert(0, "Código")

#Nome-----------------------------------------------------------------------------------------------------
lbl_nome = Label(tela, text="Nome:").place(x=130, y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "Digite o nome")

#Idade-----------------------------------------------------------------------------------------------------
lbl_idade = Label(tela, text="Idade:").place(x=480, y=170)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=520, y=170)
txt_idade.insert(0, "Idade")

#Sexo-----------------------------------------------------------------------------------------------------
Label(tela, text="Sexo:").place(x=130, y=200)

sexo = StringVar()
sexo.set("m")

rdb_buttonm = Radiobutton(tela, text="M", variable="var", value="m")
rdb_buttonf = Radiobutton(tela, text="F", variable="var", value="f")
rdb_buttonm.place(x=165 , y=200)
rdb_buttonf.place(x=200 , y=200)

#Raça-----------------------------------------------------------------------------------------------------

lbl_raca = Label(tela, text="Raça:").place(x=250, y=200)
txt_raca = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_raca.place(x=290, y=200)
txt_raca.insert(0, "Não Definido")

#Peso-----------------------------------------------------------------------------------------------------

lbl_peso = Label(tela, text="Peso:").place(x=420, y=200)
txt_peso = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_peso.place(x=460, y=200)
txt_peso.insert(0, "Kg")

#Espécie-----------------------------------------------------------------------------------------------------

lbl_especie = Label(tela, text="Espécie:").place(x=130, y=230)
comboEspecie = ttk.Combobox(tela, 
                            values=[
                                    "Cachorro", 
                                    "Gato",
                                    "Passáro",
                                    "Roedores"],)

comboEspecie.grid(column=0, row=1)
comboEspecie.place(x=180 , y=230)

#Data de nascimento-----------------------------------------------------------------------------------------------------

lbl_data = Label(tela, text="Data de nascimento:").place(x=330, y=230)
txt_data = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_data.place(x=450, y=230)
txt_data.insert(0, "Data")

#Data de Cadastro-----------------------------------------------------------------------------------------------------

lbl_cad = Label(tela, text="Data de cadastro:").place(x=130, y=260)
txt_cad = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cad.place(x=230, y=260)
txt_cad.insert(0, "Data")

#Data de Atulização-----------------------------------------------------------------------------------------------------

lbl_at = Label(tela, text="Data de atulização:").place(x=380, y=260)
txt_at = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_at.place(x=490, y=260)
txt_at.insert(0, "Data")

#Descrição-----------------------------------------------------------------------------------------------------

lbl_desc = Label(tela, text="Descrição:").place(x=130, y=290)
text_area = tk.Text(tela, height=5, width=50, font=('Arial', 12),
                    fg='black', bg='white')
text_area.pack()
text_area.place(x=200, y=290)

#Imagem-----------------------------------------------------------------------------------------------------

pasta_inicial = PhotoImage(file = r"")

def escolher_imagem():

    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg; *.jpeg; *.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
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