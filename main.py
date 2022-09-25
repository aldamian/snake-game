import pygame

# librării utilizate pentru a crea mâncare la poziții și intervale aleatorii
import random


# inițializare modul pygame
pygame.init()


# definirea culorilor
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# definirea dimensiunilor ferestrei jocului
WIDTH = 600
HEIGHT = 400

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 12

# definirea fontului
message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 25)


def print_score(score):
    value = score_font.render("Your Score: " + str(score), True, ORANGE)
    game_display.blit(value, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, WHITE, [pixel[0],
                         pixel[1], snake_size, snake_size])


def run_game():

    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    # jocul nu începe până când nu apăsăm o tasta
    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    # poziția mâncării
    food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0

    while not game_over:

        # afișarea mesajului de Game Over
        # opțiunea de a juca din nou sau de a ieși
        while game_close:
            game_display.fill(BLACK)
            game_over_message = message_font.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            game_display.blit(game_over_message, [WIDTH / 9, HEIGHT / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        # pierderea jocului dacă șarpele iese din ecran
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(BLACK)
        pygame.draw.rect(game_display, ORANGE, [food_x, food_y,
                                                snake_size, snake_size])

        # adăugare cap, ștergere coadă
        # dacă șarpele mănâncă mâncarea, crește lungimea
        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        # pierderea jocului dacă șarpele se lovește de sine
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        # scadem 1 din scor pentru a nu avea scorul 1 la început
        print_score(snake_length - 1)

        pygame.display.update()

        # logica pentru intracțiunea cu mâncarea
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    run_game()
