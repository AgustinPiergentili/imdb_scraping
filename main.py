from scrapear import Scrapear
from sentimiento import *
from procesarPelicula import *
from archivos import Archivos


class PeliculaApp:
    MENU_PRINCIPAL = """
    Menú Principal
    1. Buscar películas por ID
    2. Buscar la película con más valoraciones positivas en un archivo CSV
    3. Ver ranking de las 5 películas mejor valoradas
    4. Salir
    """

    def solicitar_rango_ids(self):
        """Solicita al usuario un rango de IDs y los valida."""
        while True:
            try:
                inicio = int(input("Introduce el inicio del rango de IDs a scrapear: "))
                fin = int(input("Introduce el fin del rango de IDs a scrapear: "))
                if inicio > fin:
                    inicio, fin = fin, inicio
                return inicio, fin
            except ValueError:
                print("Error: Por favor, introduce un número válido.")

    def manejar_guardar_peliculas(self, peliculas):
        """Maneja la lógica para guardar las películas en un archivo CSV."""
        while True:
            nombre_archivo = input("Introduce el nombre del archivo CSV para guardar (sin extensión): ")
            if nombre_archivo.endswith('.csv'):
                print("El nombre del archivo no debe incluir la extensión '.csv'. Por favor, intenta de nuevo.")
            else:
                nombre_archivo += ".csv"
                Archivos.guardar_peliculas(peliculas, nombre_archivo)
                break

    def manejar_busqueda_peliculas(self):
        """Maneja la lógica para buscar y guardar películas por ID."""
        inicio, fin = self.solicitar_rango_ids()
        peliculas = ProcesarPelicula.guardar_datos_peliculas_concurrente(inicio, fin)

        print("\nPelículas guardadas:")
        for nombre_pelicula in peliculas.keys():
            print(nombre_pelicula)

        while True:
            nombre_pelicula_buscar = input("\nIntroduce el nombre de la película, 'guardar' para guardar todas las películas en CSV, o 'volver' para regresar al menú principal: ")
            if nombre_pelicula_buscar.lower() == 'volver':
                break
            elif nombre_pelicula_buscar.lower() == 'guardar':
                self.manejar_guardar_peliculas(peliculas)
            else:
                opiniones = ProcesarPelicula.buscar_opiniones_por_nombre(peliculas, nombre_pelicula_buscar)
                print(opiniones)

    def manejar_busqueda_positiva(self):
        """Maneja la lógica para buscar la película con más valoraciones positivas."""
        try:
            nombre_archivo = input("Introduce el nombre del archivo CSV que deseas leer (con extensión .csv): ")
            pelicula, positivas = Archivos.pelicula_mas_positiva(nombre_archivo)
            if pelicula:
                print(f"La película con más valoraciones positivas es '{pelicula}' con {positivas} valoraciones positivas.")
            else:
                print("No se encontraron películas en el archivo CSV.")
        except FileNotFoundError:
            print("Error: El archivo especificado no se encuentra.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

    def manejar_ranking_peliculas(self):
        """Maneja la lógica para mostrar el ranking de las 5 películas mejor valoradas."""
        try:
            nombre_archivo = input("Introduce el nombre del archivo CSV que deseas leer (con extensión .csv): ")
            ranking = Archivos.ranking_mejores_peliculas(nombre_archivo)
            if ranking:
                print("Ranking de las 5 películas mejor valoradas:")
                for i, pelicula in enumerate(ranking, start=1):
                    print(f"{i}. {pelicula['Nombre']} ({pelicula['Año']}) - {pelicula['Positivas']} valoraciones positivas, {pelicula['Negativas']} valoraciones negativas")
            else:
                print("No se encontraron películas en el archivo CSV.")
        except FileNotFoundError:
            print("Error: El archivo especificado no se encuentra.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

    def mostrar_menu(self):
        print(self.MENU_PRINCIPAL)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Introduce una opción (1, 2, 3, o 4): ")

            if opcion == '1':
                self.manejar_busqueda_peliculas()
            elif opcion == '2':
                self.manejar_busqueda_positiva()
            elif opcion == '3':
                self.manejar_ranking_peliculas()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, introduce 1, 2, 3 o 4.")


if __name__ == "__main__":
    app = PeliculaApp()
    app.ejecutar()
