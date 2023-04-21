from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import pymongo
import io

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela = Tk()
tela.title("Gestão de Serviços")

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
lbl_tit = Label(tela, text="Gestão de Serviços", font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)

# Conectando com o banco de dados----------------------------------------------------------------------------
petshop = pymongo.MongoClient("mongodb://localhost:27017/")
db = petshop["petshop"]
collection = db["servicos"]

# Criando as funções do CRUD
def create():


    servicos = {}
    collection.insert_one(servicos)

def read():
    servico = []
    for servicos in collection.find():
        servico.append(servicos)
    print(servicos)

def update():

    collection.update_one({"código":codigo}, {"$set": {}})

def delete():
    codigo = txt_codigo.get()
    collection.delete_one({"código": codigo})

#Ícones-----------------------------------------------------------------------------------------------------

foto_salvar = PhotoImage(file=r"img\save.png")
foto_excluir = PhotoImage(file=r"img\delete.png")
foto_alterar = PhotoImage(file=r"img\edit.png")
foto_consultar = PhotoImage(file=r"img\search.png")
foto_sair = PhotoImage(file=r"img\logout.png")

#Botões-----------------------------------------------------------------------------------------------------

btn_salvar = Button(tela, text="Salvar", image= foto_salvar, compound= TOP, bg="#90EE90",command=create).place(x=130, y=410)
btn_alterar = Button(tela, text="Alterar", image= foto_alterar, compound= TOP, bg="#6495ED", command=update).place(x=200, y=410)
btn_consultar = Button(tela, text="Consultar", image= foto_consultar, compound= TOP, bg="#F0E68C", command=read).place(x=270, y=410)
btn_excluir = Button(tela, text="Excluir", image= foto_excluir, compound= TOP, bg="#FF6347", command=delete).place(x=340, y=410)
btn_sair = Button(tela, text="Sair", image= foto_sair, compound= RIGHT, bg="#000000", fg="white", height=40, width=70, anchor="center", command=tela.quit).place(x=620, y=440)

tela.mainloop()