import pygame
import random

# Configuración inicial del juego
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10  # Velocidad del juego

# Colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Derecha por defecto
        self.length = 1

    def move(self):
        # Obtiene la posición actual de la cabeza y calcula la nueva posición
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Verifica colisiones con bordes o consigo misma: si sale de la grilla o se cruza, retorna False
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or 
            new_head in self.positions):
            return False
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def change_direction(self, new_direction):
        # Evita que la serpiente se mueva en dirección opuesta directamente (evita retroceso instantáneo)
        if (new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def grow(self):
        self.length += 1

    def draw(self, screen):
        for x, y in self.positions:
            pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        # Genera una posición aleatoria para la comida dentro de la grilla
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def setup():
    global snake, food, game_over, score
    snake = Snake()
    food = Food()
    game_over = False
    score = 0

def update_loop():
    global game_over, score
    if game_over:
        return

    # Manejo de eventos (cierre de ventana y movimiento)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Actualiza el movimiento de la serpiente
    if not snake.move():
        game_over = True
        return

    # Verifica si la serpiente come la comida
    if snake.positions[0] == food.position:
        snake.grow()
        score += 1
        food.position = food.random_position()

    # Dibuja el fondo y los elementos
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()

def main():
    setup()
    # Bucle principal para mantener el juego en ejecución
    while True:
        update_loop()
        clock.tick(FPS)
        if game_over:
         pygame.quit() #cierra pygame
         break #sale del bucle
if __name__ == "__main__":
    main()