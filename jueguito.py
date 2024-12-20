import pygame
import sys
import time

pygame.init()

# Configuración básica
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Teatro Misterioso")
clock = pygame.time.Clock()

# Configuración de música de fondo
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/musica.mp3")  # Cambia esto por la ruta a tu archivo de música
pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen (0.0 a 1.0)
pygame.mixer.music.play(-1)  # Reproducir en bucle


# Carga de la imagen de fondo
fondo1 = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/fondo.png")
fondo1 = pygame.transform.scale(fondo1, (ancho, alto))

fondo2 = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/camerino.png")
fondo2 = pygame.transform.scale(fondo2, (ancho, alto))

# Pantalla final
pantalla_final = pygame.Surface((ancho, alto))
pantalla_final.fill((0, 0, 0))
fuente_final = pygame.font.Font(None, 50)
texto_final = fuente_final.render("¡Has escapado del teatro!", True, (255, 255, 255))
pantalla_final.blit(texto_final, (200, 300))

# Carga y escalado de los sprites del personaje
sprite_frente = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/frente.png")
sprite_espaldas = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/atras.png")
sprite_derecha = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/derecha.png")
sprite_izquierda = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/izquierda.png")

sprite_size = (40, 70)
sprite_frente = pygame.transform.scale(sprite_frente, sprite_size)
sprite_espaldas = pygame.transform.scale(sprite_espaldas, sprite_size)
sprite_derecha = pygame.transform.scale(sprite_derecha, sprite_size)
sprite_izquierda = pygame.transform.scale(sprite_izquierda, sprite_size)

# Carga de los maniquíes
manmascara = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/manmascara.png")
manrosa = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/manrosa.png")
masvela = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/manvela.png")

manmascara = pygame.transform.scale(manmascara, (70, 100))
manrosa = pygame.transform.scale(manrosa, (70, 100))
masvela = pygame.transform.scale(masvela, (70, 100))

# Posiciones de los maniquíes y luces (En fondo1)
pos_manmascara = (360 - 200, 368)
pos_manrosa = (360, 368)
pos_masvela = (360 + 100 + 120, 358)

# Carga de los objetos
objeto_mascara = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/mascara.png")
objeto_vela = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/vela.png")
objeto_rosa = pygame.image.load("C:/Users/Ebbony G/OneDrive/Documentos/Palmore/Programacion 2/Parcial 3/teatral/rosa.png")

objeto_mascara = pygame.transform.scale(objeto_mascara, (50, 70))
objeto_vela = pygame.transform.scale(objeto_vela, (30, 30))
objeto_rosa = pygame.transform.scale(objeto_rosa, (50, 70))

# Posiciones de los objetos
pos_objeto_vela = (40, 425)  # En fondo1
pos_objeto_mascara = (300, 350)  # En fondo2 (camerino)
pos_objeto_rosa = (450, 350)  # En fondo2 (camerino)

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Fuentes
titulo_fuente = pygame.font.Font(None, 100)
texto_fuente = pygame.font.Font(None, 40)

# Variables del personaje
pos_x = ancho // 2
pos_y = 385
velocidad = 2
sprite_actual = sprite_frente
habitacion_actual = 1

# Inventario
inventario = {
    "mascara": False,
    "vela": False,
    "rosa": False
}

# Seguimiento de interacciones con maniquíes
maniquies_completados = {
    "manmascara": False,
    "manrosa": False,
    "masvela": False
}

# Diálogos y temporizador
dialogos_objetos = {
    "mascara": "El telón se abre con la cara de los sueños.",
    "vela": "La llama marca el final, iluminando el camino de la salida.",
    "rosa": "El corazón de la escena es rojo como el amor y el dolor."
}

dialogos_maniquies = {
    "manmascara": "La verdad se oculta tras una cara. ¿Dónde está la mía? Sin ella, la obra nunca se levantará.",
    "manrosa": "El corazón de la escena late con pasión, pero algo falta… Un símbolo de amor, de tragedia, de deseo.",
    "masvela": "Solo en la oscuridad la luz cobra su verdadero significado. La llama es lo único que ilumina el camino hacia la salida."

}

dialogos_agradecimiento = {
    "manmascara": "La verdad se revela. La escena comienza a cobrar vida. Gracias.",
    "manrosa": "La pasión llena el aire, y el drama comienza. No se como podre pagartelo.",
    "masvela": "La luz se enciende, iluminando la oscuridad, la función está completa. Ten una buena vida"
}

texto_actual = ""
tiempo_mostrar_texto = 0

# Configuración de fuente
fuente = pygame.font.Font(None, 30)

# Función para la pantalla de inicio
def pantalla_inicio():
    while True:
        ventana.fill(NEGRO)

        # Dibujar título
        titulo_texto = titulo_fuente.render("Teatro Misterioso", True, ROJO)
        ventana.blit(titulo_texto, (ancho // 2 - titulo_texto.get_width() // 2, 150))

        # Dibujar texto inicial
        texto_inicial = texto_fuente.render("Despiertas desorientado en un teatro vacío...", True, BLANCO)
        ventana.blit(texto_inicial, (ancho // 2 - texto_inicial.get_width() // 2, 300))

        texto_instrucciones = texto_fuente.render("Presiona Enter para escapar", True, BLANCO)
        ventana.blit(texto_instrucciones, (ancho // 2 - texto_instrucciones.get_width() // 2, 350))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                return

# Función para la pantalla de pausa
def pantalla_pausa():
    while True:
        ventana.fill(NEGRO)

        texto_pausa = titulo_fuente.render("Juego en Pausa", True, BLANCO)
        texto_instrucciones = texto_fuente.render("Presiona ESC para continuar", True, BLANCO)
        
        ventana.blit(texto_pausa, (ancho // 2 - texto_pausa.get_width() // 2, alto // 2 - 50))
        ventana.blit(texto_instrucciones, (ancho // 2 - texto_instrucciones.get_width() // 2, alto // 2 + 50))
        
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return

# Función para mostrar texto con fondo
def mostrar_texto_con_fondo(texto, y=550):
    if texto:
        # Crear un fondo para el texto (rectángulo negro con transparencia)
        texto_superficie = fuente.render(texto, True, (255, 255, 255))
        ancho_texto = texto_superficie.get_width()
        alto_texto = texto_superficie.get_height()

        # Fondo oscuro para el texto
        fondo_texto = pygame.Surface((ancho_texto + 20, alto_texto + 10))
        fondo_texto.set_alpha(200)  # Transparencia en el fondo
        fondo_texto.fill((0, 0, 0))  # Fondo negro

        # Posicionar el fondo y el texto
        ventana.blit(fondo_texto, (20 - 10, y - 5))
        ventana.blit(texto_superficie, (20, y))

# Ajuste para limitar el texto en ancho
def dividir_texto(texto, max_ancho):
    palabras = texto.split(" ")
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if fuente.size(linea_actual + palabra)[0] < max_ancho:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual)
            linea_actual = palabra + " "
    if linea_actual:
        lineas.append(linea_actual)

    return lineas

# Función para mostrar texto ajustado
def mostrar_texto(texto, y=500):
    if texto:
        max_ancho = ancho - 40  # Máximo ancho del texto (con un margen de 20 píxeles a cada lado)
        lineas = dividir_texto(texto, max_ancho)
        # Mostrar cada línea de texto
        for i, linea in enumerate(lineas):
            mostrar_texto_con_fondo(linea, y + (i * 35))



# Función para recoger objetos
def recoger_objeto(objeto):
    global texto_actual, tiempo_mostrar_texto
    inventario[objeto] = True
    texto_actual = dialogos_objetos[objeto]
    tiempo_mostrar_texto = pygame.time.get_ticks()

# Función para interactuar con maniquíes
def interactuar_con_maniqui(maniqui):
    global texto_actual, tiempo_mostrar_texto
    if not inventario["mascara"] and maniqui == "manmascara":
        texto_actual = dialogos_maniquies[maniqui]
    elif not inventario["rosa"] and maniqui == "manrosa":
        texto_actual = dialogos_maniquies[maniqui]
    elif not inventario["vela"] and maniqui == "masvela":
        texto_actual = dialogos_maniquies[maniqui]
    elif inventario["mascara"] and maniqui == "manmascara":
        texto_actual = dialogos_agradecimiento[maniqui]
        maniquies_completados[maniqui] = True
    elif inventario["rosa"] and maniqui == "manrosa":
        texto_actual = dialogos_agradecimiento[maniqui]
        maniquies_completados[maniqui] = True
    elif inventario["vela"] and maniqui == "masvela":
        texto_actual = dialogos_agradecimiento[maniqui]
        maniquies_completados[maniqui] = True
    tiempo_mostrar_texto = pygame.time.get_ticks()

# Función para comprobar si está cerca de un objeto
def cerca_de_objeto(pos_objeto, umbral=50):
    return abs(pos_x - pos_objeto[0]) < umbral and abs(pos_y - pos_objeto[1]) < umbral

# Función para comprobar si está cerca de un maniquí
def cerca_de_maniqui(pos_maniqui, umbral=50):
    return abs(pos_x - pos_maniqui[0]) < umbral and abs(pos_y - pos_maniqui[1]) < umbral

# Función para comprobar si el juego está completo
def juego_completado():
    return all(maniquies_completados.values())

# Bucle principal del juego
# Bucle principal del juego
def bucle_juego():
    global pos_x, sprite_actual, habitacion_actual, texto_actual, tiempo_mostrar_texto
    global sprite_frente, sprite_espaldas, sprite_derecha, sprite_izquierda, sprite_size

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pantalla_pausa()

        teclas = pygame.key.get_pressed()

        # Movimiento del personaje limitado a los laterales
        if teclas[pygame.K_d]:  # Derecha
            pos_x += velocidad
            sprite_actual = sprite_derecha
        elif teclas[pygame.K_a]:  # Izquierda
            pos_x -= velocidad
            sprite_actual = sprite_izquierda
        else:
            sprite_actual = sprite_frente

        # Cambio de habitación
        if pos_x >= ancho and habitacion_actual == 1:
            habitacion_actual = 2
            pos_x = 0
            sprite_size = (sprite_size[0] * 3, sprite_size[1] * 3)  # Triplica el tamaño
            sprite_frente = pygame.transform.scale(sprite_frente, sprite_size)
            sprite_espaldas = pygame.transform.scale(sprite_espaldas, sprite_size)
            sprite_derecha = pygame.transform.scale(sprite_derecha, sprite_size)
            sprite_izquierda = pygame.transform.scale(sprite_izquierda, sprite_size)
        elif pos_x <= 0 and habitacion_actual == 2:
            habitacion_actual = 1
            pos_x = ancho - 1
            sprite_size = (sprite_size[0] // 3, sprite_size[1] // 3)  # Restaura el tamaño original
            sprite_frente = pygame.transform.scale(sprite_frente, sprite_size)
            sprite_espaldas = pygame.transform.scale(sprite_espaldas, sprite_size)
            sprite_derecha = pygame.transform.scale(sprite_derecha, sprite_size)
            sprite_izquierda = pygame.transform.scale(sprite_izquierda, sprite_size)

        # Interacción con objetos y maniquíes
        if teclas[pygame.K_e]:  # Presionar "E" para interactuar
            if habitacion_actual == 1:
                # Interacción con objetos
                if cerca_de_objeto(pos_objeto_vela) and not inventario["vela"]:
                    recoger_objeto("vela")
                # Interacción con maniquíes
                elif cerca_de_maniqui(pos_manmascara):
                    interactuar_con_maniqui("manmascara")
                elif cerca_de_maniqui(pos_manrosa):
                    interactuar_con_maniqui("manrosa")
                elif cerca_de_maniqui(pos_masvela):
                    interactuar_con_maniqui("masvela")
            elif habitacion_actual == 2:
                # Interacción con objetos
                if cerca_de_objeto(pos_objeto_mascara) and not inventario["mascara"]:
                    recoger_objeto("mascara")
                elif cerca_de_objeto(pos_objeto_rosa) and not inventario["rosa"]:
                    recoger_objeto("rosa")

        # Ocultar texto tras 2 segundos
        if texto_actual and pygame.time.get_ticks() - tiempo_mostrar_texto > 2000:
            texto_actual = ""

        # Comprobar si el juego está completo
        if juego_completado():
            ventana.blit(pantalla_final, (0, 0))
            pygame.display.flip()
            time.sleep(3)
            corriendo = False

        # Dibujar habitación
        if habitacion_actual == 1:
            ventana.blit(fondo1, (0, 0))
            if not inventario["vela"]:
                ventana.blit(objeto_vela, pos_objeto_vela)
            ventana.blit(manmascara, pos_manmascara)
            ventana.blit(manrosa, pos_manrosa)
            ventana.blit(masvela, pos_masvela)
        elif habitacion_actual == 2:
            ventana.blit(fondo2, (0, 0))
            if not inventario["mascara"]:
                ventana.blit(objeto_mascara, pos_objeto_mascara)
            if not inventario["rosa"]:
                ventana.blit(objeto_rosa, pos_objeto_rosa)

        # Dibujar personaje y texto
        ventana.blit(sprite_actual, (pos_x, pos_y))
        mostrar_texto(texto_actual)

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

pantalla_inicio()
bucle_juego()
