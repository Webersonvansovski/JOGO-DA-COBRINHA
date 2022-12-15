import pygame
from pygame.locals import *
import random

# janela
WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10

# funcção batida
def colisao(pos1, pos2):
    return pos1 == pos2

# batida nas paredes
def fora_limites(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True

# maçã muda de lugar
def random_on_grind():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('COBRINHA')

# cobrinha atributos
snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direcao = K_LEFT

# maçã atributos
apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grind()

# função restart
def restart_jogo():
    global snake_pos
    global apple_pos
    global snake_direcao
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direcao = K_LEFT
    apple_pos = random_on_grind()

# jogo
while True:
    pygame.time.Clock().tick(20)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direcao = event.key

    screen.blit(apple_surface, apple_pos)

    if colisao(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grind()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)


    for i in range(len(snake_pos)-1, 0, -1):
        if colisao(snake_pos[0], snake_pos[i]):
            restart_jogo()
        snake_pos[i] = snake_pos[i-1]

    if fora_limites(snake_pos[0]):
        restart_jogo()

    if snake_direcao == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direcao == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direcao == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direcao == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()

