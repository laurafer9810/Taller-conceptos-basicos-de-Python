#..................Integrantes...........................
#             Laura Hernandez Rodriguez
#             Sergio Ricardo Leon
#             Jairo Casallas Baquero
#             Roland Lara Rodruiguez
#..........................................................
# Inicialización del directorio
contactos = []

# Definición de mensajes
texto_mensajes = {
    "inicio": "Bienvenido al sistema de gestión de contactos",
    "ingresar_nombre": "Por favor, ingrese el nombre completo (nombre y apellido): ",
    "ingresar_telefono": "Por favor, ingrese el número de teléfono celular: ",
    "ingresar_cumpleanos": "Por favor, ingrese la fecha de cumpleaños (DD/MM): ",
    "ingresar_correo": "Por favor, ingrese el correo electrónico: ",
    "salida": "Gracias por utilizar el sistema de gestión de contactos. ¡Hasta pronto!",
    "error_opcion": "Opción no válida. Por favor, intente nuevamente."
}

# Mensaje de inicio
print(texto_mensajes["inicio"])

# Ciclo principal
while True:
    # Presentar el menú
    print("\n--- Opciones ---")
    print("1. Añadir un nuevo contacto")
    print("2. Buscar un contacto por teléfono")
    print("3. Eliminar un contacto")
    print("4. Salir del programa")
    
    # Solicitar opción al usuario
    seleccion = input("Elija una opción: ")
    
    # Opción 1: Añadir un nuevo contacto
    if seleccion == "1":
        nombre_completo = input(texto_mensajes["ingresar_nombre"])
        telefono_celular = int(input(texto_mensajes["ingresar_telefono"]))
        fecha_cumpleanos = input(texto_mensajes["ingresar_cumpleanos"])
        correo_electronico = input(texto_mensajes["ingresar_correo"])
        
        # Crear un contacto como diccionario
        contacto = {
            "nombre": nombre_completo,
            "telefono": telefono_celular,
            "cumpleanos": fecha_cumpleanos,
            "correo": correo_electronico
        }
        
        # Añadir el contacto al directorio
        contactos.append(contacto)
        print("Contacto añadido exitosamente.")
    
    # Opción 2: Buscar un contacto por teléfono
    elif seleccion == "2":
        telefono_busqueda = int(input("Ingrese el número de teléfono a buscar: "))
        encontrado = False
        for contacto in contactos:
            if contacto["telefono"] == telefono_busqueda:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Cumpleaños: {contacto['cumpleanos']}, Correo: {contacto['correo']}")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún contacto con ese número de teléfono.")
    
    # Opción 3: Eliminar un contacto
    elif seleccion == "3":
        telefono_eliminar = int(input("Ingrese el número de teléfono del contacto a eliminar: "))
        encontrado = False
        for contacto in contactos:
            if contacto["telefono"] == telefono_eliminar:
                contactos.remove(contacto)
                print("Contacto eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún contacto con ese número de teléfono.")
    
    # Opción 4: Salir del programa
    elif seleccion == "4":
        print(texto_mensajes["salida"])
        break
    
    # Opción no válida
    else:
        print(texto_mensajes["error_opcion"])