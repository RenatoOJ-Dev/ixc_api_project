import tkinter as tk

from paramiko import config


def mudar_texto_header():
    root.config

root = tk.Tk()
root.geometry('1000x500')
root.title('minha first screen')

label_header = tk.Label(root, text='Aqui tem um texto')
label_header.pack()

if __name__ == '__main__':
    root.mainloop()
