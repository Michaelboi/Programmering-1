import pygame
import random


# initsierar pygame.
pygame.init()

# Skapar ett fönster
screen = pygame.display.set_mode((800, 600))

# Titeln
pygame.display.set_caption('Mitt jspel')

# Spelaren och Botarna
BotImg = pygame.image.load('space-invaders.png')
BotX = [7,8]

class bot_spawn:
    def __init__(self):
        pass

spelareImg = pygame.image.load('Plane2.png')
spelareX = 320
spelareY = 390

# Kommer göra att man kan röra sig omkring.
spelareX_change = 0
spelareY_change = 0

# Botar
def botar(x, y):
    screen.blit(botImg)


def spelare(x, y):
    screen.blit(spelareImg, (x, y))


# Kommer göra en oändlig loop som stoppas när fliken stängs.
# Den gör att man kan stänga fliken manuellt.
running = True
while running:
    # RGB = Röd, Blå, Grön
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Kollar om knapp är nedtryckt och gör att man kommer kunna röra på spelaren höger/vänster/ner/upp.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spelareX_change += 0.5
            if event.key == pygame.K_LEFT:
                spelareX_change += -0.5
            if event.key == pygame.K_UP:
                spelareY_change += -0.5
            if event.key == pygame.K_DOWN:
                spelareY_change += 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                    event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                spelareX_change = 0
                spelareY_change = 0

    spelareY += spelareY_change
    spelareX += spelareX_change

    if spelareX <=-45:
        spelareX = -45
    if spelareX >=655:
        spelareX = 655
    if spelareY >= 470:
        spelareY = 470
    if spelareY <= -40:
        spelareY = -40

    spelare(spelareX, spelareY)
    pygame.display.update()

