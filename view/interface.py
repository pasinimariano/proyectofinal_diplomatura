from tkinter import ttk
from tkinter import messagebox
import themes.choice


class Interface:

    """            Clase padre, donde se generan todos los elementos del layout.
    El constructor de la clase, genera la variable del root principal (el cual
    fue heredado por el Tk master en el modulo "main"). Luego llama al estilo
    por default que tendra la aplicación desde el modulo "themes". Por el último 
    construira un "frame" principal donde se ubicarán todos los elementos que 
    hacen al layout (utilizando el método ".place").
        Toda la creación de la interfaz esta separada en metodos, con sus 
    respectivos nombres. Lo que facilita la detección de algún posible error a la
    hora de la creación de algun widget.  """

    def __init__(self, master=None):
        self.root = master
        themes.choice.default_style()
        self.background = ttk.Frame(self.root, width=820,
                                    height=420, style='back.TFrame')
        self.background.pack()

    def title_box(self, ):

        """            Metodo encargado de generar el título principal de la App.
        Solo se configurará el nombre a mostrar, ya que el estilo lo incorporará 
        utilizando el modulo "themes". """

        self.title = ttk.Label(self.background, text='Ingrese sus Datos',
                               style='title.TLabel')
        self.title.place(x=3, y=5)
        self.sub_title = ttk.Label(self.background, text='Registros existentes',
                                   style='title.TLabel')
        self.sub_title.place(x=3, y=105)

    def entries_box(self, ):

        """            Metodo encargado de generar los input, donde el usuario podra
        dar de alta los registros de la base de datos. Asimismo genera un focus en el
        input "Titulo". """

        self.entry_title = ttk.Entry(self.background, width=50, style='new.TEntry')
        self.entry_title.focus()
        self.entry_title.place(x=160, y=40)
        self.entry_description = ttk.Entry(self.background, width=50, style='new.TEntry')
        self.entry_description.place(x=160, y=70)
    
    def labels_box(self, ):

        """            Metodo encargado de generar los nombres de los input."""

        self.name_title = ttk.Label(self.background, text='Titulo', style='new.TLabel')
        self.name_title.place(x=40, y=45)
        self.name_description = ttk.Label(self.background, text='Descripcion', style='new.TLabel')
        self.name_description.place(x=40, y=75)
    
    def tree_box(self, ):

        """            Metodo encargado de generar la sección del Treeview en donde
        se podrán visualizar y modificar los registros de la base de datos de manera
        práctica. """
        
        self.tree = ttk.Treeview(columns=('#0', '#1', '#2', '#3', '#4', '#5'), takefocus=0)
        self.tree.column('#0', width=35)
        self.tree.column('#1', width=155)
        self.tree.column('#2', width=125)
        self.tree.column('#3', width=320)
        self.tree.column('#4', width=55)
        self.tree.column('#5', width=135)
        self.tree.heading('#0', text='Id')
        self.tree.heading('#1', text='Titulo')
        self.tree.heading('#2', text='Fecha')
        self.tree.heading('#3', text='Descripción')
        self.tree.heading('#4', text='Estado')
        self.tree.heading('#5', text='Objeto')
        self.tree.place(x=0, y=140)
    
    def buttons(self, **config):

        """            Metodo encargado de crear los botones de la App. 
        En cuanto a su configuración, se les asignará un nombre (el cual aparecerá dentro del botón), un
        ancho (width), el estilo como antes se dijo será importado del modulo "themes", y lo más importante
        de este metodo, es que se le pasa el parametro "**config**, el cual esperará que el commando de los
        botones sea configurado, si no se configura en ningún lado, los botones aparecerán en la App, pero 
        no realizarán ninguna acción.
            Estos commandos, serán configurados en el modulo "main", ya que es él quien tiene toda la estructura
        para utilizar. """

        self.button_insert = ttk.Button(self.background, text='Alta',
                                        style='new.TButton', **config)
        self.button_insert.place(x=550, y=55, width=45)
        self.button_delete = ttk.Button(self.background, text='Eliminar',
                                        style='new.TButton', **config)
        self.button_delete.place(x=610, y=55, width=70)
        self.button_update = ttk.Button(self.background, text='Modificar',
                                        style='new.TButton', **config)
        self.button_update.place(x=695, y=55, width=75)
        self.button_themes = ttk.Button(self.background, text='Themes',
                                        style='new.TButton', command=lambda: (themes.choice.ChoiceTheme()))
        self.button_themes.place(x=10, y=385, width=65)
        self.button_exit = ttk.Button(self.background, text='Salir',
                                      style='exit.TButton', command=self.exit)
        self.button_exit.place(x=745, y=385, width=65)

    def exit(self, ):

        """            Metodo sencillo encargado de crear el comando para el botón de salida de la App.
        Incorpora un popup para confirmar o cancelar la salida. """

        self.box_confirm = messagebox.askquestion('Shut Down',
                                                  '¿Esta seguro que desea cerrar la aplicacion?',
                                                  icon='warning')
        if self.box_confirm == 'yes':
            self.root.destroy()
        else:
            pass
