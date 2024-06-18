import requests
from bs4 import BeautifulSoup


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


