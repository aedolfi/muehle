from stellung import muehle, setzen, ziehen
from connected import connected

class automat():

    def __init__(self, depth, farbe):
        self.farbe=farbe
        self.depth=depth


    def zug(self, muehle):
        muehlen=[]
        if muehle.phase==1:
            for feld in range(1,25):
                if muehle.steine[feld]==0:
                    if muehle.zuege>0:
                        for nehmen in range(1,25):
                            if muehle.steine[nehmen]==self.farbe*(-1):
                                neu = setzen(muehle,feld,nehmen)
                                if neu != False :
                                    muehlen.append([self.calc(neu,self.depth-1,self.farbe*(-1)),feld,nehmen])
            for objekt in muehlen:
                if not objekt[0]:
                    muehlen.remove(objekt)
            muehlen = sorted(muehlen, key=lambda muehle: muehle[0].wert )
            if self.farbe==1:
                return setzen(muehle,muehlen[len(muehlen)-1][1],muehlen[len(muehlen)-1][2], True)
            elif self.farbe==-1:
                return setzen(muehle,muehlen[0][1],muehlen[0][2],True)
        elif muehle.phase==2:
            for con in connected:
                if muehle.steine[con[0]]==self.farbe and muehle.steine[con[1]]==0:
                    for nehmen in range(1,25):
                        if muehle.steine[nehmen]==self.farbe*(-1):
                            neu = ziehen(muehle,con[0],con[1],nehmen)
                            if neu!=False:
                                muehlen.append([self.calc(neu,self.depth-1,self.farbe*(-1)),con[0],con[1],nehmen])
                if muehle.steine[con[1]]==self.farbe and muehle.steine[con[0]]==0:
                    for nehmen in range(1,25):
                        if muehle.steine[nehmen]==self.farbe*(-1):
                            neu = ziehen(muehle,con[1],con[0],nehmen)
                            if neu!= False:
                                muehlen.append([self.calc(neu,self.depth-1,self.farbe*(-1)),con[1],con[0],nehmen])
            for objekt in muehlen:
                if not objekt[0]:
                    muehlen.remove(objekt)
            muehlen = sorted(muehlen, key=lambda muehle: muehle[0].wert )
            if self.farbe==1:
                return ziehen(muehle,muehlen[len(muehlen)-1][1],muehlen[len(muehlen)-1][2],muehlen[len(muehlen)-1][3], True)
            elif self.farbe==-1:
                return ziehen(muehle,muehlen[0][1],muehlen[0][2],muehlen[0][3], True)

    def calc(self, muehle, i, farbe):
        if i== 0:
            return muehle
        elif i>0:
            muehlen=[]
            if muehle !=False:
                if muehle.phase==1:
                    for feld in range(1,25):
                        if muehle.steine[feld]==0:
                            if muehle.zuege>0:
                                for nehmen in range(1,25):
                                    if muehle.steine[nehmen]==farbe*(-1):
                                        neu = setzen(muehle,feld,nehmen)
                                        if neu !=False:
                                            muehlen.append(self.calc(neu,i-1,farbe*(-1)))
                elif muehle.phase==2:
                    for con in connected:
                        if muehle.steine[con[0]]==farbe and muehle.steine[con[1]]==0:
                            for nehmen in range(1,25):
                                if muehle.steine[nehmen]==farbe*(-1):
                                    neu = ziehen(muehle,con[0],con[1],nehmen)
                                    if neu != False:
                                        muehlen.append(self.calc(neu,i-1,farbe*(-1)))
                        if muehle.steine[con[1]]==farbe and muehle.steine[con[0]]==0:
                            for nehmen in range(1,25):
                                if muehle.steine[nehmen]==farbe*(-1):
                                    neu = ziehen(muehle,con[1],con[0],nehmen)
                                    if neu!= False:
                                        muehlen.append(self.calc(neu,i-1,farbe*(-1)))
                muehlen = filter(None, muehlen) #returns filter object
                muehlen = sorted(muehlen, key=lambda muehle: muehle.wert ) # returns list
                if muehlen:
                    if farbe==1:
                        return muehlen[len(muehlen)-1]
                    elif farbe==-1:
                        return muehlen[0]
