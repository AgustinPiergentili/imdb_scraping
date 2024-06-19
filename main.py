from scrapear import Scrapear
from sentimiento import *
from procesarPelicula import *
from archivos import Archivos



# Solicitar rango de IDs
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
            inicio = int(input("Introduce el inicio del rango de IDs a scrapear: "))
            fin = int(input("Introduce el fin del rango de IDs a scrapear: "))

            # Guardar datos de películas desde tt0000001 hasta tt0000030
            peliculas = ProcesarPelicula.guardar_datos_peliculas_concurrente(inicio, fin)

            while True:
                # Mostrar nombres de películas al usuario
                print("\nPelículas guardadas:")
                for nombre_pelicula in peliculas.keys():
                    print(nombre_pelicula)

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

        elif opcion == '2':
            # Buscar la película con más valoraciones positivas
            nombre_archivo = input("Introduce el nombre del archivo CSV que deseas leer (con extensión .csv): ")
            pelicula, positivas = Archivos.pelicula_mas_positiva(nombre_archivo)
            if pelicula:
                print(f"La película con más valoraciones positivas es '{pelicula}' con {positivas} valoraciones positivas.")
            else:
                print("No se encontraron películas en el archivo CSV.")

        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, introduce 1, 2, o 3.")

if __name__ == "__main__":
    main()