import pygame
import random

# initsierar pygame.
pygame.init()

# Skapar ett fönster som är 800 * 600
screen = pygame.display.set_mode((800, 600))

# Titeln
pygame.display.set_caption('Mitt spel')

# Spelaren och Botarnas Start koordinater och ändringsvärde för X och Y
BotImg = pygame.image.load('space-invaders.png')
BotX = random.randint(50, 750)
BotY = random.randint(0, 150)
BotX_change = 0.4
BotY_change = 30

class bot_spawn:
    def __init__(self, x, y):
        screen.blit(BotImg, (x, y))

# när status = redo så syns skottet inte på skärmen
# när status = skjut så syns skottet på skärmen.
SkottImg = pygame.image.load('skott.png')
SkottX = 0
SkottY = 450
SkottX_change = 0
SkottY_change = 30
Skott_status = 'klar'

def skott():
    screen.blit(SkottImg, ())

spelareImg = pygame.image.load('Plane2.png')

spelareX = 320
spelareY = 450

# Kommer göra att man kan röra sig omkring. Spelarens ändrings värden för X och Y
spelareX_change = 0
spelareY_change = 0


# Infogar in spelarens ikon och gör att den kan spawna på en viss X och Y koordinat
def spelare(x, y):
    screen.blit(spelareImg, (x, y))


# Kommer göra en oändlig loop som stoppas när fliken stängs genom att man klickar upp på x.
# Den gör att man kan stänga fliken manuellt istället för att den gör det automatiskt och inte fungerar.
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
                spelareX_change += 0.6
            if event.key == pygame.K_LEFT:
                spelareX_change += -0.6



# När man inte trycker på tangenten så slutar den röra på sig.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                spelareX_change = 0
            if event.key == pygame.K_RIGHT:
                spelareX_change = 0
            if event.key == pygame.K_DOWN:
                spelareX_change = 0
            if event.key == pygame.K_UP:
                spelareX_change = 0


# Gör att de ökar och minskar med deras ändringsvärden.

    spelareX += spelareX_change
    BotX += BotX_change


# Vägar som hindrar spelaren från att gå utanför banan och håller den på skärmen.
    if spelareX <= -45:
        spelareX = -45
    if spelareX >= 655:
        spelareX = 655

# Bottarnas Barriärer och ändringsvärden när de nuddar väggen och åker andra hållet.
# Ett stop villkor när en bot nuddar spelaren.
    if BotX <= -10:
        BotX_change = 0.4
        BotY += BotY_change
    if BotX >= 740:
        BotX_change = -0.4
        BotY += BotY_change
    if BotY >= spelareY:
        print('\nGame Over')
        running = False

# anroppar på alla ikoner/spelare och botar med deras värden och själva fliken så att de ska uppdatera.
    bot_spawn(BotX, BotY)
    spelare(spelareX, spelareY)
    pygame.display.update()
