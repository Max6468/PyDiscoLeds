import time
import pygame

# Configuración de la pantalla // # Display configuration
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()

# Configuración de la música // # Music settings
pygame.mixer.init()
pygame.mixer.music.load("SONG.mp3")

# Ocultar el cursor del ratón // # Hide the mouse cursor
pygame.mouse.set_visible(False)

# Colores para los efectos de luz // # Colours for light effects
colors = {
  "red": (255, 0, 0),
  "green": (0, 255, 0),
  "blue": (0, 0, 255),
  "yellow": (255, 255, 0),
  "magenta": (255, 0, 255),
  "cyan": (0, 255, 255),
  "white": (255, 255, 255),
  "orange": (255, 165, 0),
  "black": (0, 0, 0)
}

# Función para ejecutar los comandos de luces // # Function for executing light commands
def movingColors(color, duration, fade_duration=0):
  screen.fill(color)
  pygame.display.flip()
  time.sleep(duration)
  fade_start_time = time.time()

  while time.time() - fade_start_time < fade_duration:
    elapsed_time = time.time() - fade_start_time
    faded_color = tuple(int(c * (fade_duration - elapsed_time) / fade_duration) for c in color)
    screen.fill(faded_color)
    pygame.display.flip()
    time.sleep(0.01) # Pequeña pausa para evitar bloquear la CPU // # Small pause to avoid CPU blocking

def execute_light_command(command):
  parts = command.replace(")", "").split("(")
  params = [float(param) for param in parts[1].split(',')]
  duration, fade_duration = params if len(params) == 2 else (params[0], 0.0)
  color = colors[parts[0]]
  movingColors(color, duration, fade_duration)

# Reproducir la música // # Play the music
pygame.mixer.music.play()

# Programar las luces // # Programming the lights
execute_light_command("red(0.0, 2.0)")
execute_light_command("red(2.0, 4.0)")

pygame.mixer.music.stop()
pygame.quit()
