# Proyecto de Scraping de Reseñas de Películas

Este proyecto está diseñado para scrapear reseñas de películas desde la página de IMDb. El proyecto permite guardar los datos de las reseñas en un archivo CSV y analizar las valoraciones de las películas.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

1. `main.py`: Archivo principal que ejecuta el menú principal del programa.
2. `scrapear.py`: Contiene la clase `Scrapear` que se encarga de obtener y parsear el HTML de la página de IMDb.
3. `procesarPelicula.py`: Contiene la clase `ProcesarPelicula` que se encarga de procesar la información de las películas y analizar los sentimientos de las reseñas.
4. `sentimiento.py`: Contiene la clase `Sentimiento` que se encarga de analizar el sentimiento de las reseñas utilizando la librería `TextBlob`.
5. `archivos.py`: Contiene funciones para guardar los datos en archivos CSV y leerlos.

## Instalación

### Librerías Necesarias

El proyecto requiere las siguientes librerías de Python:

- `requests`
- `beautifulsoup4`
- `textblob`
- `concurrent.futures`

### Instrucciones de Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install requests beautifulsoup4 textblob
    ```

4. Descarga los recursos necesarios para `TextBlob`:

    ```bash
    python -m textblob.download_corpora
    ```

## Uso

Para ejecutar el programa, utiliza el siguiente comando:

```bash
python main.py