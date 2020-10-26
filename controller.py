from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedTk  # IMPORTANTE: ejecutar "pip install ttkthemes"
from sqlalchemy.exc import OperationalError
import model.sqlalquemy
import view.interface


class Controller:

    """            Modulo principal, el cual estara encargado de generar el inicio y correcto
        funcionamiento de la App. Para ello utiliza la clase 'Controller'.
        Generando el master root, con su estilo predefinido, e importando a la clase Interface, 
        generará el layout principal.
        IMPORTANTE: toda la App utiliza el paquete "ttkthemes", por lo que se debera instalar 
        previamente de una manera sencilla. Dentro del terminal ingrese el comando: "pip install ttkthemes".
        Asi mismo, importará del modulo: 'model.sqlalquemy' todos sus componentes.
        Por último configurará los commands de los botones. """

    def __init__(self, ):
        try:
            if __name__ == '__main__':
                self.master = ThemedTk(theme='equilux')
                self.master.geometry('820x420')
                self.master.title('Python Avanzado')
                self.master.resizable(0, 0)

                self.conn_db = model.sqlalquemy.CreateDb()

                self.window = view.interface.Interface(self.master)
                self.window.title_box()
                self.window.entries_box()
                self.window.labels_box()
                self.window.tree_box()
                self.window.buttons()

                self.command = model.sqlalquemy.CreateTables()
                self.command.show_records(self.window.tree)

                self.window.button_insert.config(command=lambda: (self.command_insert()))
                self.window.button_delete.config(command=lambda: (self.command_delete()))
                self.window.button_update.config(command=lambda: (self.command_update()))

                self.master.mainloop()

        except NameError as error:
            view.interface.messagebox.showerror('Fatal Error', str(error) +
                                                'Ah surgido un error inesperado,'
                                                'Por favor contacte a su técnico.')
        except OperationalError:
            messagebox.showerror('Error de conexion',
                                 'Para mostrar los datos, debe estar conectado a la base de datos. '
                                 'Intente conectarse con su servidor, y vuelva a intentar.')

    def command_insert(self, ):

        """            Incorpora los metodos 'insert_record' y 'show_record' del modulo sqlalquemy, 
        y les inserta los parametros necesarios para su correcto funcionamiento.  """

        noticia = model.sqlalquemy.ObjetoStr(self.window.entry_title.get())
        objeto_noticia = "Titulo: " + noticia.objeto
        self.command.insert_record(self.window.entry_title.get(),
                                   self.window.entry_description.get(),
                                   objeto_noticia)
        self.command.show_records(self.window.tree)
        self.delete_input()

    def command_delete(self, ):

        """            Incorpora los metodos 'delete_record' y 'show_record' del modulo sqlalquemy, 
        y les inserta los parametros necesarios para su correcto funcionamiento.  """

        self.command.delete_record(self.window.tree)
        self.command.show_records(self.window.tree)

    def command_update(self, ):

        """            Incorpora los metodos 'update_record' y 'show_record' del modulo sqlalquemy, 
        y les inserta los parametros necesarios para su correcto funcionamiento.  """

        noticia = model.sqlalquemy.ObjetoStr(self.window.entry_title.get())
        objeto_noticia = "Titulo: " + noticia.objeto
        self.command.update_record(self.window.tree,
                                   self.window.entry_title.get(),
                                   self.window.entry_description.get(),
                                   objeto_noticia)
        self.command.show_records(self.window.tree)

    def delete_input(self, ):

        """            Elimina los registros ingresados por el usuario en los entries."""

        self.window.entry_title.delete(0, END)
        self.window.entry_description.delete(0, END)


Controller()