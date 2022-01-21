# Det här är en miniräknare som just nu inte har roten ur.
# Funktionen gör att jag kan använda if till att göra så att man kan välja räknesättet man vill ha.
# räknesätt är då det som tar in input och kollar om det är likadant som räknesätten.

import math

print('addition, subtraktion, multiplikation, division, upphöjt till, roten')
# noinspection NonAsciiCharacters
räknesätt = input('välj ett räknesätt ')


def miniräknare():

    while räknesätt != 'stop':
        if räknesätt == 'addition':
            tal1 = float(input('Tal 1 '))
            tal2 = float(input('Tal 2 '))
            print(tal1 + tal2)


        if räknesätt == 'subtraktion':
            tal1 = float(input('Tal 1 '))
            tal2 = float(input('Tal 2 '))
            print(tal1 - tal2)

        if räknesätt == 'multiplikation':
            tal1 = float(input('Tal 1 '))
            tal2 = float(input('Tal 2 '))
            print(tal1 * tal2)

        if räknesätt == 'division':
            tal1 = float(input('Täljare '))
            tal2 = float(input('Nämnare '))
            print(tal1 / tal2)

        if räknesätt == 'upphöjt till':
            tal1 = float(input('Bas '))
            tal2 = float(input('Exponent '))
            print(tal1 ** tal2)

        if räknesätt == 'roten':
            tal1 = float(input('Tal 1 '))
            print(math.sqrt(tal1))




miniräknare()
