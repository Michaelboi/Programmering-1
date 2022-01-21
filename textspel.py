import time


def room1():
    start1 = input('Hallå, välj en dörr för att börja spela mellan (1 eller 2)')
    if start1 == '1':
        time.sleep(1.0)
        answer1 = input('Du ser en hungrig människa som letar efter mat och du måste på något sätt ta dig förbi '
                        'honom.\n'
                        'Du har två alternativ. 1: Ge honom chicken nuggets. 2: Kasta en banan på människan')
        if '2' in answer1:
            room2()
        elif '1' in answer1:
            print('Dina chicken nuggets var frysta och människan kastade tillbaka de på din skalle så du dog.')
            game_over()

    if start1 == '2':
        time.sleep(1.0)
        answer2 = input('Det finns en psykopat som springer mot dig som kommer anfalla dig med en kniv.\n'
                         'Du har två alternativ. 1: Springa iväg. eller 2: Ge honom en present.')
        if '2' in answer2:
            room2()

def room2():
    print('Bra jobbat noob')




def game_over():
    print('Game Over')

room1()
