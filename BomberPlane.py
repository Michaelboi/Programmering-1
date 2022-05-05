import pygame
import random
import math

# initsierar pygame.
pygame.init()

# Skapar ett fönster som är 800 * 600
screen = pygame.display.set_mode((800, 600))

# Titeln
pygame.display.set_caption('Mitt spel')

# Spelaren och Botarnas Start koordinater och ändringsvärde för X och Y
BotImg = pygame.image.load('Botar.png')
pixel = 64
BotX = random.randint(50, 750)
BotY = random.randint(0, 150)
BotX_change = 0.4
BotY_change = 30


# Gör en hitbox för botten


class Bot_spawn:
    def __init__(self, x, y):
        screen.blit(BotImg, ((x + pixel), y))


spelareX = 320
spelareY = 450

# Kommer göra att man kan röra sig omkring. Spelarens ändrings värden för X och Y
spelareX_change = 0
spelareY_change = 0

# när status = redo så syns skottet inte på skärmen
# när status = skjut så syns skottet på skärmen.
SkottImg = pygame.image.load("skott.png")
SkottX = 0
SkottY = 450
SkottX_change = 0
SkottY_change = 1.5
Skott_status = 'klar'


# Skottets funktion för att få med den på skärmen och se till att när villkoret är uppfyllt så används funktionen
class Skott:
    def __init__(self, x, y):
        global Skott_status
        Skott_status = 'skjut'
        screen.blit(SkottImg, (x + 77, y + 60))


# Infogar in spelarens ikon och gör att den kan spawna på en viss X och Y koordinat
class spelare:
    def __init__(self, x, y):
        self.image = pygame.image.load('Plane2.png')
        screen.blit(self.image, (x, y))


# Kollar om den kolliderar, den räknar ut avståndet mellan skottet och botten med avståndsformel
def Kollision(BotX, BotY, SkottX, SkottY):
    avstånd = math.sqrt((math.pow(BotX - SkottX, 2)) + (math.pow(BotY - SkottY, 2)))
    if avstånd < 27:
        return True
    else:
        return False


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
                spelareX_change += 1
            if event.key == pygame.K_LEFT:
                spelareX_change += -1

            # Anroppar class när knappen E är intryckt
            if event.key == pygame.K_e:
                if Skott_status == 'klar':
                    SkottX = spelareX
                    Skott(SkottX, SkottY)

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

    # Skottets rörelse/movement, den kollar om skottens status är skjut så att den kan anropa funktionen.
    if Skott_status == 'skjut':
        Skott(SkottX, SkottY)
        SkottY -= SkottY_change
    if SkottY <= -100:
        Skott_status = 'klar'
        SkottY = 450

    # Bottarnas Barriärer och ändringsvärden när de nuddar väggen och åker andra hållet.
    # Ett stop villkor när en bot nuddar spelaren.
    if BotX <= -70:
        BotX_change = 0.4
        BotY += BotY_change
    if BotX >= 680:
        BotX_change = -0.4
        BotY += BotY_change
    if BotY >= spelareY:
        print('\nGame Over')
        running = False
    # Kollar om den kolliderar för att sen skicka allt till sina start positioner.
    Kollisionen = Kollision(BotX, BotY, SkottX, SkottY)
    if Kollisionen:
        SkottY = 450
        Skott_status = 'klar'
        BotX = random.randint(50, 750)
        BotY = random.randint(0, 150)

    # anroppar på alla ikoner/spelare och botar med deras värden och själva fliken så att de ska uppdatera.
    Bot_spawn(BotX, BotY)
    spelare(spelareX, spelareY)
    pygame.display.update()
