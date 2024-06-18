from scrapear import Scrapear
from procesarPelicula import *

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
    nombre_pelicula_buscar = input("\nIntroduce el nombre de la película o 'exit' para salir: ")

    if nombre_pelicula_buscar.lower() == 'exit':
        break

    # Buscar opiniones por nombre de película
    opiniones = ProcesarPelicula.buscar_opiniones_por_nombre(peliculas, nombre_pelicula_buscar)
    if isinstance(opiniones, list):
        for opinion in opiniones:
            print(opinion)
    else:
        print(opiniones)