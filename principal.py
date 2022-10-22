from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError

janela = Tk()
janela.title('Baixando videos do youtube')


def dowload(link_):
    if link_:
        try:
            pasta = filedialog.askdirectory()
            YouTube(link_).streams.get_highest_resolution().download(pasta)
            aviso()
        except RegexMatchError:
            aviso_erro()
    else:
        aviso_erro()


def aviso():
    janela_msg = Toplevel()
    janela_msg.title('Aviso')
    janela_msg.geometry('300x200')

    Label(janela_msg, text='Dowload concluido', font='arial 12 bold', pady=30).pack()

    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()


def aviso_erro():
    janela_msg = Toplevel()
    janela_msg.title('Aviso')
    janela_msg.geometry('300x200')

    Label(janela_msg, text='Insira um link válido', font='arial 12 bold', pady=30).pack()

    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()


quadro = Frame(janela)
quadro.pack()

Label(quadro, text='Inserir link: ', font='arial 12 bold').pack(side='left')
link = Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

Button(quadro, bg='green', text='>>>', bd=1, fg='white', width=4, height=2, command=lambda: dowload(link.get())).pack()
janela.mainloop()
