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

# Ajustar el tamaño de los sprites (ahora más grandes)
sprite_frente = pygame.transform.scale(sprite_frente, (70, 110))
sprite_espaldas = pygame.transform.scale(sprite_espaldas, (70, 110))
sprite_derecha = pygame.transform.scale(sprite_derecha, (70, 110))
sprite_izquierda = pygame.transform.scale(sprite_izquierda, (70, 110))

# Variables del personaje
pos_x = ancho // 2  # Posición inicial X (centro de la pantalla)
pos_y = 345  # Posición inicial Y (ajustada al escenario)
velocidad = 3  # Velocidad de movimiento
sprite_actual = sprite_frente  # Sprite inicial (mirando al frente)

# Límites del escenario
limite_izquierdo = 0  # Límite izquierdo (extremo de la pantalla)
limite_derecho = ancho - 70  # Límite derecho (extremo menos el ancho del personaje)

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
        if teclas[pygame.K_d] and pos_x < limite_derecho:  # Mover a la derecha
            pos_x += velocidad
            sprite_actual = sprite_derecha
        elif teclas[pygame.K_a] and pos_x > limite_izquierdo:  # Mover a la izquierda
            pos_x -= velocidad
            sprite_actual = sprite_izquierda
        else:
            sprite_actual = sprite_frente  # Si no se mueve, mirar al frente
        if teclas[pygame.K_w]:  # Mirar hacia arriba
            sprite_actual = sprite_espaldas

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
