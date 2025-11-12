# BillboardApp

BillboardApp es una aplicación en Python diseñada para analizar y visualizar listas de éxitos musicales (Billboard), tanto en inglés como en español. Permite cargar datos de canciones desde archivos CSV, generar gráficas de popularidad y explorar estadísticas de los artistas y canciones.

## Características

- Lectura y manejo de archivos CSV con información de canciones.
- Gráficas de popularidad por artista, año y género.
- Interfaz gráfica interactiva usando PySimpleGUI o Dash.
- Soporte para grandes listas de canciones (500 canciones incluidas).  
- Exportación de resultados y gráficos.

## Requisitos

Se recomienda crear un entorno virtual e instalar las dependencias usando:

```bash
pip install -r requirements.txt
```

Dependencias principales:

- pandas
- matplotlib
- seaborn
- plotly
- numpy
- PySimpleGUI (opcional)
- dash (opcional)

## Uso

1. Los archivos CSV con las 500 canciones ya están incluidos en la carpeta `data/`.  
   Cada CSV tiene las columnas: `posicion, nombre_cancion, nombre_artista, anio`.
2. Ejecuta el script principal:

```bash
python main.py
```

3. Explora las gráficas y estadísticas generadas.  
4. Si usas la interfaz gráfica, sigue las instrucciones en pantalla.

## Estructura del proyecto

```
BillboardApp/
│
├─ main.py                # Script principal
├─ data/                  # Carpeta con archivos CSV
├─ requirements.txt       # Dependencias del proyecto
├─ README.md              # Este archivo
└─ utils.py               # Funciones auxiliares (lectura, gráficos, etc.)
```

## Mejoras futuras

- Función de búsqueda avanzada por artista o canción.
- Exportar gráficas como imágenes.
- Soporte para más formatos de archivo (Excel, JSON).

## Autores

- Daniel Avellaneda  
- Luis Rico  
- Andrés Vargas
