from scrapear import Scrapear
from sentimiento import *
from procesarPelicula import *
from archivos import Archivos

def main():
    while True:
        # Mostrar el menú principal
        print("\nMenú Principal")
        print("1. Guardar datos de películas en CSV")
        print("2. Buscar la película con más valoraciones positivas en un archivo CSV")
        print("3. Salir")

        opcion = input("Introduce una opción (1, 2, o 3): ")

        if opcion == '1':
            # Solicitar rango de IDs
            try:
                inicio = int(input("Introduce el inicio del rango de IDs a scrapear: "))
                fin = int(input("Introduce el fin del rango de IDs a scrapear: "))

                # Validar y ajustar el rango si es necesario
                if inicio > fin:
                    print("El valor de inicio es mayor que el valor de fin. Intercambiando valores...")
                    inicio, fin = fin, inicio

                # Guardar datos de películas desde el rango especificado
                peliculas = ProcesarPelicula.guardar_datos_peliculas_concurrente(inicio, fin)

                # Mostrar nombres de películas al usuario
                print("\nPelículas guardadas:")
                for nombre_pelicula in peliculas.keys():
                    print(nombre_pelicula)

                while True:
                    # Solicitar al usuario el nombre de la película
                    nombre_pelicula_buscar = input("\nIntroduce el nombre de la película, 'guardar' para guardar todas las películas en CSV, o 'volver' para regresar al menú principal: ")

                    if nombre_pelicula_buscar.lower() == 'volver':
                        break
                    elif nombre_pelicula_buscar.lower() == 'guardar':
                        nombre_archivo = input("Introduce el nombre del archivo CSV (sin extensión): ") + ".csv"
                        Archivos.guardar_peliculas(peliculas, nombre_archivo)
                    else:
                        # Buscar opiniones por nombre de película
                        opiniones = ProcesarPelicula.buscar_opiniones_por_nombre(peliculas, nombre_pelicula_buscar)
                        print(opiniones)

            except ValueError:
                print("Error: Por favor, introduce un número válido.")
            except Exception as e:
                print(f"Se produjo un error: {e}")

        elif opcion == '2':
            try:
                # Buscar la película con más valoraciones positivas
                nombre_archivo = input("Introduce el nombre del archivo CSV que deseas leer (con extensión .csv): ")
                pelicula, positivas = Archivos.pelicula_mas_positiva(nombre_archivo)
                if pelicula:
                    print(f"La película con más valoraciones positivas es '{pelicula}' con {positivas} valoraciones positivas.")
                else:
                    print("No se encontraron películas en el archivo CSV.")

            except Exception as e:
                print(f"Se produjo un error: {e}")

        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, introduce 1, 2, o 3.")

if __name__ == "__main__":
    main()
