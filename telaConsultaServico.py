from tkinter import *

import tkinter as tk
from pymongo import MongoClient
import pandas 


#Configuração da tela-----------------------------------------------------------------------------------------------------

tela = Tk()
tela.title("Consulta")

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

#Consulta-------------------------------------------------------------------------------------------------------------------


client = MongoClient('mongodb://localhost:27017/')
db = client['petshop']
collection = db['servico']
data = collection.find()

def consultar_servico():
    listbox = tk.Listbox(tela)
    listbox.pack(fill=tk.BOTH, expand=True)

    for item in data:
        listbox.insert(tk.END, item)

    df = pandas.DataFrame(list(data))
    table = tk.Frame(tela)
    table.pack(fill=tk.BOTH, expand=True)
    for i, col in enumerate(df.columns):
        tk.Label(table, text=col).grid(row=0, column=i)
    for i, row in df.iterrows():
        for j, val in enumerate(row):
            tk.Label(table, text=val).grid(row=i+1, column=j)

lbl_consultar = Label(tela, text="Consultar:", bg="#ffffff").place(x=10, y=10)
txt_consultar = Entry(tela, width=80, borderwidth=2, fg="black", bg="white")
txt_consultar.place(x=70, y=10)
txt_consultar.insert(0, "")

#Botões-----------------------------------------------------------------------------------------------------

btn_servico = Button(tela, text="Consultar Serviços", command=consultar_servico, bg="#90EE90")
btn_servico.place(x=570, y=10)

tela.mainloop()