from tkinter import *

janelinha = Tk()
janelinha.geometry('200x200+800+260')
janelinha.config(background='#B0C4DE')


def soma():
    if caixinha1.get().isnumeric() and caixinha2.get().isnumeric():
        textinho['text'] = float(caixinha1.get()) + float(caixinha2.get())
    else:
        textinho['text'] = 'Valor invalido!'


textinho = Label(janelinha, text='O resultadinho é!', bg='#B0C4DE')
caixinha1 = Entry(janelinha)
caixinha2 = Entry(janelinha)
btzinho = Button(janelinha, text='Sominha', bg='#7FFFD4', command=soma)

textinho.pack()
caixinha1.pack()
caixinha2.pack()
btzinho.pack()

janelinha.mainloop()
