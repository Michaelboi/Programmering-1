form = input('Vilken figur vill vill beräkna med?')

def beräknaArea():



    if form == 'kvadrat':
        bas = float(input())
        höjd = float(input())
        print(bas*höjd)

        if form == 'rektangel':
            bas = float(input())
            höjd = float(input())
            print(bas * höjd)

    if form == 'triangel':
        bas = float(input())
        höjd = float(input())
        print(bas*höjd/2)

    if form == 'cirkel':
        radie = float(input())
        pi = float(input('pi'))
        print(radie**2*pi)


beräknaArea()