from stellung import muehle, setzen, ziehen
from automat import automat


def farbe(i):
    if i ==-1:
        return 'Schwarz'
    elif i==1:
        return 'Weiß'
    else:
        return 'FEHLER'

#muehle([0,-1,-1,1,-1,1,1,1,-1,-1,1,-1,1,-1,0,0,1,1,-1,1,0,0,0,0,0],2,1,41,0,9)
smuehle = muehle()
level = int(input('Level 1, 2 oder 3? '))
sautomat = automat(level,-1)

go=True
print('Hallo, lass uns eine Partie Mühle spielen.')

print(smuehle.toString())
while go:
    if smuehle.phase == 1 and smuehle.amzug==1:
        feld = int(input(f'{farbe(smuehle.amzug)}, wohin willst du deinen Stein setzen? ' ))
        nehmen = int(input(f'Falls möglich, welchen Stein möchtest du nehmen? '))
        neu = setzen(smuehle,feld,nehmen,True)
        if neu:
            smuehle=neu
    elif smuehle.phase==2  and smuehle.amzug==1:
        von = int(input(f'{farbe(smuehle.amzug)}, welchen Stein willst du setzen? ' ))
        nach = int(input(f'Wohin willst du den Stein setzen? ' ))
        nehmen = int(input(f'Falls möglich, welchen Stein möchtest du nehmen? '))
        neu =ziehen( smuehle,von, nach, nehmen,True)
        if neu:
            smuehle=neu
    elif smuehle.amzug==-1:
        smuehle= sautomat.zug(smuehle)
    print(smuehle.toString())
    if smuehle.sieger!=0:
        print(f'Glückwunsch {farbe(smuehle.sieger)}, du hast gewonnen!')
        inp= input('Willst du noch ein Spiel spielen? (J/N) ')
        if inp.lower()=='j':
            smuehle = muehle()
            level = int(input('Level 1, 2 oder 3? '))
            sautomat = automat(level,-1)
        else:
            go=False
