# Instalación de la librería necesaria para utilizar la API.
# pip install musicbrainzngs

import musicbrainzngs
import pandas as pd

# Carga del dataset.
artist_dataset = pd.read_csv("Datasets/Generados/ArtistDataset.csv")

# Eliminación de los artistas repetidos.
artistas_unicos = list(artist_dataset["Artist"].unique())

# Creación de un dataset utilizando un diccionario con los artistas únicos.
artist_dataset = pd.DataFrame.from_dict({"Artista" : artistas_unicos})

# Configuración de los datos de conexión.
musicbrainzngs.set_useragent("TPE-FCD", "1.0", "iroumec@alumnos.exa.unicen.edu.ar")

# Definición de la función encargada de realizar la búsqueda de la nacionalidad del artista.
def obtener_nacionalidad_artista(nombre_artista):
    try:
        
        nombre = None
        nacionalidad = None
        
        # Consulta del artista.
        resultado = musicbrainzngs.search_artists(artist=nombre_artista)
        
        # Si se hallaron resultados...
        if resultado['artist-count'] > 0:
            # Se toma el primer resultado que coincida.
            artista = resultado['artist-list'][0]
            nombre = artista['name']
            
            # Se verifica si hay información sobre la nacionalidad del artista...
            if 'country' in artista:
                nacionalidad = artista['country']
        
        return nombre, nacionalidad
    
    except Exception as e:
        print(f"Error al obtener la información: {e}")
        return None, None

# Creación en el dataset de una nueva columna para el nombre y nacionalidad hallados.
artist_dataset["Nombre"] = 'Unknown'
artist_dataset["Nacionality"] = 'Unknown'

# Por cada artista, se invoca la función y se obtiene su nacionalidad.
for index, artist in enumerate(artist_dataset['Artista']):
    
    # Impresión del artista para verificar que el algoritmo se halla funcionando.
    print(artist)
    
    nombre, nacionalidad = obtener_nacionalidad_artista(artist)
    
    artist_dataset.at[index, "Nombre"] = nombre
    artist_dataset.at[index, "Nacionality"] = nacionalidad
        
# Importación de los resultados.
artist_dataset.to_csv("Datasets/Generados/ArtistsNationalities.csv")