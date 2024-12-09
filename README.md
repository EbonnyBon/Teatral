
# Teatro Misterioso 🎭

**Teatro Misterioso** es un juego de aventura 2D desarrollado en Python utilizando la librería Pygame. Los jugadores se encuentran atrapados en un teatro abandonado lleno de maniquíes enigmáticos y objetos misteriosos. Tu misión es interactuar con el entorno, resolver acertijos y escapar.

---

## 🎮 Cómo jugar

### Historia:
Despiertas desorientado en un teatro vacío y extraño. A medida que exploras, descubres maniquíes que parecen cobrar vida al recuperar ciertos objetos perdidos. Para escapar, debes devolver los objetos correctos a cada maniquí y descubrir el secreto del teatro.

### Controles:
- **Moverse a la izquierda:** Presiona la tecla `A`.
- **Moverse a la derecha:** Presiona la tecla `D`.
- **Interactuar con objetos o maniquíes:** Presiona la tecla `E`.
- **Pausar el juego:** Presiona la tecla `ESC`.
- **Salir del juego:** Cierra la ventana del programa.

### Objetivo:
1. Explora las dos habitaciones del teatro.
2. Encuentra y recoge los objetos clave: una máscara, una vela y una rosa.
3. Devuélvelos a los maniquíes correctos según las pistas que ofrecen.
4. Una vez que todos los maniquíes estén completos, escaparás del teatro.

---

## 🛠️ Instalación

### Prerrequisitos:
Asegúrate de tener instalado lo siguiente en tu sistema:
1. **Python 3.x**: Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).
2. **Pygame**: Instala Pygame ejecutando el siguiente comando:
   ```bash
   pip install pygame
   ```

### Pasos de Instalación:
1. Clona este repositorio o descarga los archivos del juego:
   ```bash
   git clone https://github.com/tuusuario/teatro-misterioso.git
   cd teatro-misterioso
   ```
2. Asegúrate de que las rutas de los archivos de recursos (música, imágenes) en el código sean correctas según tu sistema.
3. Inicia el juego ejecutando el siguiente comando:
   ```bash
   python teatro_misterioso.py
   ```

---

## 📂 Estructura del proyecto

```plaintext
teatro-misterioso/
├── assets/                 # Carpeta con recursos del juego
│   ├── musica.mp3          # Música de fondo
│   ├── fondo.png           # Fondo de la habitación principal
│   ├── camerino.png        # Fondo de la segunda habitación
│   ├── frente.png          # Sprite del personaje (frontal)
│   ├── atras.png           # Sprite del personaje (espaldas)
│   ├── derecha.png         # Sprite del personaje (derecha)
│   ├── izquierda.png       # Sprite del personaje (izquierda)
│   ├── manmascara.png      # Imagen del maniquí con máscara
│   ├── manrosa.png         # Imagen del maniquí con rosa
│   ├── manvela.png         # Imagen del maniquí con vela
│   ├── mascara.png         # Objeto máscara
│   ├── rosa.png            # Objeto rosa
│   └── vela.png            # Objeto vela
├── teatro_misterioso.py    # Código principal del juego
└── README.md               # Este archivo
```

---

## 📝 Notas del desarrollo

- El juego utiliza sprites simples para representar al personaje y los elementos.
- Las rutas de los archivos deben configurarse correctamente para evitar errores al cargar recursos.
- El diseño visual y el código están optimizados para resoluciones de 800x600 píxeles.

---

## 🏆 Créditos

**Desarrollador:** Ebonny Guigón
**Herramientas utilizadas:** Python y Pygame.
