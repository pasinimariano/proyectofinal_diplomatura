import mysql.connector
from tkinter import messagebox
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Text, Integer, String, DateTime, func, or_, desc
from sqlalchemy.exc import OperationalError
import regex.validation
from view.decorators import *


class CreateDb:
    """            Clase encargada de concectarse con el servidor, y crear la base de datos,
    la cual sera indispensable para toda funcionalidad de la App.
    Asi mismo, invoca a la clase "Create_tables", para crear sus respectivas tablas. 
    Puede generarse un error fatal, si no se inicia el servidor donde se almacena la base de datos.
    El usuario sera notificado de dicho error mediante un popup."""

    def __init__(self, ):
        try:
            self.db = mysql.connector.connect(host='localhost',
                                              user='root',
                                              passwd=''
                                              )
            self.cursor = self.db.cursor()
            try:
                self.cursor.execute('CREATE DATABASE Python_avanzado')
                self.db.commit()
                CreateTables()
                self.db.close()
            except mysql.connector.Error:
                pass
        except mysql.connector.InterfaceError:
            messagebox.showerror('ERROR 2003', '''Error: No se puede establecer una conexión ya que se denegó la conexión.
            Intente conectarse con el servidor de su base de datos, y vuelva a intentar.''')
        except ConnectionRefusedError:
            messagebox.showerror('Error de conexion',
                                 'Para mostrar los datos, debe estar conectado a la base de datos.')


class CreateTables:

    """            Clase encargada de crear las tablas. Utilizando el lenguaje de SqlAlchemy."""

    def __init__(self, ):

        self.db_url = "mysql+pymysql://root@localhost/Python_avanzado"
        self.engine = create_engine(self.db_url)
        self.metadata = MetaData(self.engine)
        self.table_producto = Table('Producto', self.metadata,
                                    Column('Id', Integer, primary_key=True),
                                    Column('Titulo', String(128)),
                                    Column('Fecha', DateTime, server_default=func.now()),
                                    Column('Descripcion', Text),
                                    Column('Estado', String(12)),
                                    Column('Objeto', Text)
                                    )
        self.metadata.create_all()

    def show_records(self, tview):

        """            Metodo encargado de mostrar en el Treeview todos los registros de la db.
        Para ello, utiliza el lenguaje de SqlAlchemy.
        Hay que tener en cuenta que para su funcionamiento, se debera acceder al Treeview, el cual
        sera insertado como parametro del metodo."""

        try:
            self.records = tview
            self.records_tree = self.records.get_children()
            for items in self.records_tree:
                self.records.delete(items)
            self.conn = self.engine.connect()
            self.select = self.table_producto.select().where(
                or_(self.table_producto.c.Id >= '0'
                    )).order_by(desc(self.table_producto.c.Id))
            self.response = self.conn.execute(self.select)
            for x in self.response:
                self.records.insert('', 'end', text=x[0],
                                    values=(x[1], x[2], x[3], x[4], x[5]))
        except OperationalError:
            messagebox.showerror('Error de conexion',
                                 'Para mostrar los datos, debe estar conectado a la base de datos.')

    @decorator_insert
    def insert_record(self, titulo, descripcion, objeto):

        """            Metodo encargado de insertar datos en las tablas. Para ello, utiliza el lenguaje de SqlAlchemy.
        Hay que tener en cuenta que esperara los parametros ingresados en los entries de la App."""

        try:
            if len(titulo) != 0 and len(descripcion) != 0:
                if regex.validation.match(titulo) and regex.validation.match(descripcion):
                    self.insert = self.table_producto.insert().values(Titulo=titulo,
                                                                      Descripcion=descripcion,
                                                                      Objeto=objeto)
                    self.conn = self.engine.connect()
                    self.conn.execute(self.insert)
                    messagebox.showinfo('Data Update', 'El registro -{}- fue ingresado correctamente'.format(titulo))
                else:
                    messagebox.showerror('ERROR',
                                         'Error: El registro no debe contener números, ni caracteres especiales.')
            else:
                messagebox.showerror('ERROR', 'Error: Alguno de los campos está vacio')

        except OperationalError:
            messagebox.showerror('Error de conexión',
                                 'Para mostrar los datos, debe estar conectado a la base de datos.')

    @decorator_delete
    def delete_record(self, tview):

        """            Metodo encargado de eliminar el registro de la db, seleccionado en el Treeview.
        Para ello, utiliza el lenguaje de SqlAlchemy.
        Hay que tener en cuenta que para su funcionamiento, se debera acceder al Treeview, el cual
        sera insertado como parametro del metodo."""

        try:
            self.record = tview
            if self.record.item(self.record.selection())['text']:
                self.box_confirm = messagebox.askquestion('Delete record',
                                                          '¿Esta seguro que desea eliminar el registro?',
                                                          icon='warning')
                if self.box_confirm == 'yes':
                    self.selection = self.record.item(self.record.selection())['text']
                    self.conn = self.engine.connect()
                    self.table = self.table_producto.delete().where(self.table_producto.c.Id == self.selection)
                    self.response = self.conn.execute(self.table)
                    messagebox.showinfo('Data Update',
                                        'El registro -{}- fue eliminado correctamente'.format(self.selection))
                else:
                    self.selection = None
            else:
                messagebox.showerror('ERROR', 'Error: Para eliminar, debe seleccionar un registro.')
        except OperationalError:
            messagebox.showerror('Error de conexión',
                                 'Para mostrar los datos, debe estar conectado a la base de datos.')

    @decorator_update
    def update_record(self, tview, titulo, descripcion, objeto):

        """            Metodo encargado de modificar el registro de la db, seleccionado en el Treeview.
        Para ello, utiliza el lenguaje de SqlAlchemy.
        Hay que tener en cuenta que para su funcionamiento, se deberá acceder al Treeview, el cual
        sera insertado como parámetro del metodo. Y asimismo, se necesitará acceder a los datos de los
        entries, tambien serán insertados como parametros del metodo."""

        try:
            self.record = tview
            if len(titulo) != 0 and len(descripcion) != 0:
                if regex.validation.match(titulo) and regex.validation.match(descripcion):
                    if self.record.item(self.record.selection())['text']:
                        self.box_confirm = messagebox.askquestion('Update record',
                                                                  '¿Esta seguro que desea modificar el registro?',
                                                                  icon='warning')
                        if self.box_confirm == 'yes':
                            self.selection = self.record.item(self.record.selection())['text']
                            self.table = self.table_producto.update().where(
                                self.table_producto.c.Id == self.selection
                            ).values(Titulo=titulo,
                                     Descripcion=descripcion,
                                     Objeto=objeto)
                            self.conn = self.engine.connect()
                            self.conn.execute(self.table)
                            messagebox.showinfo('Data Update', 'Registro -{}- actualizado correctamente'.format(titulo))
                        else:
                            self.selection = None
                    else:
                        messagebox.showerror('ERROR', 'Error: Para modificar, debe seleccionar un registro.')
                else:
                    messagebox.showerror('ERROR',
                                         'Error: El registro no debe contener números, ni caracteres especiales.')
            else:
                messagebox.showerror('ERROR', 'Error: Alguno de los campos está vacio')
        except OperationalError:
            messagebox.showerror('Error de conexión',
                                 'Para mostrar los datos, debe estar conectado a la base de datos.')


class ObjetoStr:
    def __init__(self, titulo):
        self.objeto = titulo

    def __str__(self, ):
        return self.objeto
