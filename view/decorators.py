def decorator_insert(func):
    def inner(*args):
        func(*args)
        print('Se esta ejecutando {}'.format(func.__name__))
        if len(args[1]) != 0 and len(args[2]) != 0:
            print('Los datos fueron cargados exitosamente.')
            print('--'*45)
        else:
            print('Error al cargar los datos.\n'
                  'Verifique los datos y vuelva a intentar.')
            print('--' * 45)

    return inner


def decorator_delete(func):
    def inner(*args):
        func(*args)
        print('Se esta ejecutando {}'.format(func.__name__))
        record = args[1].selection()
        if record:
            print('Los datos fueron eliminados.')
            print('--' * 45)
        else:
            print('Error al intentar eliminar los datos.')
            print('--' * 45)

    return inner


def decorator_update(func):
    def inner(*args):
        func(*args)
        print('Se esta ejecutando {}'.format(func.__name__))
        if len(args[2]) != 0 and len(args[3]) != 0:
            print('Los datos fueron modificados exitosamente.')
            print('--' * 45)
        else:
            print('Error al intentar modificar los datos.\n'
                  'Verifique los datos y vuelva a intentar.')
            print('--' * 45)

    return inner
