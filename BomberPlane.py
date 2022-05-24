import pygame
import random
import math
import playsound

# bakgrunds musik
playsound('C:\Users\MichaelNwaijah\Downloads\Musik.mp3')

# initsierar pygame.
pygame.init()

# Skapar ett fönster som är 800 * 600
# Bakgrund
screen = pygame.display.set_mode((800, 600))
bakgrund = pygame.image.load('Sky.png')

# Titeln
pygame.display.set_caption('Mitt spel')

# en variabel som fixar kollision problemet för boten
pixel = 64

points = 0

BotImg = []
BotX = []
BotY = []
BotX_change = []
BotY_change = []
antal_botar = 5

# en for loop som appendar in all information i listorna så att alla botar får samma kod
# Botten får ett random x och y värde och har ändringsvärden för x och y
for i in range(antal_botar):
    BotImg.append(pygame.image.load('Botar.png'))
    BotX.append(random.randint(50, 750))
    BotY.append(random.randint(0, 100))
    BotX_change.append(0.4)
    BotY_change.append(30)

# funktion som rendrar in botten på skärmen med blit.
class Bot_spawn:
    def __init__(self, x, y, i):
        screen.blit(BotImg[i], ((x + pixel), y))


spelareX = 320
spelareY = 450

# Kommer göra att man kan röra sig omkring. Spelarens ändrings värden för X och Y
spelareX_change = 0
spelareY_change = 0

# när status = klar så syns skottet inte på skärmen
# när status = skjut så syns skottet på skärmen.
SkottImg = pygame.image.load("skott.png")
SkottX = 0
SkottY = 450
SkottX_change = 0
SkottY_change = 1.5
Skott_status = 'klar'

points_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)
textX = 20
textY = 20

# en funktion som visar poängen som då ökas varje gång man träffar en bot
def visa_poäng(x, y):
    points = font.render('Poäng : ' + str(points_value), True, (0, 0, 0))
    screen.blit(points, (x, y))

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
    # Bakgrund
    screen.blit(bakgrund, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Kollar om knapp är nedtryckt och gör att man kommer kunna röra på spelaren höger/vänster/ner/upp.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spelareX_change += 1
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spelareX_change += -1

            # Anroppar class när knappen E är intryckt
            if event.key == pygame.K_e or event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                if Skott_status == 'klar':
                    SkottX = spelareX
                    Skott(SkottX, SkottY)

        # När man inte trycker på tangenten så slutar den röra på sig.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spelareX_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spelareX_change = 0

    # Gör att den ökar och minskar med ändringsvärden.

    spelareX += spelareX_change

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
    for i in range(antal_botar):
        BotX[i] += BotX_change[i]
        if BotX[i] <= -70:
            BotX_change[i] = 0.5
            BotY[i] += BotY_change[i]
        if BotX[i] >= 680:
            BotX_change[i] = -0.5
            BotY[i] += BotY_change[i]

        # Kollar om den kolliderar för att sen skicka allt till sina start positioner.
        Kollisionen = Kollision(BotX[i], BotY[i], SkottX, SkottY)
        if Kollisionen:
            points_value += 1
            SkottY = 450
            Skott_status = 'klar'
            BotX[i] = random.randint(50, 750)
            BotY[i] = random.randint(0, 100)
        Bot_spawn(BotX[i], BotY[i], i)
    # anroppar på alla ikoner/spelare och botar med deras värden och själva fliken så att de ska uppdatera.

    spelare(spelareX, spelareY)
    visa_poäng(textX, textY)
    pygame.display.update()
