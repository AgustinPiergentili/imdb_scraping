from scrapear import Scrapear
from sentimiento import *
from procesarPelicula import *


# Guardar datos de películas desde tt0000001 hasta tt0000030
peliculas = ProcesarPelicula.guardar_datos_peliculas_concurrente(1, 30)

# Mostrar nombres de películas al usuario
print("Películas guardadas:")
for nombre_pelicula in peliculas.keys():
    print(nombre_pelicula)

# Solicitar al usuario el nombre de la película
nombre_pelicula_buscar = input("Introduce el nombre de la película: ")

# Buscar opiniones por nombre de película
opiniones = ProcesarPelicula.buscar_opiniones_por_nombre(peliculas, nombre_pelicula_buscar)
if isinstance(opiniones, list):
    for opinion in opiniones:
        print(opinion)
else:
    print(opiniones)
