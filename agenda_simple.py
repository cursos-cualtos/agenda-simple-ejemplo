from agenda import Agenda
from contacto import Contacto

agenda = Agenda('nueva_agenda')
contactos = agenda.obtener_contactos()

def mostrar_menu():
    print("Bienvenido a Agenda Simple")
    print("Selecciona la acción que desees efectuar")
    print("1. Mostrar contactos")
    print("2. Crear contacto")
    print("3. Guardar contactos en agenda")
    print("0. Prueba de entrada")
    print("9. Salir")
    print("=" * 20)

def mostrar_agenda(agenda):
    for contacto in agenda.mostrar_contactos():
        for campo, dato in contacto.items():
            print(campo, "=", dato)
        print("-" * 15)

def mostrar_contactos():
    for id, contacto in enumerate(contactos):
        print(id, "=", contacto.nombre)
        print("-" * 15)

def crear_contacto(agenda):
    datos = {}
    datos['nombre'] = input("Ingrese el nombre: ")
    datos['empresa'] = input("Ingrese la empresa: ")
    datos['correo'] = input("Ingrese el correo: ")
    datos['telefono'] = input("Ingrese el telefono: ")
    datos['nota'] = input("Ingrese nota: ")
    nuevo_contacto = Contacto(datos)
    agenda.agregar_contacto(nuevo_contacto)

def crear_contacto_alt():
    nuevo_contacto = Contacto(input("Ingresa el nombre: "))
    nuevo_contacto.empresa = input("Ingresa empresa: ")
    nuevo_contacto.correo = input("Ingresa correo: ")
    nuevo_contacto.telefono = input("Ingresa telefono: ")
    nuevo_contacto.nota = input("Ingresa nota: ")
    contactos.append(nuevo_contacto)

def prueba_entrada():
    salida = input("Ingresa algo: ")
    print(salida)
    return salida

def ejecutar_opcion(opcion):
    if isinstance(opcion, int):
        print("=" * 20)
        if opcion == 1:
            mostrar_contactos()
        elif opcion == 2:
            crear_contacto_alt()
        elif opcion == 3:
            agenda.agregar_contactos(contactos)
            agenda.guardar()
            print("Agenda guardada correctamente.")
        elif opcion == 0:
            prueba_entrada()
        elif opcion == 9:
            print("Agenda cerrada")
            exit()

def validar_seleccion():
    while True:
        try:
            seleccion = int(input("Ingrese opcion: "))
            break
        except ValueError:
            print("Error. Ingrese unicamente numeros enteros.")
    return seleccion

if __name__ == "__main__":
    seleccion = 'S'
    while(seleccion in  ['S', 's', 'Si', 'SI', 'si']):
        mostrar_menu()
        ejecutar_opcion(validar_seleccion())
        seleccion = input("Desea continuar? (S/N): ")
