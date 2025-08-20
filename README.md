# Snake Game Project (Versión Actualizada)

## Descripción del Proyecto
Este es un juego de la serpiente desarrollado en Python utilizando la biblioteca Pygame. El objetivo es controlar una serpiente que crece al comer comida roja, evitando colisiones con los bordes o consigo misma. En esta versión actualizada, se han añadido un menú inicial para iniciar el juego, un menú post-juego para volver a jugar o salir, y un historial de puntajes. El código utiliza estructuras de datos como listas (para posiciones y historial), diccionarios (para mapear teclas a direcciones), y tuplas (para colores y direcciones), manejado a través de funciones modulares.

## Cómo se Juega
- Usa las flechas del teclado (arriba, abajo, izquierda, derecha) para mover la serpiente durante el juego.
- Come la comida roja para aumentar el puntaje y la longitud de la serpiente.
- El juego termina si la serpiente choca con un borde o consigo misma, mostrando el puntaje y el historial.
- Cierra el juego manualmente con la 'X' en la ventana o selecciona "Salir" en los menús.

## Versión de Python
El proyecto fue desarrollado y probado con **Python 3.13.5** (verifica con `python --version` en tu terminal).

## Librerías de Python Instaladas
- **pygame**: Usada para gráficos, eventos y manejo de la ventana del juego (instala con `pip install pygame`).
- **random**: Usada para generar posiciones aleatorias de la comida (incluida con Python).

## Instrucciones de Instalación
1. Asegúrate de tener Python 3.13.5 (o superior) instalado. Verifica con `python --version`.
2. Instala la librería necesaria ejecutando:pip install pygame
3. Descarga o clona este repositorio: git clone https://github.com/Kevin090920/SnakeGameProyect.git
4. Navega a la carpeta del proyecto y ejecuta el juego:cd SnakeGameProject python snake.py

## Estructura del Repositorio
- **/ (raíz)**:
- Contiene todos los archivos principales del proyecto.
- **snake.py**: Archivo principal con el código del juego, incluyendo menús y historial.
- **diagrama 1 actualizado.png a diagrama 5 actualizado.png**: Diagramas de flujo actualizados que ilustran la lógica del juego con menús y historial (Inicio, Movimiento, Comida, Colisiones, Fin).
- **flujo1.png a flujo5.png**: Diagramas originales (opcional, para referencia).
- **README.md**: Este archivo con la documentación del proyecto.

No hay carpetas adicionales en este repositorio por simplicidad.

## Novedades en esta Versión
- **Menú Inicial**: Permite iniciar el juego (opción 1) o salir (opción 2) antes de jugar.
- **Menú Post-Juego**: Ofrece volver a jugar (opción 1) o salir (opción 2) tras terminar.
- **Historial de Puntajes**: Muestra los últimos 5 puntajes al finalizar el juego, almacenados en una lista.
- **Estructuras de Datos**: Uso de diccionarios para mapear teclas, listas para el historial y tuplas para colores/direcciones.
- **Funciones Modulares**: Implementación de `show_menu()`, `setup()`, y `update_loop()` para gestionar la lógica.

## Notas de Desarrollo
Este proyecto fue actualizado como parte de una tarea para incluir estructuras de datos y manejo funcional. Los diagramas de flujo reflejan los nuevos pasos, y el código está optimizado para reiniciar el juego correctamente.