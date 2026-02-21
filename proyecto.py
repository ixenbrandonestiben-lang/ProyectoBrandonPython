from json import load, dump
archivo_datos = "registros.json"

def cargar_datos():
    try:
        with open(archivo_datos, "r") as archivo:
            return load(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
        return []
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []

def guardar_datos(coleccion):
    try:
        with open(archivo_datos, "w") as archivo:
            dump(coleccion, archivo, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def separador():  
    print("==========================================")

    
def mostrar_coleccion(coleccion):
    if not coleccion:
        print("La colección está vacía.")
    else:
        for i, item in enumerate(coleccion, start=1):
            print(f"{i}. {item['tipo']}: {item['titulo']} - {item['autor']} - {item['genero']} - {item['valoracion']}")

while True:
    try:
        separador()
        print("        Administrador de colecciones    ")
        separador()
        print("1. Añadir elemento a la colección")
        print("2. ver todos los elementos")
        print("3. Buscar elementos")
        print("4. Editar elementos")
        print("5. Eliminar elementos")
        print("6. ver elementos ")
        print("7. Salir")
        separador()

        op = int(input("Ingrese una opción: "))
        separador()

        if op == 1:
            while True:
                try:
                    separador()
                    print("    añadir un nuevo elemento")
                    separador()
                    print("1.libro")
                    print("2.película")
                    print("3.música")
                    print("4.regresar al menu principal")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op in [1, 2, 3]:
                        tipo = "Libro" if sub_op == 1 else "Película" if sub_op == 2 else "Música"
                        titulo = input("Ingrese el título: ")
                        autor = input("Ingrese el autor/director/artista: ")
                        genero = input("Ingrese el género: ")
                        valoracion = input("Ingrese la valoración: ")
                        coleccion = cargar_datos()
                        coleccion.append({
                            "tipo": tipo,
                            "titulo": titulo,
                            "autor": autor,
                            "genero": genero,
                            "valoracion": valoracion
                        })
                        guardar_datos(coleccion)  
                        print(f"{tipo} añadido exitosamente.")
                    elif sub_op == 4:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif op == 2:
            while True:
                try:
                    separador()
                    print("    Ver todos los elementos   ")
                    separador()
                    print("1. ver todos los libros")
                    print("2. ver todas las peliculas")
                    print("3. ver toda la musica")
                    print("4. regresar al munu principal")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        coleccion = cargar_datos()
                        separador()
                        libros = [item for item in coleccion if item['tipo'] == "Libro"]
                        
                        
                        mostrar_coleccion(libros)
                        separador()
                    elif sub_op == 2:
                        coleccion = cargar_datos()
                        separador()
                        peliculas = [item for item in coleccion if item['tipo'] == "Película"]
                        
                        
                        mostrar_coleccion(peliculas)
                    elif sub_op == 3:
                        coleccion = cargar_datos()
                        musica = [item for item in coleccion if item['tipo'] == "Música"]
                
                        mostrar_coleccion(musica)
                    elif sub_op == 4:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif op == 3:
            while True:
                try:
                    separador()
                    print("")
                    separador()
                    print("1. buscar por titulo")
                    print("2. buscar por autor/director/artista")
                    print("3. buscar por genero")
                    print("4.regresar al menu")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        criterio = input("Ingrese el título a buscar: ").lower()
                        coleccion = cargar_datos()
                        resultados = [item for item in coleccion if criterio in item['titulo'].lower()]
                        mostrar_coleccion(resultados)
                    elif sub_op == 2:
                        criterio = input("Ingrese el autor a buscar: ").lower()
                        coleccion = cargar_datos()
                        resultados = [item for item in coleccion if criterio in item['autor'].lower() ]
                        mostrar_coleccion(resultados)
                    elif sub_op == 3:
                        criterio = input("Ingrese el genero a buscar: ").lower()
                        coleccion = cargar_datos()
                        resultados = [item for item in coleccion if criterio in item['genero'].lower()]
                        mostrar_coleccion(resultados)
                    elif sub_op ==4:    
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif op == 4: 
            while True:

                try:
                    separador()
                    print("     editar un elemento    ")
                    separador()
                    coleccion = cargar_datos()
                    
                    if not coleccion:
                        print("Colección vacía.")
                        input("Enter para continuar...")
                        continue
                    mostrar_coleccion(coleccion)
                    separador()
                    
                    print("1. editar titulo")
                    print("2. editar autor/director/artista")
                    print("3. editar genero")
                    print("4. editar valoracion")
                    print("5. regresar al menu principal")
                    separador()
                    
                    sub_op = int(input("Elija una opción: "))
                    
                    if sub_op in [1, 2, 3, 4]:
                        indice = int(input("Número del elemento: ")) - 1
                        if 0 <= indice < len(coleccion):
                            item = coleccion[indice]
                            print(f"→ Editando: {item['titulo']}")
                            
                            if sub_op == 1: 
                                nuevo = input(f"Nuevo título [{item['titulo']}]: ")
                                if nuevo.strip(): item['titulo'] = nuevo.strip()
                                
                            elif sub_op == 2: 
                                nuevo = input(f"Nuevo autor [{item['autor']}]: ")
                                if nuevo.strip(): item['autor'] = nuevo.strip()
                                
                            elif sub_op == 3: 
                                nuevo = input(f"Nuevo género [{item['genero']}]: ")
                                if nuevo.strip(): item['genero'] = nuevo.strip()
                                
                            elif sub_op == 4:  
                                nuevo = input(f"Nueva valoración [{item['valoracion']}]: ")
                                if nuevo.strip():
                                    try:
                                        item['valoracion'] = f"{float(nuevo):.1f}"
                                        print(" Guardado.")
                                    except ValueError:
                                        print(" Debe ser número (ej: 8.5). Sin cambio.")
                                        continue
                            
                            guardar_datos(coleccion)
                            print(" Elemento editado y guardado.")
                        else:
                            print(" Índice inválido.")
                            
                    elif sub_op == 5:
                        print("Regresando al menú principal...")
                        break
                        
                    else:
                        print(" Opción inválida.")
                        
                except ValueError:
                    print("Solo números.")
                except Exception as e:
                    print(f" Error: {e}")
        elif op == 5:  
            while True:
                try:
                    separador()
                    print("*** ELIMINAR ELEMENTO ***")
                    separador()
                    coleccion = cargar_datos()
                    mostrar_coleccion(coleccion)
                    separador()
                    print("1. Eliminar un elemento")
                    print("2. Volver")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        if not coleccion:
                            print("La colección está vacía.")
                        else:
                            indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
                            if 0 <= indice < len(coleccion):
                                eliminado = coleccion.pop(indice)
                                guardar_datos(coleccion)
                                print(f"'{eliminado['titulo']}' eliminado exitosamente.")
                            else:
                                print("Número inválido.")
                    elif sub_op == 2:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif op == 6:
            while True:

                try:        
                    
                    coleccion = cargar_datos()
                    separador()
                    print("1. Libros  2. Películas  3. Músicas  4. Volver")
                    sub_op = int(input("Categoría (1-4): "))
                    
                    if sub_op == 4: 
                        print("regresando..."); 
                        
                    cat = ["libro", "pelicula", "musica"][sub_op-1]
                    separador()
                    print(f"{cat.upper()}: 1.Género 2.Autor 3.Volver")
                    opc = int(input("Opción: "))
                    
                    if opc == 3: continue
    
                    busca = input(f"{['Género','Autor'][opc-1]} {cat}: ").lower()
                    campo = ['genero','autor'][opc-1]
                    
                    encontrado = False
                    for item in coleccion:
                        if cat in item['genero'].lower() and busca == item[campo].lower():
                            print(f" {item['titulo']} ({item['autor']})")
                            encontrado = True
                    
                    if not encontrado:
                        print(" No encontrado")
                        
                except ValueError: 
                    print("Opción inválida")
        elif op == 7:
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
    except ValueError:
        print("Por favor, ingrese un número válido.")