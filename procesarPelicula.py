from concurrent.futures import ThreadPoolExecutor, as_completed
from sentimiento import Sentimiento
from scrapear import Scrapear
from procesarPelicula import *


class ProcesarPelicula(Sentimiento):

    @staticmethod
    def procesar(tt_id):
        url = f'https://www.imdb.com/title/{tt_id}/reviews/?ref_=tt_ql_2'
        pagina = Scrapear(url)
        html_texto = pagina.obtener_html()
        soup = pagina.parsear_html(html_texto)
        nombre_pelicula = pagina.extraer_nombre()
        ano_pelicula = pagina.extraer_ano()
        opiniones = pagina.extraer_opiniones()
        
        opiniones_con_sentimiento = [Sentimiento.analizar_sentimiento(opinion) for opinion in opiniones]
        
        # Suma de opiniones
        positivas = sum(1 for sentimiento in opiniones_con_sentimiento if sentimiento == 1)
        negativas = sum(1 for sentimiento in opiniones_con_sentimiento if sentimiento == -1)
        neutras = sum(1 for sentimiento in opiniones_con_sentimiento if sentimiento == 0)
        
        return {
            'nombre': nombre_pelicula.lower(),
            'datos': {
                'ano': ano_pelicula,
                'positivas': positivas,
                'negativas': negativas,
                'neutras': neutras,
                'id': tt_id
            }
        }


    # Función para guardar datos de múltiples películas usando concurrencia
    @staticmethod
    def guardar_datos_peliculas_concurrente(inicio, fin):
        peliculas = {}
        tt_ids = [f"tt{i:07d}" for i in range(inicio, fin + 1)]
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(ProcesarPelicula.procesar, tt_id): tt_id for tt_id in tt_ids}
            for future in as_completed(futures):
                result = future.result()
                peliculas[result['nombre']] = result['datos']
        
        return peliculas

    @staticmethod
    def buscar_opiniones_por_nombre(peliculas, nombre):
        nombre = nombre.lower()
        if nombre in peliculas:
            datos_pelicula = peliculas[nombre]
            return f"Opiniones de la película '{nombre}':\n" \
                    f"Positivas: {datos_pelicula['positivas']}\n" \
                    f"Negativas: {datos_pelicula['negativas']}\n" \
                    f"Neutras: {datos_pelicula['neutras']}"
        else:
            return "Película no encontrada"

