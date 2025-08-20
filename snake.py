import pygame
import random

# Configuración inicial del juego
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colores definidos como tuplas
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Diccionario para mapear teclas a direcciones
DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

# Lista para historial de puntajes (global)
score_history = []
game_over = False  # Variable global inicializada

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1
        self.history = []

    def move(self):
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or 
            new_head in self.positions):
            return False
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
        self.history.append(new_head)
        return True

    def change_direction(self, new_direction):
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
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_text(screen, text, x, y, color=WHITE):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))  # Centra el texto
    screen.blit(text_surface, text_rect)

def show_menu(screen, menu_options, title):
    while True:
        screen.fill(BLACK)
        draw_text(screen, title, WIDTH // 2, HEIGHT // 4)  # Título centrado
        for i, option in enumerate(menu_options.keys()):
            draw_text(screen, f"{i + 1}. {option}", WIDTH // 2, HEIGHT // 2 + i * 40)  # Opciones centradas
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and len(menu_options) > 0:
                    return list(menu_options.values())[0]
                elif event.key == pygame.K_2 and len(menu_options) > 1:
                    return list(menu_options.values())[1]
                elif event.key == pygame.K_ESCAPE:
                    return False

def setup():
    global snake, food, score
    snake = Snake()
    food = Food()
    score = 0

def update_loop():
    global game_over, score
    if game_over:
        return

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and event.key in DIRECTIONS:
            snake.change_direction(DIRECTIONS[event.key])

    if not snake.move():
        game_over = True
        return

    if snake.positions[0] == food.position:
        snake.grow()
        score += 1
        food.position = food.random_position()

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    draw_text(screen, f"Puntaje: {score}", 10, 30)
    pygame.display.flip()

def main():
    global game_over
    while True:
        # Menú inicial
        menu_options = {"Iniciar Juego": True, "Salir": False}
        game_over = False  # Reinicia el estado
        choice = show_menu(screen, menu_options, "Menú Principal - Presiona 1 para Iniciar, 2 para Salir")
        if choice is False:
            break

        setup()
        while not game_over:
            update_loop()
            clock.tick(FPS)
        score_history.append(score)  # Añade puntaje al historial
        screen.fill(BLACK)
        draw_text(screen, f"Game Over - Puntaje: {score}", WIDTH // 2, HEIGHT // 2 - 20)
        draw_text(screen, "Historial de Puntajes:", WIDTH // 2, HEIGHT // 2 + 20)
        for i, s in enumerate(score_history[-5:]):  # Muestra los últimos 5 puntajes
            draw_text(screen, f"{i + 1}. {s}", WIDTH // 2, HEIGHT // 2 + 40 + i * 20)
        pygame.display.flip()
        pygame.time.wait(1000)  # Pausa para ver el historial

        # Menú post-juego
        menu_options = {"Volver a Jugar": True, "Salir": False}
        choice = show_menu(screen, menu_options, "Menú Post-Juego - Presiona 1 para Jugar de Nuevo, 2 para Salir")
        if choice is False:
            break
        # Reinicia para volver a jugar
        game_over = False
        setup()  # Llama a setup() para resetear el juego

    pygame.quit()

if __name__ == "__main__":
    main()