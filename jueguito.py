import pygame
import sys

pygame.init()

# Configuración básica
ancho, alto = 800, 600  # Tamaño de la ventana
ventana = pygame.display.set_mode((ancho, alto))  # Crear la ventana
pygame.display.set_caption("Teatro Misterioso")  # Título de la ventana
clock = pygame.time.Clock()  # Controla los FPS

# Carga de imágenes
fondo = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/fondo.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))  # Escalar fondo al tamaño de la ventana

# Cargar sprites del personaje
sprite_frente = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/frente.png")
sprite_espaldas = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/atras.png")
sprite_derecha = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/derecha.png")
sprite_izquierda = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/izquierda.png")

# Ajustar el tamaño de los sprites
sprite_frente = pygame.transform.scale(sprite_frente, (50, 80))
sprite_espaldas = pygame.transform.scale(sprite_espaldas, (50, 80))
sprite_derecha = pygame.transform.scale(sprite_derecha, (50, 80))
sprite_izquierda = pygame.transform.scale(sprite_izquierda, (50, 80))

# Variables del personaje
pos_x = ancho // 2  # Posición inicial X (centro de la pantalla)
pos_y = 450  # Posición inicial Y (en el escenario)
velocidad = 5  # Velocidad de movimiento
sprite_actual = sprite_frente  # Sprite inicial (mirando al frente)

# Límites del escenario
limite_izquierdo = 150  # Límite izquierdo
limite_derecho = 650  # Límite derecho

# Bucle principal
def bucle_juego():
    global pos_x, sprite_actual
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Salir del juego
                corriendo = False

        # Detectar teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT] and pos_x < limite_derecho:  # Mover a la derecha
            pos_x += velocidad
            sprite_actual = sprite_derecha
        elif teclas[pygame.K_LEFT] and pos_x > limite_izquierdo:  # Mover a la izquierda
            pos_x -= velocidad
            sprite_actual = sprite_izquierda
        else:
            sprite_actual = sprite_frente  # Si no se mueve, mirar al frente

        # Dibujar todo
        ventana.blit(fondo, (0, 0))  # Dibujar el fondo
        ventana.blit(sprite_actual, (pos_x, pos_y))  # Dibujar al personaje

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)  # Mantener 60 FPS

    pygame.quit()  # Salir de Pygame
    sys.exit()  # Cerrar el programa

# Iniciar el juego
bucle_juego()
