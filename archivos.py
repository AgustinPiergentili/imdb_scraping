import csv

class Archivos():
    """Clase para el manejo de archivos csv"""
    @staticmethod
    def guardar_peliculas(peliculas, nombre_archivo="peliculas.csv"):
        """Guarda los datos de todas las películas en un archivo CSV"""
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre de la Pelicula', 'Anio', 'Positivas', 'Negativas', 'Neutras', 'ID'])
            for nombre_pelicula, datos in peliculas.items():
                writer.writerow([nombre_pelicula, datos['ano'], datos['positivas'], datos['negativas'], datos['neutras'], datos['id']])
        print(f"Opiniones de todas las películas guardadas en {nombre_archivo}")
        
    def pelicula_mas_positiva(nombre_archivo):
        """Lee el archivo CSV y devuelve la película con más valoraciones positivas"""
        max_positivas = -1
        pelicula_con_mas_positivas = None

        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                positivas = int(row['Positivas'])
                if positivas > max_positivas:
                    max_positivas = positivas
                    pelicula_con_mas_positivas = row['Nombre de la Película']

        return pelicula_con_mas_positivas, max_positivas