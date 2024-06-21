import csv

class Archivos():
    """Clase para el manejo de archivos csv"""
    @staticmethod
    def guardar_peliculas(peliculas, nombre_archivo="peliculas.csv"):
        """Guarda los datos de todas las películas en un archivo CSV"""
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre de la Película', 'Año', 'Positivas', 'Negativas', 'Neutras', 'ID'])
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
    
    @staticmethod
    def ranking_mejores_peliculas(nombre_archivo):
        """Lee el archivo CSV y devuelve un ranking de las 5 películas mejor valoradas"""
        peliculas = []

        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                peliculas.append({
                    'Nombre': row['Nombre de la Película'],
                    'Año': row['Año'],
                    'Positivas': int(row['Positivas']),
                    'Negativas': int(row['Negativas']),
                    'Neutras': int(row['Neutras']),
                    'ID': row['ID']
                })

        # Ordenar las películas por el número de valoraciones positivas (desc) y luego por el número de valoraciones negativas (asc)
        peliculas.sort(key=lambda x: (-x['Positivas'], x['Negativas']))

        # Devolver las 5 primeras películas del ranking
        return peliculas[:5]