from tkinter import ttk


def default_style():
    style = ttk.Style()
    style.configure('back.TFrame', background='#382933')
    style.configure('title.TLabel', font=('Tahoma', 11, 'bold'), background='#3b5249', foreground='#a4b494', width=81,
                    borderwidth=3, relief='ridge', anchor=8)
    style.configure('new.TEntry', foreground='#a4b494')
    style.configure('new.TLabel', font=('Tahoma', 8, 'bold'), background='#382933', foreground='#a4b494')
    style.configure('new.TButton', foreground='#a4b494')
    style.configure('exit.TButton', foreground='#382933')


def violent_style():
    style = ttk.Style()
    style.configure('back.TFrame', background='#181426')
    style.configure('title.TLabel', font=('Verdana', 11, 'bold'), background='#ab990e', foreground='#181426', width=73,
                    borderwidth=3, relief='ridge', anchor=8)
    style.configure('new.TEntry', foreground='#181426')
    style.configure('new.TLabel', font=('Verdana', 8, 'bold'), background='#181426', foreground='red')
    style.configure('new.TButton', foreground='#ab990e')
    style.configure('exit.TButton', foreground='red')


def kimbie_style():
    style = ttk.Style()
    style.configure('back.TFrame', background='#002b36')
    style.configure('title.TLabel', font=('Verdana', 11, 'bold'), background='#0b4352', foreground='#993506', width=73,
                    borderwidth=3, relief='ridge', anchor=8)
    style.configure('new.TEntry', foreground='#993506')
    style.configure('new.TLabel', font=('Verdana', 8, 'bold'), background='#002b36', foreground='#993506')
    style.configure('new.TButton', foreground='#032e2e')
    style.configure('exit.TButton', foreground='#993506')


def quiet_style():
    style = ttk.Style()
    style.configure('back.TFrame', background='#baadba')
    style.configure('title.TLabel', font=('Tahoma', 11, 'bold'), background='#786d78', foreground='black', width=81,
                    borderwidth=3, relief='ridge', anchor=8)
    style.configure('new.TEntry', foreground='black')
    style.configure('new.TLabel', font=('Tahoma', 8, 'bold'), background='#baadba', foreground='black')
    style.configure('new.TButton', foreground='White')
    style.configure('exit.TButton', foreground='White')
