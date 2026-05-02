import tkinter as tk

COLOR_BG = 'lightblue4'


def get_text():
    top = tk.Toplevel(root)
    top.title('Text')

    message = """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Commodi, ea? Repellendus, vitae error, delectus voluptatum ab minus voluptatem 
    quo atque eligendi consectetur ex cumque qui inventore reiciendis sequi suscipit in."""
    toplabel = tk.Label(top, text=message)
    toplabel.pack()
    top.mainloop()


def set_theme_light():
    root.config(bg='lightblue4')
    label1.config(bg='lightblue4')


def set_theme_dark():
    root.config(bg='dimgray')
    label1.config(bg='dimgray')


# COLOR_GREEN
root = tk.Tk()
menu = tk.Menu(root)
scroll_bar = tk.Scrollbar(root)

scroll_bar.pack()
mylist = tk.Listbox(root, yscrollcommand=scroll_bar.set)
mylist.pack(side='bottom', fill='both')

scroll_bar.config(command=mylist.yview)

theme = tk.Menu(menu)
menu.add_cascade(label='Theme', menu=theme)
theme.add_command(label='Light', command=set_theme_light)
theme.add_command(label='Dark', command=set_theme_dark)


root.config(menu=menu)
root.config(bg=COLOR_BG)
root.title('meu gui')
root.geometry('500x500')

label1 = tk.Label(root, text='', bg=COLOR_BG)


button1 = tk.Button(root, text='PEGAR TEXTO', command=get_text, activebackground='limegreen', border=False, borderwidth=False)
button1.pack(padx=10, pady=10)
label1.pack()
root.mainloop()
