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
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    tipo = comboservico.get()
    valor = txt_valor.get()
    tempo = txt_tempo.get()
    desc = text_area.get("1.0", END)

    servicos = {"código": codigo, "nome": nome, "serviço": tipo, "valor": valor, "tempo de duração": tempo, "descrição": desc}
    collection.insert_one(servicos)

def read():
    servico = []
    for servicos in collection.find():
        servico.append(servicos)
    print(servicos)

def update():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    tipo = comboservico.get()
    valor = txt_valor.get()
    tempo = txt_tempo.get()
    desc = text_area.get("1.0", END)

    collection.update_one({"código":codigo}, {"$set": {"código": codigo, "nome": nome, "serviço": tipo, "valor": valor, "tempo de duração": tempo, "descrição": desc}})

def delete():
    codigo = txt_codigo.get()
    collection.delete_one({"código": codigo})


#Código-----------------------------------------------------------------------------------------------------
lbl_codigo = Label(tela, text="Código:", bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)
txt_codigo.insert(0, "Código")

#Nome-----------------------------------------------------------------------------------------------------
lbl_nome = Label(tela, text="Nome:", bg="#ffffff").place(x=130, y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "Digite o nome")

#Serviços estéticos: banhos, hidratação, tosa na máquina, tosa na tesoura, tosa higiênica, desembaraçamento, tingimento #dos pelos, escovação de dentes, limpeza de ouvido e corte de unhas.
#Bem estar: dog walker/passeador, prática de esportes guiada como natação e corridas, ioga, acupuntura e fitoterápicos 
#(sessões de relaxamento).
#Serviços Médicos: consultas clínicas gerais e especialidades, atendimento domiciliar, vacinação, preventivos e cirurgias.
#Educação: adestramento e hospedagem (aprendizagem de convívio com outros animais).

#Tipo de Serviço-----------------------------------------------------------------------------------------------------

lbl_servico = Label(tela, text="Tipo:", bg="#ffffff").place(x=130, y=200)
comboservico = ttk.Combobox(tela, 
                            values=[
                                    "Serviços Estéticos", 
                                    "Bem-Estar",
                                    "Serviços Médicos",
                                    "Educação"],)

comboservico.grid(column=0, row=1)
comboservico.place(x=190 , y=200)

#Valor-----------------------------------------------------------------------------------------------------
lbl_valor = Label(tela, text="Valor:", bg="#ffffff").place(x=130, y=230)
txt_valor = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_valor.place(x=190, y=230)
txt_valor.insert(0, "valor")

#Tempo de duração-----------------------------------------------------------------------------------------------------
lbl_tempo = Label(tela, text="Tempo de Duração:", bg="#ffffff").place(x=130, y=260)
txt_tempo = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_tempo.place(x=240, y=260)
txt_tempo.insert(0, "")

#Descrição-----------------------------------------------------------------------------------------------------

lbl_desc = Label(tela, text="Descrição:", bg="#ffffff").place(x=130, y=290)
text_area = tk.Text(tela, height=5, width=45, font=('Arial', 12),
                    fg='black', bg='white')
text_area.pack()
text_area.place(x=190, y=290)

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
btn_consultar = Button(tela, text="Consultar", image= foto_consultar, compound= TOP, bg="#F0E68C", command=read).place(x=270, y=410)
btn_excluir = Button(tela, text="Excluir", image= foto_excluir, compound= TOP, bg="#FF6347", command=delete).place(x=340, y=410)
btn_sair = Button(tela, text="Sair", image= foto_sair, compound= RIGHT, bg="#000000", fg="white", height=40, width=70, anchor="center", command=tela.quit).place(x=620, y=440)

tela.mainloop()