import argparse
from agenda import Agenda
from contacto import Contacto

agenda = Agenda('nueva_agenda')
contactos = agenda.obtener_contactos()

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--show', help='Show currently stored contacts')
parser.add_argument('-a', '--add', help='Add new contact', action='store_true')
args = parser.parse_args()

if args.show and args.show == 'all':
    print(agenda.mostrar_contactos())
elif args.add:
    nuevo_contacto = Contacto(input("Ingresa el nombre: "))
    nuevo_contacto.empresa = input("Ingresa empresa: ")
    nuevo_contacto.correo = input("Ingresa correo: ")
    nuevo_contacto.telefono = input("Ingresa telefono: ")
    nuevo_contacto.nota = input("Ingresa nota: ")
    contactos.append(nuevo_contacto)
    agenda.agregar_contactos(contactos)
    agenda.guardar()