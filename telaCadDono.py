from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import pymongo
import io
import subprocess

#Configuração da tela-----------------------------------------------------------------------------------------------------

tela = Tk()
tela.title("Gestão dos Donos")

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
lbl_tit = Label(tela, text="Gestão de Donos", font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)

#Código-----------------------------------------------------------------------------------------------------
lbl_codigo = Label(tela, text="Código:", bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)
txt_codigo.insert(0, "Código")

#Celular-----------------------------------------------------------------------------------------------------

lbl_cel = Label(tela, text="Celular:", bg="#ffffff").place(x=370, y=140)
txt_cel = Entry(tela, width=25, borderwidth=2, fg="black", bg="white")
txt_cel.place(x=420, y=140)
txt_cel.insert(0, " ")


#Nome-----------------------------------------------------------------------------------------------------
lbl_nome = Label(tela, text="Nome:", bg="#ffffff").place(x=130, y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "Digite o nome")

#CPF-----------------------------------------------------------------------------------------------------
lbl_cpf = Label(tela, text="CPF:", bg="#ffffff").place(x=450, y=170)
txt_cpf = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cpf.place(x=480, y=170)
txt_cpf.insert(0, "")

#Sexo-----------------------------------------------------------------------------------------------------
Label(tela, text="Sexo:", bg="#ffffff").place(x=130, y=200)

sexo = StringVar()
sexo.set("m")

rdb_buttonm = Radiobutton(tela, text="M", variable="var", value="m", bg="#ffffff")
rdb_buttonf = Radiobutton(tela, text="F", variable="var", value="f", bg="#ffffff")
rdb_buttonm.place(x=165 , y=200)
rdb_buttonf.place(x=200 , y=200)

#Idade-----------------------------------------------------------------------------------------------------

lbl_idade = Label(tela, text="Idade:", bg="#ffffff").place(x=250, y=200)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=290, y=200)
txt_idade.insert(0, "")

#Endereço-----------------------------------------------------------------------------------------------------

lbl_end = Label(tela, text="Endereço:", bg="#ffffff").place(x=420, y=200)
txt_end = Entry(tela, width=25, borderwidth=2, fg="black", bg="white")
txt_end.place(x=480, y=200)
txt_end.insert(0, "")

#Estado-----------------------------------------------------------------------------------------------------

lbl_estado = Label(tela, text="Estado:", bg="#ffffff").place(x=130, y=230)
comboestado = ttk.Combobox(tela, 
                            values=[
                                    "São Paulo", 
                                    "Rio de Janeiro",
                                    "Minas Gerais",
                                    "Espírito Santo"],)

comboestado.grid(column=0, row=1)
comboestado.place(x=180 , y=230)

#Bairro-----------------------------------------------------------------------------------------------------

lbl_bairro = Label(tela, text="Bairro:", bg="#ffffff").place(x= 330, y= 230)
txt_bairro = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_bairro.place(x= 370, y=230)
txt_bairro.insert(0, " ")

#Cidade-----------------------------------------------------------------------------------------------------

lbl_cidade = Label(tela, text="Cidade:", bg="#ffffff").place(x= 500, y= 230)
txt_cidade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cidade.place(x= 550, y=230)
txt_cidade.insert(0, " ")

#Data de nascimento-----------------------------------------------------------------------------------------------------

lbl_data = Label(tela, text="Data de nascimento:", bg="#ffffff").place(x=380, y=260)
txt_data = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_data.place(x=500, y=260)
txt_data.insert(0, "Data")

#Data de Cadastro-----------------------------------------------------------------------------------------------------

lbl_cad = Label(tela, text="Data de cadastro:", bg="#ffffff").place(x=130, y=260)
txt_cad = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cad.place(x=230, y=260)
txt_cad.insert(0, "Data")


#Descrição-----------------------------------------------------------------------------------------------------

lbl_desc = Label(tela, text="Info. Adicionais:", bg="#ffffff").place(x=130, y=290)
text_area = tk.Text(tela, height=5, width=45, font=('Arial', 12),
                    fg='black', bg='white')
text_area.pack()
text_area.place(x=230, y=290)

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

    imagem_byte_arr = io.BytesIO()
    imagem_pil.save(imagem_byte_arr, format='JPEG')
    imagem_byte_arr = imagem_byte_arr.getvalue()
    collection.insert_one({"image": imagem_byte_arr})

#Banco-----------------------------------------------------------------------------------------------------

# Conectando com o banco de dados
petshop = pymongo.MongoClient("mongodb://localhost:27017/")
db = petshop["petshop"]
collection = db["clientes"]

# Criando as funções do CRUD
def create():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    sexy = sexo.get()
    celular = txt_cel.get()
    end = txt_end.get()
    cpf = txt_cpf.get()
    data = txt_data.get()
    cad = txt_cad.get() 
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()
    desc = text_area.get("1.0", END)

    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_cel.delete(0, tk.END)
    txt_end.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    comboestado.set("")
    txt_data.delete(0, tk.END)
    txt_cad.delete(0, tk.END)
    txt_cpf.delete(0, tk.END)
    text_area.delete('1.0', tk.END)
    sexo.set("")

    cliente = {"código":codigo, "nome": nome, "idade":idade, "sexo": sexy, "celular": celular, "endereço": end, "cpf":cpf, "data_nasc":data, "data_cad":cad, "bairro":bairro, "cidade":cidade, "estado": estado, "descrição": desc}
    collection.insert_one(cliente)

def read():
    clientes = []
    for cliente in collection.find():
        clientes.append(cliente)
    print(clientes)

def update():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    sexy = sexo.get()
    celular = txt_cel.get()
    end = txt_end.get()
    cpf = txt_cpf.get()
    data = txt_data.get()
    cad = txt_cad.get() 
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()
    desc = text_area.get()
    collection.update_one({"código":codigo}, {"$set": {"código":codigo, "nome": nome, "idade":idade, "sexo": sexy, "celular": celular, "endereço": end, "cpf":cpf, "data_nasc":data, "data_cad":cad, "bairro":bairro, "cidade":cidade, "estado": estado, "descrição": desc}})

def delete():
    codigo = txt_codigo.get()
    collection.delete_one({"código": codigo})

def abrir_consultaCliente():
    subprocess.run(["python", "telaConsulta.py"])


#Botões-----------------------------------------------------------------------------------------------------

btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem, bg="#90EE90")
btn_escolher.place(x=10, y=200)

#Ícones-----------------------------------------------------------------------------------------------------

foto_salvar = PhotoImage(file=r"img\save.png")
foto_excluir = PhotoImage(file=r"img\delete.png")
foto_alterar = PhotoImage(file=r"img\edit.png")
foto_consultar = PhotoImage(file=r"img\search.png")
foto_sair = PhotoImage(file=r"img\logout.png")

#Botões-----------------------------------------------------------------------------------------------------

btn_salvar = Button(tela, text="Salvar", image= foto_salvar, compound= TOP, bg="#90EE90",command=create).place(x=130, y=410)
btn_alterar = Button(tela, text="Alterar", image= foto_alterar, compound= TOP, bg="#6495ED", command=update).place(x=200, y=410)
btn_consultar = Button(tela, text="Consultar", image= foto_consultar, compound= TOP, bg="#F0E68C", command=abrir_consultaCliente).place(x=270, y=410)
btn_excluir = Button(tela, text="Excluir", image= foto_excluir, compound= TOP, bg="#FF6347", command=delete).place(x=340, y=410)
btn_sair = Button(tela, text="Sair", image= foto_sair, compound= RIGHT, bg="#000000", fg="white", height=40, width=70, anchor="center", command=tela.quit).place(x=620, y=440)

tela.mainloop()