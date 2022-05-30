# importar a biblioteca
from tkinter import *


# back-end
def imprimir():
    label1['text'] = entry1.get()
    print(entry1.get())


# front-end
# criar a janela
janela = Tk()
janela.geometry('600x600+100+300')
janela.minsize(width=100, height=50)
janela.maxsize(width=900, height=900)
janela.config(background='#87CEEB')

# criar os widgets
label1 = Label(janela, text='Olá Mundo!', font='Arial 36 bold')
entry1 = Entry(janela, font='Arial 36')
btn1 = Button(janela, text='Sair', font='Arial 36', command=quit)
btn2 = Button(janela, text='Imprimir', font='Arial 36', command=imprimir)

# organizar os widgets
label1.pack()
entry1.pack()
btn1.pack()
btn2.pack()

# executar a janela
janela.mainloop()

