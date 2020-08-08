importy csv

ARCHIVO = "agenda.csv"
CAMPOS = ["Nombre","Apellido","Telefono","Cumpleaños"]

def leer_csv(datos_csv):
	try:
		return datos_csv.next()
	except:
		return None

def leer_datos(archivo):
	abierto = open(archivo)
	datos_csv = csv.reader(abierto)
	campos = leer_csv(datos_csv)
	datos = []
	elemento = leer_csv(datos_csv)
	while elemento:
		datos.append(elemento)
		elemento = leer_csv(datos_csv)
	abierto.close()
	return datos


def guardar_datos(datos, archivo):
	abierto = open(archivo, "w")
	datos_csv = csv.writer(abierto)
	datos_csv.writerow(CAMPOS)
	datos_csv.writerows(datos)
	abierto.close()

def leer_busqueda():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    return (nombre, apellido)

def buscar(nombre, apellido, datos):
    for elemento in datos:
        if nombre in elemento[0] and apellido in elemento[1]:
            return elemento
    return None

def menu_alta(nombre, apellido, datos):
    print("No se encuentra %s %s en la agenda." % (nombre, apellido))
    confirmacion = input("Desea ingresarlo? (s/n) ")
    if confirmacion.lower() != "s":
        return
    telefono = input("Telefono: ")
    cumple = input("Cumpleaños: ")
    datos.append([nombre, apellido, telefono, cumple])
    
def mostrar_elemento(elemento):
    print()
    print(( "%s %s") % (elemento[0], elemento[1]))
    print("Telefono: %s" % elemento[2])
    print("Cumpleaños: %s" % elemento[3])
    print()
    
def menu_elemento():
    o = input("b: borrar, m: modificar, ENTER para containuar (b/m) ")
    return o.lower()

def modificar(viejo, nuevo, datos):
    indice = datos.index(viejo)
    datos[indice] = nuevo
    
def menu_modificacion(elemento, datos):
    nombre = input("Nuevo apellido: ")
    apellido = input("Nuevo telefono: ")
    cumple = input("Nuevo cumpleaños: ")
    modificar(elemento, [nombre, apellido, telefono, cumple], datos)
    
def baja(elemento, datos):
    datos.remove(elemento)
    
def confirmar_salida():
    confirmacion = input("¿Desea salir? (s/n) ")
    return confirmacion.lower() == "s"

def agenda():
    datos = leer_datos(ARCHIVO)
    fin = False
    while not fin:
        (nombre, apellido) = leer_busqueda()
        if nombre == "" and apellido == "":
            fin = confirmar_salida()
            continue
        elemento = buscar(nombre, apellido, datos)
        if not elemento: 
            menu_alta(nombre, apellido, datos)
            continue
        mostrar_elemento(elemento)
        opcion = menu_elemento()
        if opcion == "m":
            menu_modificacion(elemento, datos)
        elif opcion == "b":
            baja(elemento, datos)
    guardar_datos(datos, ARCHIVO)

agenda()