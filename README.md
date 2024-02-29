# PyDiscoLeds

## Español
### ¿Qué es?
PyDiscoLeds es un programa hecho en Python que te permite crear animaciones con luces de colores utilizando la pantalla de tu ordenador. Convierte tu música en un espectáculo visual vibrante y personalizable.

### ¿Cómo lo uso?
1. Descarga e instala Python 3 desde https://www.python.org/downloads/.
2. Descarga el código de PyDiscoLeds.
3. Guarda el archivo PyDiscoLeds.py en una carpeta de tu ordenador.
4. Abre una terminal o símbolo del sistema y navega hasta la carpeta donde se encuentra el archivo PyDiscoLeds.py.
5. Instala los paquetes necesarios: time y pygame con pip3 install time pygame
7. Ejecuta el comando python PyDiscoLeds.py para iniciar el programa.
### ¿Cómo lo programo?
PyDiscoLeds usa un lenguaje de comandos simple para controlar las luces. Puedes crear secuencias de comandos para reproducir diferentes efectos de iluminación en sincronía con tu música.

#### Comandos básicos:

- color(nombre_color, duración, tiempo_de_desvanecimiento): Muestra un color durante un tiempo determinado y luego se desvanece al siguiente color.
  
Ejemplo de secuencia de comandos:
```
rojo(2.0, 0.5)
verde(1.0, 0.5)
azul(1.0, 0.5)
amarillo(2.0, 0.5)
```
Este código muestra un ciclo de colores que se desvanecen entre sí: rojo durante 2 segundos, verde durante 1 segundo, azul durante 1 segundo y amarillo durante 2 segundos, todos con un desvanecimiento de 0.5 segundos.

### ¿Cómo pongo la música?
PyDiscoLeds puede reproducir música en formato MP3. Para agregar música:

1. Coloca tu archivo de música MP3 en la misma carpeta que el archivo PyDiscoLeds.py.
2. Modifica la variable musica_path en el código fuente de PyDiscoLeds.py para que apunte a la ruta de tu archivo MP3.
3. Ejecuta el programa como se describe en la sección "¿Cómo lo uso?".
