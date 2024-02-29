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

## English
### What is it?
PyDiscoLeds is a Python program that allows you to create animations with coloured lights using your computer screen. It turns your music into a vibrant and customizable visual spectacle.

### How do I use it?
1. Download and install Python 3 from https://www.python.org/downloads/.
2. Download the PyDiscoLeds code.
3. Save the PyDiscoLeds.py file to a folder on your computer.
4. Open a terminal or command prompt and navigate to the folder where the PyDiscoLeds.py file is located.
5. Install the necessary packages: time and pygame with pip3 install time pygame.
7. Run the python command PyDiscoLeds.py to start the program.
### How do I program it?
PyDiscoLeds uses a simple command language to control the lights. You can create scripts to play different lighting effects in sync with your music.

#### Basic commands:

- colour(color_name, duration, fade_time): display a colour for a set time and then fade to the next colour.
  
Example command sequence:
```
red(2.0, 0.5)
green(1.0, 0.5)
blue(1.0, 0.5)
yellow(2.0, 0.5)
```
This code shows a cycle of colours fading into each other: red for 2 seconds, green for 1 second, blue for 1 second and yellow for 2 seconds, all with a fade of 0.5 seconds.

### How do I play music?
PyDiscoLeds can play music in MP3 format. To add music:

1. Place your MP3 music file in the same folder as the PyDiscoLeds.py file.
2. Modify the musica_path variable in the PyDiscoLeds.py source code to point to the path of your MP3 file.
3. Run the program as described in the "How do I use it?" section.
