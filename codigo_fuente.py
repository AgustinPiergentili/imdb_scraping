import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from concurrent.futures import ThreadPoolExecutor, as_completed

class Scrapear():
    """Clase que se encarga de obtener el HTML de la página de IMDb"""
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def obtener_html(self):
        html = requests.get(self.url, headers=self.headers)
        return html.text
    
    def parsear_html(self, html):
        """Parsea el HTML utilizando BeautifulSoup y lo almacena en self.soup"""
        self.soup = BeautifulSoup(html, 'html.parser')
        return self.soup

    def extraer_nombre(self):
        # Ajuste para el título de la película
        nombre_peli = self.soup.find('a', attrs={'itemprop': 'url'})
        return nombre_peli.text.strip() if nombre_peli else "Nombre no encontrado"
    
    def extraer_ano(self):
        # Ajuste para el año de la película
        ano_peli = self.soup.find('span', attrs={'class': 'nobr'})
        return ano_peli.text.strip() if ano_peli else "Año no encontrado"

    def extraer_opiniones(self):
        """Extrae todas las etiquetas de opiniones de la página"""
        if self.soup:
            opiniones = self.soup.find_all('div', class_='text show-more__control')
            return [opinion.text.strip() for opinion in opiniones]
        return []

def analizar_sentimiento(texto):
    """Analiza el sentimiento de un texto y devuelve un valor numérico"""
    blob = TextBlob(texto)
    sentimiento = blob.sentiment.polarity
    if sentimiento > 0:
        return 1  # positivo
    elif sentimiento < 0:
        return -1  # negativo
    else:
        return 0  # neutro


def procesar_pelicula(tt_id):
    url = f'https://www.imdb.com/title/{tt_id}/reviews/?ref_=tt_ql_2'
    pagina = Scrapear(url)
    html_texto = pagina.obtener_html()
    soup = pagina.parsear_html(html_texto)
    nombre_pelicula = pagina.extraer_nombre()
    ano_pelicula = pagina.extraer_ano()
    opiniones = pagina.extraer_opiniones()
    
    opiniones_con_sentimiento = [analizar_sentimiento(opinion) for opinion in opiniones]
    
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
def guardar_datos_peliculas_concurrente(inicio, fin):
    peliculas = {}
    tt_ids = [f"tt{i:07d}" for i in range(inicio, fin + 1)]
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(procesar_pelicula, tt_id): tt_id for tt_id in tt_ids}
        for future in as_completed(futures):
            result = future.result()
            peliculas[result['nombre']] = result['datos']
            print(f"Guardados datos de la película: {result['nombre']}")
    
    return peliculas

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


# Guardar datos de películas desde tt0000001 hasta tt0000030
peliculas = guardar_datos_peliculas_concurrente(1, 30)

# Mostrar nombres de películas al usuario
print("Películas guardadas:")
for nombre_pelicula in peliculas.keys():
    print(nombre_pelicula)

# Solicitar al usuario el nombre de la película
nombre_pelicula_buscar = input("Introduce el nombre de la película: ")

# Buscar opiniones por nombre de película
opiniones = buscar_opiniones_por_nombre(peliculas, nombre_pelicula_buscar)
if isinstance(opiniones, list):
    for opinion in opiniones:
        print(opinion)
else:
    print(opiniones)

