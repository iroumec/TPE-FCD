import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Función para realizar la búsqueda en Google y devolver varias URLs
def buscar_en_google(query, num_enlaces=5):
    urls = []
    for url in search(query, num_results=num_enlaces, timeout=num_enlaces, lang="es"):
        urls.append(url)
    return urls

# Función para verificar la información en una URL
def verificar_cancion(url, nombre_cancion, autor, fecha_lanzamiento):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Simplificado: Verificamos si las palabras clave aparecen en la página
        if (nombre_cancion.lower() in soup.text.lower() and 
            autor.lower() in soup.text.lower() and 
            fecha_lanzamiento in soup.text):
            return True
    except Exception as e:
        print(f"Error al acceder a {url}: {e}")
    return False

# Cargar el dataset desde un archivo CSV
dataset = pd.read_csv('Covers.csv')
dataset = dataset.drop(dataset.index[0:342])

# Crear una nueva columna para los resultados
dataset['Verified'] = ''

# Recorrer el dataset
for index, row in dataset.iterrows():
    nombre_cancion = row['Track']
    autor = row['Artist']
    fecha_lanzamiento = row['Year']
    
    # Crear la consulta para Google
    query = f"{nombre_cancion} {autor} fecha de lanzamiento"
    
    # Buscar en Google y obtener varias URLs
    urls = buscar_en_google(query, num_enlaces=5)
    
    es_correcto = False
    # Verificar cada una de las URLs obtenidas
    for url in urls:
        if verificar_cancion(url, nombre_cancion, autor, str(fecha_lanzamiento)):
            es_correcto = True
            break  # Si encontramos un enlace correcto, no necesitamos seguir buscando
    
    # Guardar el resultado en la nueva columna
    if es_correcto:
        dataset.at[index, 'Verified'] = 'Yes'
    else:
        dataset.at[index, 'Verified'] = 'No'
    
    # Guardar los resultados parciales en el archivo
    dataset.to_csv('resultados_canciones2.csv', index=False)

print("Verificación completada. Resultados guardados en 'resultados_canciones.csv'.")
