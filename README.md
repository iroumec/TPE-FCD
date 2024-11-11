# Introduccion

Trabajo Práctico Especial para la materia _Fundamentos de la Ciencia de Datos_.

En este trabajo, se realizó el análisis de un _dataset_ que contiene canciones de la década de 1970 con la finalidad de obtener conclusiones de este. Para ello, se aplicaron los conocimientos adqueridos en la materia. A grandes rasgos, el trabajo realizado contempla:

- La limpieza de la información.
- El estudio (individual y grupal) de las distintas variables.
- El modelado y predicción del conjunto de características.
- La propuesta de hipótesis y su validación.

# Guia de instalacion
Guia para descarga del trabajo e instalacion de las librerias necesarias.

## Descarga de los archivos necesarios
Se deben descargar los archivos necesarios los cuales están contenido es en el repositorio. Se recomiendan los siguientes metodos.

### Utilizando GIT
En este método se utiliza la herramienta GIT para clonar el repositorio en el destino deseado.
> [!IMPORTANT]
> No se incluye la [instalación de la herramienta Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) en esta guía, ya que escapa al alcance del trabajo.

Para clonar el repositorio, se debe abrir una terminal, dirigirse a la carpeta en la cual se desea descargar el repositorio y ejecutar el siguiente comando:

```
git clone https://github.com/iroumec/TPE-FCD
```

### Realizando una descarga directa desde el repositorio de GitHUB
Para esto se debe dirigir al [repositorio](https://github.com/iroumec/TPE-FCD) y seguir el siguiente tutorial.

!!!! GIF !!!!!!!!!

## Creacion del ambiente virtual
Para asegurar que las dependencias se instalen correctamente y evitar conflictos entre versiones, se recomienda crear un entorno virtual. Desde la terminal, se debe navegar a la carpeta del proyecto y ejecutar:

```
python -m venv env

```
Activación del entorno virtual

En Linux o Mac:

```
source env/bin/activate
```
En Windows:

```
.\env\Scripts\activate
```

## Instalación de dependencias
Con el entorno virtual activo, se deben instala las dependencias del archivo requirements.txt para poder ejecutar la notebook de análisis:

```
pip install -r requirements.txt
```











