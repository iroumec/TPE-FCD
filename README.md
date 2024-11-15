# Introducción

Trabajo Práctico Especial para la materia _Fundamentos de la Ciencia de Datos_.

En este trabajo, se realizó el análisis de un _dataset_ que contiene canciones de la década de 1970 con la finalidad de obtener conclusiones de este. Para ello, se aplicaron los conocimientos adquiridos en la materia. A grandes rasgos, el trabajo realizado contempla:

- La limpieza de la información.
- El estudio (individual y grupal) de las distintas variables.
- El modelado y predicción del conjunto de características.
- La propuesta de hipótesis y su validación.

# Guía de instalación
Guía para descarga del trabajo e instalación de las librerías necesarias.

## Descarga de los archivos necesarios
Se deben descargar los archivos necesarios los cuales están contenidos en el repositorio. Se recomiendan los siguientes métodos.

### Utilizando Git
En este método se utiliza la herramienta Git para clonar el repositorio en el destino deseado.
> [!IMPORTANT]
> No se incluye la [instalación de la herramienta Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) en esta guía, ya que escapa al alcance del trabajo.

Para clonar el repositorio, se debe abrir una terminal, dirigirse a la carpeta en la cual se desea descargar el repositorio y ejecutar el siguiente comando:

```
git clone https://github.com/iroumec/TPE-FCD
```

### Realizando una descarga directa desde el repositorio de GitHUB
Para esto se debe dirigir al [repositorio](https://github.com/iroumec/TPE-FCD) y seguir el siguiente tutorial.

![Gif para mostrar como descargar](Resources/Gifs/descarga_repositorio.gif)

## Creación del ambiente virtual
> [!IMPORTANT]
> No se incluye la [instalación del lenguaje Python](https://www.youtube.com/watch?v=4EGfl6sWQ18) en esta guía, ya que escapa al alcance del trabajo.

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
Con el entorno virtual activo, se deben instalar las dependencias del archivo `requirements.txt` para poder ejecutar la notebook de análisis:

```
pip install -r requirements.txt
```

## Lectura de la notebook de Jupyter
Una vez se ha instalado todo lo necesario, solo resta la lectura del archivo `Notebook.ipynb`. Para esto, se recomiendan los siguientes métodos.

### Utilizando JupyterLab
> [!IMPORTANT]
> No se incluye la [instalación de la herramienta JupyerLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) en esta guía, ya que escapa al alcance del trabajo.

Para utilizar JupyerLab este abre una pestaña en el buscador predeterminado. Para esto se debe ejecutar el siguiente comando:
``` 
jupyter lab
```
> [!WARNING]
> Esto se debe realizar con el ambiente activo para que se detecte correctamente el kernel.

Una vez allí, se debe dirigir al siguiente apartado 

![imagen para explicar como abrir la notebook en jupyter lab](Resources/Images/apartado_jupyterlab.png)

### Utilizando el IDE de Visual Studio Code
> [!IMPORTANT]
> No se incluye la [instalación del IDE Visual Studio code](https://code.visualstudio.com/docs/)

Para utilizar este IDE se deben instalar las extensiones necesarias. Se debe presionar en el ícono de cuadrado en la barra lateral izquierda ![icono de extensión](Resources/Images/icono_extension.png).

Una vez allí, se deben instalar las extensiones Python y Jupyter, ambas publicadas por Microsoft.

![Extensiones necesarias: Jupyter](Resources/Images/extensiones_necesarias_jupyter.png)

![Extensiones necesarias: Python](Resources/Images/extensiones_necesarias_python.png)


Una vez que se han instalado las extensiones necesarias, en el apartado de _"file"_ en la parte superior izquierda, se debe seleccionar la opcion de _"Open Folder"_ y navegar hasta el apartado del proyecto. Es importante que el proyecto y el ambiente se encuentren en la misma carpeta para que este último sea detectado. 
Es posible que el IDE no detecte automaticamente el kernel, por lo que se recomiendo realizas `Ctrl + Shift + P` para mostrar los comandos existentes y seleccionar "Python: Clear Cache and Reload Window".

Finalmente, al tener la carpeta seleccionada, se debe seleccionar el archivo `Notebook.ipynb` y presionar el boton ![boton run all](Resources/Images/run_all.png)

> [!CAUTION]
> Se recomienda encarecidamente la utilización de estos metodos ya que otras plataformas como GitHub no renderizan correctamente los gráficos realizados.

# Tips para la lectura de la notebook.

La notebook cuenta con gráficos interactivos realizados utilizando la libreria `plotly`.

![Gif para utilización de los graficos interactivos](Resources/Gifs/interaccion_grafico.gif)

