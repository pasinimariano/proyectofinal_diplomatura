from tkinter import Radiobutton
from ttkthemes import *
from themes.styles import *


class ChoiceTheme:
    """            Clase encargada de crear el commando del boton "themes". Esta clase
        abrira una ventana emergente donde apareceran los nombres de los temas a elegir. Utilizando
        "Radiobuttons", la App viene configurada por el estilo= "default_style".
                Los commands se crean en un modulo separado, para poder configurar los diferentes
        temas de manera sencilla, y asi poder incorporar todos los temas que se deseen. Estas
        funciones (cuyo nombre coincide con el nombre del estilo), seran las encargadas de cambiar
        los colores, las fuentes, los tamaños, etc., de la App.
                Dentro de cada funcion se crea la variable "style" que toma como atributo la galeria
        "ttk.Style". Gracias a ello solo con un ".configure" y darle un nombre a eleccion, se podra
        configurar todas las caracteristicas deseadas del widget seleccionado.
                Hay que tener en cuenta que para crear un nombre de estilo hay que respetar cierta estructura,
        la cual es: -"*****.?????". Los "*****" seran reemplazados por un nombre a elección (para poder crear
        diferentes estilos), en cambio los "?????" seran reemplazados de manera estricta con los nombres
        correspondies al widget que se desea configurar: TLabel, TEntry, TButton, TFrame; una T mayuscula
        proventiente de la galaeria Ttk, seguido por el nombre del widget a modificar (comenzando por una mayuscula).
                Algo muy importante es que para que esto funcione, se debe importar dentro del modulo de creacion del
        widget la libreria ttk y ttkthemes. Asimismo, al crear el widget debe ser creado anteponiendo las siglas ttk.
        Como por ejemplo ttk.Label, si por el contrario se realiza el llamado Label sin anteponer las siglas, el 
        estilo no se tomara, y quedaran configuradas por defecto."""

    def __init__(self, ):
        self.window = ThemedTk(theme='equilux')
        self.window.geometry('220x180')
        self.window.resizable(0, 0)
        self.window.configure(bg='grey22')
        self.window.title('Themes')

        self.default = Radiobutton(self.window, bg='grey22', text='          Default Style', font=('Tahoma', 8, 'bold'),
                                   fg='#a4b494', command=lambda: (default_style()))
        self.default.place(x=15, y=5)

        self.violent = Radiobutton(self.window, bg='grey22', text='          Violent Contrast',
                                   font=('Tahoma', 8, 'bold'),
                                   fg='#a4b494', command=lambda: (violent_style()))
        self.violent.place(x=15, y=35)

        self.kimbie = Radiobutton(self.window, bg='grey22', text='          Kimbie', font=('Tahoma', 8, 'bold'),
                                  fg='#a4b494', command=lambda: (kimbie_style()))
        self.kimbie.place(x=15, y=65)

        self.quiet = Radiobutton(self.window, bg='grey22', text='          Quiet', font=('Tahoma', 8, 'bold'),
                                 fg='#a4b494', command=lambda: (quiet_style()))
        self.quiet.place(x=15, y=95)

        self.quit_button = ttk.Button(self.window, text='Aceptar', command=self.window.destroy)
        self.quit_button.place(x=110, y=135, width=70)
