import json
from .contacto import Contacto

class Agenda():
    def __init__(self, nombre):
        """Crea un nuevo objeto agenda con el nombre indicado en
        el argumento.
        Argumentos:
        nombre -> str
        Valor de retorno:
        () -> Agenda
        """
        self.contactos = []
        self.nombre = nombre
        self.archivo = nombre + '.tdb'
        self.cargar()

    def cargar(self):
        """Carga los datos de una agenda guardada anteriormente,
        los datos son cargados de un documento de texto.
        Argumentos:
        (ninguno)
        Valor de retorno:
        (ninguno)
        """
        try:
            with open(self.archivo, 'r') as db:
                for registro in db:
                    contacto = json.loads(registro)
                    self.contactos.append(contacto)
        except FileNotFoundError as error:
            pass

    def guardar(self):
        with open(self.archivo, 'w') as db:
            for contacto in self.contactos:
                db.write(json.dumps(contacto))
                db.write('\n')

    def agregar_contacto(self, contacto):
        if isinstance(contacto, dict):
            self.contactos.append(contacto)
        elif isinstance(contacto, Contacto):
            self.contactos.append(contacto.obtenerDatos())
        else:
            raise TypeError

    def agregar_contactos(self, lista_contactos):
        if isinstance(lista_contactos, list):
            self.contactos.clear()
            for contacto in lista_contactos:
                if isinstance(contacto, Contacto):
                    self.contactos.append(contacto.obtenerDatos())
                else:
                    raise TypeError

    def mostrar_contactos(self):
        return self.contactos

    def obtener_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                return contacto.copy()
            else:
                return {}

    def obtener_contactos(self):
        lista_contactos = []
        for contacto in self.contactos:
            nuevo_contacto = Contacto(contacto)
            lista_contactos.append(nuevo_contacto)
        return lista_contactos
