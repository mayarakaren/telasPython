from tkinter import *
import tkinter as tk
import bcrypt
from tkinter import messagebox
import subprocess

tela = Tk()
tela.title("Petz")

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela.geometry("750x500")
tela.resizable(True,True)
tela.configure(background='#ffffff')
largura = 300
altura = 120

largura_screen= tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()

posx=largura_screen/2 - largura/2
posy=altura_screen/2 - altura/2

tela.geometry("%dx%d+%d+%d"%(largura, altura, posx, posy))

#-----------------------------------------------------------------------------------------------------------------------------

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['petshop']
collection = db['usuarios']


lbl_user = Label(tela, text="Usuário:", bg="#ffffff").place(x=10, y=10)
txt_user = Entry(tela, width=35, borderwidth=3)
txt_user.place(x=60, y=10)
txt_user.insert(0, "")

lbl_password = Label(tela, text="Senha:", bg="#ffffff").place(x=10, y=40)
txt_password = Entry(tela)
txt_password = tk.Entry(tela, show="*", width=35, borderwidth=3)
txt_password.place(x=60, y=40)
txt_password.insert(0, "")


def cadastro():
    username = txt_user.get()
    password = txt_password.get()

    hash_senha = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    usuarios = {"usuário": username, "senha":hash_senha}
    collection.insert_one(usuarios)

    messagebox.showinfo('Cadastro','Cadastro bem-sucedido')
    tela.destroy()

def abrir_tela_principal():
    subprocess.run(["python", "telaPrincipal.py"])

def login():
    username = txt_user.get()
    password = txt_password.get().encode('utf-8')

    colecao_user = db['usuarios']
    usuario_encontrado = colecao_user.find_one({"usuário": username})

    if usuario_encontrado:
        hash_senha = usuario_encontrado['senha']
        if bcrypt.checkpw(password, hash_senha):
            messagebox.showinfo('Login','Login bem-sucedido')
            tela.destroy() # Fecha a tela de login
            abrir_tela_principal() # Abre a outra tela da aplicação
        else:
            messagebox.showinfo('Login','Login ou Senha incorreta')
            tela.destroy()
    else:
        messagebox.showinfo('Login', 'Usuário não encontrado!')
        tela.destroy()

login_button = Button(tela, text="Login", bg="#6495ED")
login_button.place(x=180, y=80)
login_button.config(command=login)

cad_button = Button(tela, text="Cadastrar", bg="#6495ED")
cad_button.place(x=80, y=80)
cad_button.config(command=cadastro)


tela.mainloop()