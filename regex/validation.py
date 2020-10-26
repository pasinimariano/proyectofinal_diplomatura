import re


def match(x):

    """            Función encargada de realizar la verificación del registro ingresado por el usuario.
    Al ser importada a otro módulo, solo hará falta colocar su nombre, y dentro de unos "()"
    ingresar la variable a verificar. """

    regex = re.compile(r'^[A-z]+(?:[ _][A-z]+)*$')
    regex_match = regex.search(x)
    return regex_match
