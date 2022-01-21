sida1 = float(input('välj längd för sida1'))
sida2 = float(input('välj längd för sida2'))

def beräknaArea():
    if (sida1 < 0):
        print('sida1 måste vara större än 0')
    if (sida2 < 0):
        print('sida2 måste vara större än 0')
        area = sida1*sida2

        print(area)

beräknaArea()
