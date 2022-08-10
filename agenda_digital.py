def escribir_agenda(nombre_agenda, agenda_digital):
    """Escribe la agenda en un fichero de texto.

    Parametros posicionales
    nombre_agenda -- str que representa el nombre de la agenda en disco.
    agenda_digital -- dict que representa la agenda y los contactos.
    """
    agenda_fichero = open(nombre_agenda, "w")
    # Escribimos el diccionario en el fichero
    agenda_fichero.write(str(agenda_digital))
    # Cerramos el fichero abierto con open
    agenda_fichero.close()

def leer_agenda(nombre_agenda):
    """Lee la agenda de un fichero en disco.

    Parametros posicionales:
    nombre_agenda -- str que representa el nombre de la agenda en disco.
    """
    agenda_digital_lectura = open(nombre_agenda, "r")
    # Leemos todas las líneas del fichero y las asignamos a la variable agenda_digital
    agenda_digital = agenda_digital_lectura.readlines()
    # Cerramos el fichero abierto con open
    agenda_digital_lectura.close()
    return eval(agenda_digital[0])

def solicitar_contacto_agenda():
    """Esta funcion solicita los datos de un nuevo contacto al usuario"""
    Nombre = input("Introduce el nombre completo del contacto: ")
    Direccion = input("Introduce la direccion del contacto: ")
    Email = input("Introduce el email del contacto: ")
    Telefono = input("Introduce el telefono del contacto: ")
    # Construimos un diccionario con los valores recibidos
    Contacto = {
        "Nombre": Nombre,
        "Direccion": Direccion,
        "Email": Email,
        "Telefono": Telefono
    }
    return Contacto


def crear_contacto(agenda_digital, nuevo_agenda):
    """Introduce un nuevo contacto en la agenda.

    Parametros posicionales:
    agenda_digital -- dict que representa la agenda digital.
    nuevo_agenda -- dict que representa un nuevo contacto.
    """
    agenda_digital[nuevo_agenda["Nombre"]] = {
        "Direccion": nuevo_agenda["Direccion"],
        "Email": nuevo_agenda["Email"],
        "Telefono": nuevo_agenda["Telefono"]
    }
    return agenda_digital

def consultar_contacto_agenda(agenda_digital):
    """Esta funcion consulta un contacto en la agenda."""
    nombre_completo = input("Introduce el nombre completo del contacto: ")
    print("\n[+]", nombre_completo)
    print("\tDireccion:", agenda_digital[nombre_completo]["Direccion"])
    print("\tEmail:", agenda_digital[nombre_completo]["Email"])
    print("\tTelefono:", agenda_digital[nombre_completo]["Telefono"])

#Se crea el fichero de la agenda en disco
agenda_digital = {}
escribir_agenda("agenda_digital", agenda_digital)

#Solicitamos datos de nuevos contactos
agenda_digital = leer_agenda("agenda_digital")
nuevo_agenda = solicitar_contacto_agenda()
agenda_digital = crear_contacto(agenda_digital, nuevo_agenda)
escribir_agenda("agenda_digital", agenda_digital)

#Consultamos algún contacto de la agenda
print("Buscamos el nuevo contacto en la agenda")
agenda_digital = leer_agenda("agenda_digital")
consultar_contacto_agenda(agenda_digital)
