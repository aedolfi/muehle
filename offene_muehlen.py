from connected import connected, muehlen


for muehl in muehlen:
    for i in range(3):
        for con in connected:
            if muehl[i] in con:
                x=0
                if con[0]==muehl[i]:
                    x=con[1]
                elif con[1]==muehl[i]:
                    x= con[0]
                if not x in muehl:
                    list = []
                    if i==0:
                        list= [muehl[1],muehl[2],x,muehl[i]]
                    if i==1:
                        list= [muehl[0],muehl[2],x,muehl[i]]
                    if i == 2:
                        list= [muehl[0],muehl[1],x,muehl[i]]
                    print(f'{list},')
