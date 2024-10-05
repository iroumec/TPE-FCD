#pip install musicbrainzngs

import musicbrainzngs
import pandas as pd

artist_dataset = pd.read_csv("Track_Dataset.csv")

artistas_unicos = list(artist_dataset["Artist"].unique())

artist_dataset = {"Artista" : artistas_unicos}

artist_dataset = pd.DataFrame.from_dict(artist_dataset)

# Configurar la librería con el nombre del usuario y contacto
musicbrainzngs.set_useragent("TuAplicacion", "1.0", "tu_email@example.com")

def obtener_nacionalidad_artista(nombre_artista):
    try:
        # Buscar al artista por nombre
        resultado = musicbrainzngs.search_artists(artist=nombre_artista)
        
        if resultado['artist-count'] > 0:
            # Tomar el primer resultado que coincida
            artista = resultado['artist-list'][0]
            nombre = artista['name']
            
            # Verificar si hay información sobre la localización/nacionalidad
            if 'country' in artista:
                nacionalidad = artista['country']
                return nombre, nacionalidad
            else:
                return nombre, None
        else:
            return None, None
    
    except Exception as e:
        print(f"Error al obtener la información: {e}")
        return None, None

# Creo una nueva fila para el nombre hallado y la nacionalidad.
artist_dataset["Nombre"] = 'Unknown'
artist_dataset["Nacionality"] = 'Unknown'

for index, artist in enumerate(artist_dataset['Artista']):
    print(index)
    nombre, nacionalidad = obtener_nacionalidad_artista(artist)
    
    artist_dataset.at[index, "Nombre"] = nombre
    artist_dataset.at[index, "Nacionality"] = nacionalidad
        
artist_dataset.to_csv("Datasets/Generados/ArtistsNationalities.csv")