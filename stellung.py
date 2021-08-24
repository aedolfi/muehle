from connected import connected, muehlen, offene_muehlen



def steintostring(i):
    if i==-1:
        return 'X'
    elif i==1:
        return 'O'
    elif i==0:
            return '-'


class muehle():


    def __init__(self, steine=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], phase=1, amzug=1, zuege=0,sieger=0,wert=0):
        self.steine = steine
        self.phase=phase #1: setzen, 2:ziehen
        self.amzug=amzug #1:weiß, -1: schwarz
        self.zuege=zuege
        self.sieger=sieger
        self.wert=wert




    def diesemuehlegibtes(self, muehl, amzug):
        if self.steine[muehl[0]]==amzug and self.steine[muehl[1]]==amzug and self.steine[muehl[2]]==amzug:
            return True
        else:
            return False


    def istteileinermuehle(self, nehmen):
        for muehl in muehlen:
            if self.diesemuehlegibtes(muehl, self.amzug*(-1)) and (nehmen in muehl):
                return True
        else:
            return False


    def muehlegebaut(self, stein, nehmen):
        for muehl in muehlen:
            if self.diesemuehlegibtes(muehl, self.amzug) and (stein in muehl) and not self.istteileinermuehle(nehmen):
                return True
        return False


    def toString(self):
        ausdruck=''
        ausdruck+=f'{steintostring(self.steine[1])}--------{steintostring(self.steine[2])}--------{steintostring(self.steine[3])}\n'
        ausdruck+=f'|        |        |\n'
        ausdruck+=f'|        |        |\n'
        ausdruck+=f'|  {steintostring(self.steine[9])}-----{steintostring(self.steine[10])}-----{steintostring(self.steine[11])}  |\n'
        ausdruck+=f'|  |     |     |  |\n'
        ausdruck+=f'|  |     |     |  |\n'
        ausdruck+=f'|  |  {steintostring(self.steine[17])}--{steintostring(self.steine[18])}--{steintostring(self.steine[19])}  |  |\n'
        ausdruck+=f'|  |  |     |  |  |\n'
        ausdruck+=f'|  |  |     |  |  |\n'
        ausdruck+=f'{steintostring(self.steine[8])}--{steintostring(self.steine[16])}--{steintostring(self.steine[24])}     {steintostring(self.steine[20])}--{steintostring(self.steine[12])}--{steintostring(self.steine[4])}\n'
        ausdruck+=f'|  |  |     |  |  |\n'
        ausdruck+=f'|  |  |     |  |  |\n'
        ausdruck+=f'|  |  {steintostring(self.steine[23])}--{steintostring(self.steine[22])}--{steintostring(self.steine[21])}  |  |\n'
        ausdruck+=f'|  |     |     |  |\n'
        ausdruck+=f'|  |     |     |  |\n'
        ausdruck+=f'|  {steintostring(self.steine[15])}-----{steintostring(self.steine[14])}-----{steintostring(self.steine[13])}  |\n'
        ausdruck+=f'|        |        |\n'
        ausdruck+=f'|        |        |\n'
        ausdruck+=f'{steintostring(self.steine[7])}--------{steintostring(self.steine[6])}--------{steintostring(self.steine[5])}\n'
        ausdruck += f'Phase: {self.phase}, zuege: {self.zuege}, sieger: {self.sieger}, wert: {self.wert} '
        return ausdruck



    def weristsieger(self):
        schwarz=0
        weis=0
        for i in self.steine:
            if i==-1:
                schwarz+=1
            elif i==1:
                weis+=1
        if schwarz <=2:
            return 1
        elif weis <=2:
            return -1
        for con in connected:
            if self.steine[con[0]]==self.amzug and self.steine[con[1]]==0:
                return 0
            if self.steine[con[1]]==0 and self.steine[con[0]]==self.amzug:
                return 0
        return self.amzug*(-1)







    def bewertung(self, manuel=False):
        gewicht_stein=5
        gewicht_zue_muehle=3
        gewicht_offene_muehle=4
        wert=0
        if self.phase==2:
            self.sieger=self.weristsieger()
        if self.sieger!=0:
            return 100000000*self.sieger
        for i in self.steine:
            wert+=gewicht_stein*i
        for muehl in muehlen:
            if self.diesemuehlegibtes(muehl, 1):
                wert += gewicht_zue_muehle
            elif self.diesemuehlegibtes(muehl, -1):
                wert -= gewicht_zue_muehle
        if self.phase==1:
            for farbe in [-1,1]:
                for muehl in muehlen:
                    if muehl[0]==farbe and muehl[1]==farbe and muehl[2]==0:
                        wert += farbe* gewicht_offene_muehle
                    if muehl[0]==farbe and muehl[1]==0 and muehl[2]==farbe:
                        wert += farbe* gewicht_offene_muehle
                    if muehl[0]==0 and muehl[1]==farbe and muehl[2]==farbe:
                        wert += farbe* gewicht_offene_muehle
        if self.phase==2:
            for muehl in offene_muehlen:
                if self.offene_muehle_ist_da(muehl, 1):
                    wert += gewicht_offene_muehle
                if self.offene_muehle_ist_da(muehl, -1):
                    wert -= gewicht_offene_muehle
        return wert


    def offene_muehle_ist_da(self, muehl, farbe):
        if self.steine[muehl[0]]==farbe and self.steine[muehl[1]]==farbe and self.steine[muehl[2]]==farbe and self.steine[muehl[3]]==0:
            return True
        else:
            return False

def ziehen(old, von, nach, nehmen, manuel = False):
    neu= muehle(list(old.steine), int(old.phase), float(old.amzug), int(old.zuege),float(old.sieger),float(old.wert))
    if old.steine[von]==old.amzug and old.steine[nach]==0 and ([min(von,nach),max(von,nach)] in connected):
        neu.steine[von]=0
        neu.steine[nach]=float(old.amzug)
        if(neu.muehlegebaut(nach, nehmen)):
            if manuel:
                print(f'{nach} ist Teil einer Mühle, {nehmen} wird entfernt')
            neu.steine[nehmen]=0
        neu.amzug=float(old.amzug*(-1))
        neu.zuege +=1
        neu.wert=float(neu.bewertung(manuel))
        neu.sieger=float(neu.weristsieger())
        return neu
    else:
        if manuel:
            print('Unzulässiger Zug!')
        if not ([min(von,nach),max(von,nach)] in connected):
            print('Felder sind nicht benachbart')
        if not old.steine[nach]==0:
            print('Zielfeld ist nicht leer')
        if not old.steine[von]==old.amzug :
            print('Du hast keinen Stein auf dem Starfeld')
        return False



def setzen(old, feld, nehmen, manuel=False):
    neu= muehle(list(old.steine), int(old.phase), float(old.amzug), int(old.zuege),float(old.sieger),float(old.wert))
    if old.steine[feld]==0:
        neu.steine[feld]=float(old.amzug)
        if(neu.muehlegebaut(feld, nehmen)):
            if manuel:
                print(f'{feld} ist Teil einer Mühle, {nehmen} wird entfernt')
            neu.steine[nehmen]=0
        neu.amzug=float(old.amzug*(-1))
        neu.zuege +=1
        neu.wert = float(neu.bewertung(manuel))
        if neu.zuege==18:
            neu.phase=2
        return neu
    else:
        if manuel:
            print('Unzulässiger Zug!')
        return False
