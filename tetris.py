from tkinter import*
from turtle import*
from random import*
from time import*
from keyboard import*
from winsound import*
from threading import*
import pyrebase
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
def nacrtajpolje(t,sirinabloka):
    for i in range(21):
        t.pu()
        t.goto(-5*sirinabloka,(10-i)*sirinabloka)
        t.pd()
        t.fd(10*sirinabloka)
    t.rt(90)
    for i in range(12):
        t.pu()
        t.goto((-5+i)*sirinabloka,10*sirinabloka)
        t.pd()
        t.fd(20*sirinabloka)
def pocetak(prozor,canvas,screen,t,sirinabloka):
    canvas.pack()
    t.hideturtle()
    t.pensize(3)
    screen.tracer(0)
    prozor.config(width=10*sirinabloka,height=20*sirinabloka)
def provjera(prozor,polja,sirinabloka,poljaslike,padajuce):
    for c in padajuce:
        if c[0]==19 or (((c[0]+1),c[1]) not in padajuce and polja[c[0]+1][c[1]]!=0):
            return True
    return False
def noviprovjera(polja):
    for i in range(2):
        for j in range(3,7):
            if polja[i][j]==1:
                return False
    return True
def provjeralijevo(prozor,polja,sirinabloka,poljaslike,padajuce):
    for c in padajuce:
        if c[1]<=0 or ((c[0],(c[1]-1)) not in padajuce and polja[c[0]][c[1]-1]!=0):
            return False
    return True
def provjeradesno(prozor,polja,sirinabloka,poljaslike,padajuce):
    for c in padajuce:
        if c[1]>=9 or ((c[0],(c[1]+1)) not in padajuce and polja[c[0]][c[1]+1]!=0):
            return False
    return True
def dodajnovo(prozor,polja,sirinabloka,poljaslike,padajuce,polozaj,nextslike):
    global oblici
    global nextup
    oblici.append(randint(0,6))
    random_shape=oblici.pop(0)
    nextup.config(image=nextslike[oblici[0]])
    if random_shape==0:
        polozaj+=(0,4,0)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        for i in range(4):
            noviblokovi[i].pack()
            noviblokovi[i].place(x=200*(3/4)+(3+i)*sirinabloka,y=0*sirinabloka)
            poljaslike[0][3+i]=noviblokovi[i]
            polja[0][3+i]=2
            padajuce.append((0,3+i))
    elif random_shape==1:
        polozaj+=(1,4,1)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        noviblokovi[0].pack()
        noviblokovi[0].place(x=200*(3/4)+3*sirinabloka,y=0*sirinabloka)
        poljaslike[0][3]=noviblokovi[0]
        polja[0][3]=2
        padajuce.append((0,3))
        for i in range(3):
            noviblokovi[i+1].pack()
            noviblokovi[i+1].place(x=200*(3/4)+(3+i)*sirinabloka,y=1*sirinabloka)
            poljaslike[1][3+i]=noviblokovi[i+1]
            polja[1][3+i]=2
            padajuce.append((1,3+i))
    elif random_shape==2:
        polozaj+=(1,4,2)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        noviblokovi[0].pack()
        noviblokovi[0].place(x=200*(3/4)+5*sirinabloka,y=0*sirinabloka)
        poljaslike[0][5]=noviblokovi[0]
        polja[0][5]=2
        padajuce.append((0,5))
        for i in range(3):
            noviblokovi[i+1].pack()
            noviblokovi[i+1].place(x=200*(3/4)+(3+i)*sirinabloka,y=1*sirinabloka)
            polja[1][3+i]=2
            poljaslike[1][3+i]=noviblokovi[i+1]
            padajuce.append((1,3+i))
    elif random_shape==3:
        polozaj+=(0,4,3)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        brojac=0
        for i in range(2):
            for j in range(2):
                noviblokovi[brojac].pack()
                noviblokovi[brojac].place(x=200*(3/4)+(4+j)*sirinabloka,y=i*sirinabloka)
                polja[i][4+j]=2
                poljaslike[i][4+j]=noviblokovi[brojac]
                padajuce.append((j,4+i))
                brojac+=1
    elif random_shape==4:
        polozaj+=(1,4,4)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        for i in range(2):
            noviblokovi[i].pack()
            noviblokovi[i].place(x=200*(3/4)+(4+i)*sirinabloka,y=0*sirinabloka)
            poljaslike[0][4+i]=noviblokovi[i]
            polja[0][4+i]=2
            padajuce.append((0,4+i))
        for i in range(2):
            noviblokovi[2+i].pack()
            noviblokovi[2+i].place(x=200*(3/4)+(3+i)*sirinabloka,y=1*sirinabloka)
            poljaslike[1][3+i]=noviblokovi[2+i]
            polja[1][3+i]=2
            padajuce.append((1,3+i))
    elif random_shape==5:
        polozaj+=(1,4,5)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        for i in range(2):
            noviblokovi[i].pack()
            noviblokovi[i].place(x=200*(3/4)+(3+i)*sirinabloka,y=0*sirinabloka)
            poljaslike[0][3+i]=noviblokovi[i]
            polja[0][3+i]=2
            padajuce.append((0,3+i))
        for i in range(2):
            noviblokovi[2+i].pack()
            noviblokovi[2+i].place(x=200*(3/4)+(4+i)*sirinabloka,y=1*sirinabloka)
            poljaslike[1][4+i]=noviblokovi[2+i]
            polja[1][4+i]=2
            padajuce.append((1,4+i))
    elif random_shape==6:
        polozaj+=(1,4,6)
        boja=slike[random_shape]
        noviblokovi=[Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja),Label(prozor,image=boja)]
        noviblokovi[0].pack()
        noviblokovi[0].place(x=200*(3/4)+4*sirinabloka,y=0*sirinabloka)
        polja[0][4]=2
        poljaslike[0][4]=noviblokovi[0]
        padajuce.append((0,4))
        for i in range(3):
            noviblokovi[i+1].pack()
            noviblokovi[i+1].place(x=200*(3/4)+(3+i)*sirinabloka,y=1*sirinabloka)
            polja[1][3+i]=2
            poljaslike[1][3+i]=noviblokovi[i+1]
            padajuce.append((1,3+i))
def padanje(poljaslike,polja,padajuce,sirinabloka,polozaj):
    padajuce.sort(key=lambda t:t[0],reverse=True)
    for i in range(4):
        xx=padajuce[0][0]
        yy=padajuce[0][1]
        slika=poljaslike[xx][yy]
        slika.place(x=200*(3/4)+yy*sirinabloka,y=(xx+1)*sirinabloka)
        padajuce.append((xx+1,yy))
        padajuce.pop(0)
        poljaslike[xx+1][yy]=slika
        polja[xx+1][yy]=2
        poljaslike[xx][yy]=None
        polja[xx][yy]=0
    polozaj[0]+=1
def okretanje(prozor,polja,sirinabloka,polozaj,poljaslike):
    if polozaj[2]==3:
        return
    else:
        if polozaj[2]==0:
            a=4
            b=1
        else:
            a=3
            b=0
    moze=True
    moze2=True
    if polozaj[1]<=b:
        if provjeradesno(prozor,polja,sirinabloka,poljaslike,padajuce):
            micanjedesno(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
            if polozaj[2]==0 and polozaj[1]<=1:
                if provjeradesno(prozor,polja,sirinabloka,poljaslike,padajuce):
                    micanjedesno(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
                else:
                    micanjelijevo(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
                    moze2=False
        else:
            moze2=False
    if polozaj[1]>=9-b:
        if provjeralijevo(prozor,polja,sirinabloka,poljaslike,padajuce):
            micanjelijevo(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
            if polozaj[2]==0 and polozaj[1]>=8:
                if provjeralijevo(prozor,polja,sirinabloka,poljaslike,padajuce):
                    micanjelijevo(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
                else:
                   micanjedesno(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
                   moze2=False
        else:
            moze2=False
    if polozaj[0]<19-b and moze2:
        if polozaj[0]==0:
            padanje(poljaslike,polja,padajuce,sirinabloka,polozaj)
        novapolja=[[0 for i in range(a)] for j in range(a)]
        novapoljaslike=[[None for i in range(a)] for j in range(a)]
        for i in range(a):
            for j in range(a):
                if polja[polozaj[0]+i-1][polozaj[1]+j-1]==1:
                    novapolja[i][j]=1
                    if novapolja[j][a-1-i]!=1:
                        novapolja[j][a-1-i]=0
                    novapoljaslike[i][j]=poljaslike[polozaj[0]+i-1][polozaj[1]+j-1]
                else:
                    if novapolja[j][a-1-i]!=1:
                        novapolja[j][a-1-i]=polja[polozaj[0]+i-1][polozaj[1]+j-1]
                    if novapolja[j][a-1-i]==2:
                        novapoljaslike[j][a-1-i]=poljaslike[polozaj[0]+i-1][polozaj[1]+j-1]
        br2=0
        for i in range(a):
            for j in range(a):
                if novapolja[i][j]==2:
                    br2+=1
            
        if br2!=4:
            moze=False
        if moze:
            br=-1
            padajuce.clear()
            for c in novapolja:
                for i in range(a):
                    polja[polozaj[0]+br][polozaj[1]+i-1]=novapolja[br+1][i]
                    poljaslike[polozaj[0]+br][polozaj[1]+i-1]=novapoljaslike[br+1][i]
                    if novapolja[br+1][i]==2:
                        padajuce.append((polozaj[0]+br,polozaj[1]+i-1))
                        slika=novapoljaslike[br+1][i]
                        slika.place(x=200*(3/4)+(polozaj[1]+i-1)*sirinabloka,y=(polozaj[0]+br)*sirinabloka)
                    if novapolja[br+1][i]==1:
                        slika=novapoljaslike[br+1][i]
                        slika.place(x=200*(3/4)+(polozaj[1]+i-1)*sirinabloka,y=(polozaj[0]+br)*sirinabloka)
                br+=1
def micanjelijevo(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj):
    padajuce.sort(key=lambda t:t[1])
    for i in range(4):
        xx=padajuce[0][0]
        yy=padajuce[0][1]
        slika=poljaslike[xx][yy]
        slika.place(x=200*(3/4)+(yy-1)*sirinabloka,y=xx*sirinabloka)
        padajuce.append((xx,yy-1))
        padajuce.pop(0)
        poljaslike[xx][yy-1]=slika
        polja[xx][yy-1]=2
        poljaslike[xx][yy]=None
        polja[xx][yy]=0
    polozaj[1]-=1
def micanjedesno(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj):
    padajuce.sort(key=lambda t:t[1],reverse=True)
    for i in range(4):
        xx=padajuce[0][0]
        yy=padajuce[0][1]
        slika=poljaslike[xx][yy]
        slika.place(x=200*(3/4)+(yy+1)*sirinabloka,y=xx*sirinabloka)
        padajuce.append((xx,yy+1))
        padajuce.pop(0)
        poljaslike[xx][yy+1]=slika
        polja[xx][yy+1]=2
        poljaslike[xx][yy]=None
        polja[xx][yy]=0
    polozaj[1]+=1
def spusti():
    padanje(poljaslike,polja,padajuce,sirinabloka,polozaj)
def okreni():
    okretanje(prozor,polja,sirinabloka,polozaj,poljaslike)
def lijevo():
    if provjeralijevo(prozor,polja,sirinabloka,poljaslike,padajuce):
        micanjelijevo(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
def desno():
    if provjeradesno(prozor,polja,sirinabloka,poljaslike,padajuce):
        micanjedesno(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
def padanjedodna(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj):
    global score
    global level
    global displayscore
    global vrijeme
    global paused
    global spustenododna
    global highscore
    global highs
    starttime=round(time(),1)
    starttime2=round(time(),1)
    starttime3=round(time(),1)
    while True:
        newtime=round(time(),1)
        razlika=newtime-starttime
        razlika=round(razlika,1)
        razlika2=newtime-starttime2
        razlika2=round(razlika2,1)
        razlika3=newtime-starttime3
        razlika3=round(razlika3,1)
        if (not provjera(prozor,polja,sirinabloka,poljaslike,padajuce)) and razlika>=vrijeme and not paused:
            starttime=round(time(),1)
            spusti()
        else:
            a=polozaj[0]
            if provjera(prozor,polja,sirinabloka,poljaslike,padajuce) and razlika>=vrijeme*0.75:
                spustenododna=True
                polozaj.clear()
                for c in padajuce:
                    polja[c[0]][c[1]]=1
                padajuce.clear()
                red(prozor,sirinabloka,padajuce,polozaj)
                break
            else:
                if razlika2>=0.2:
                    if is_pressed('Escape'):
                        paused=True
                        otvoripause(prozor)
                        break
                    elif (is_pressed('a') or is_pressed('left arrow')):
                        starttime2=round(time(),1)
                        lijevo()
                    elif (is_pressed('d') or is_pressed('right arrow')):
                        starttime2=round(time(),1)
                        desno()
                    elif (is_pressed('s') or is_pressed('down arrow')):
                        starttime2=round(time(),1)
                        spustidokraja()
                        score+=(level*(20-a))//2
                        if score>highscore:
                            highscore=score
                        displayscore.set('Score:{}'.format(score))
                        highs.set(str(highscore))
                        break
                if razlika3>=0.2:
                    if (is_pressed('w') or is_pressed('up arrow')):
                        starttime3=round(time(),1)
                        okreni()
        prozor.update()
def padanjedodna2(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj):
    while not provjera(prozor,polja,sirinabloka,poljaslike,padajuce):
        spusti()
        prozor.update()
    if provjera(prozor,polja,sirinabloka,poljaslike,padajuce):
        polozaj.clear()
        for c in padajuce:
            polja[c[0]][c[1]]=1
        padajuce.clear()
        red(prozor,sirinabloka,padajuce,polozaj)
def red(prozor,sirinabloka,padajuce,polozaj):
    global polja
    global poljaslike
    global score
    global level
    global scoring
    global displayscore
    global levelbr
    global vrijeme
    global l
    global highscore
    global highs
    l=[]
    br=0
    for i in range(19,-1,-1):
        if 0 not in polja[i]:
            l.append(i)
            br+=1
            levelbr+=1
    if br==4:
        score+=1200*level
    elif br==3:
        score+=300*level
    elif br==2:
        score+=100*level
    elif br==1:
        score+=40*level
    else:
        score+=0
    if br>0 and music:
        grmi2(br)
    if score>highscore:
        highscore=score
    if levelbr>=7:
        level+=1
        levelbr=0
        if level<=10:
            vrijeme=round(vrijeme*(3/4),2)
    displayscore.set('Score:{}'.format(score))
    displaylevel.set('Level: {}'.format(level))
    highs.set(str(highscore))
    if len(l)>0:
        for i in range(len(l)):
            polja.pop(l[i])
            polja=[[0 for j in range(10)]]+polja
            for k in poljaslike[l[i]]:
                k.destroy()
            poljaslike.pop(l[i])
            for p in range(i+1,len(l)):
                l[p]+=1
            poljaslike=[[None for i in range(10)]]+poljaslike
        updatered() 
def updatered():
    global poljaslike
    for j in range(19,-1,-1):
                for k in range(10):
                    slika=poljaslike[j][k]
                    if slika!=None:
                        slika.place(x=200*(3/4)+k*sirinabloka,y=j*sirinabloka)
def spustidodna():
    padanjedodna(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
def novi():
    dodajnovo(prozor,polja,sirinabloka,poljaslike,padajuce,polozaj,nextslike)
def spustidokraja():
    global spustenododna
    padanjedodna2(prozor,polja,poljaslike,sirinabloka,padajuce,polozaj)
    spustenododna=True
def game():
    global polja
    global gameover
    global spustenododna
    if noviprovjera(polja) and spustenododna:
        novi()
        spustenododna=False
        
    spustidodna()
    if (not noviprovjera(polja)) and spustenododna:
        f=open(file='config/config.txt',mode='r+')
        f.seek(1)
        f.write('\n'+ str(highscore))
        f.close()
        gameover=True
        otvorigameover(prozor)
def muzika():
    PlaySound("audio/Tetris 99 - Main Theme.wav",SND_ASYNC | SND_LOOP)
def grmi():
    global muzika_thread
    muzika_thread=Thread(target=muzika)
    muzika_thread.start()
def grmi2(broj):
    global muzika_threadred
    muzika_threadred=Thread(target=muzikared,args=(broj,))
    muzika_threadred.start()
def muzikared(broj):
    if broj==1:
        zvuk1.play()
    elif broj==2:
        zvuk2.play()
    elif broj==3:
        zvuk3.play()
    elif broj==4:
        zvuk4.play()
def startgame(prozor,canvas):
    global gameover
    global paused
    global spustenododna
    global prvopaljenje
    global nextup
    global scoring
    global le
    unistipocetnu(prozor)
    gameover=False
    paused=False
    startgumb.place_forget();quitgumb.place_forget();optionsgumb.place_forget();resumegumb.place_forget();retrygumb.place_forget();optionsgumb2.place_forget();restartgumb.place_forget()
    gasigameover(prozor)
    scoring.place(x=610*(3/4),y=40*(3/4))
    scoring.config(font=("Arial 15 bold"),bg='white',fg='black')
    le.config(font=("Arial 15 bold"),bg='white',fg='black')
    le.place(x=610*(3/4),y=240*(3/4))
    hir.config(font=("Arial 15 bold"),bg='white',fg='black')
    hir.place(x=610*(3/4),y=120*(3/4))
    his.config(font=("Arial 15 bold"),bg='white',fg='black')
    his.place(x=610*(3/4),y=160*(3/4))
    if prvopaljenje:
        nacrtajpolje(t,sirinabloka)
        prvopaljenje=False
        nextup.config(image=nextslike[0])
    while not gameover:
        if paused:
            break
        try:
            game()
        except:
            PlaySound(None,SND_PURGE)
            break
def restartgame(prozor,canvas):
    global polozaj;global score;global level;global levelbr;global vrijeme;global oblici; global gameover; global paused; global spustenododna; global nextup; global displayscore; global displaylevel; global polja; global poljaslike; global padajuce;global scoring;global le;global kraj
    for c in poljaslike:
        for k in c:
            if k!=None:
                k.destroy()
    polozaj=[] 
    score=0
    level=1
    levelbr=0
    vrijeme=1
    oblici=[randint(0,6)]
    gameover=False
    paused=False
    spustenododna=True
    nextup=Label(prozor)
    nextup.place(x=10,y=0)
    displayscore.set(value='Score:0')
    displaylevel.set(value='Level: 1')
    polja=[[0 for i in range(10)] for j in range(20)]
    poljaslike=[[None for i in range(10)] for j in range(20)]
    padajuce=[]
    startgame(prozor,canvas)
def otvoripocetnu(prozor):
    pocetna.place(x=0,y=0)
    startgumb.place(x=280*(3/4),y=520*(3/4))
    optionsgumb.place(x=280*(3/4),y=600*(3/4))
    quitgumb.place(x=280*(3/4),y=680*(3/4))
def otvorioptions(prozor):
    global music
    options.place(x=0,y=0)
    if music:
        volumeonbutton.place(x=400*(3/4),y=130*(3/4))
        volumeoffbutton.place_forget()
    else:
        volumeoffbutton.place(x=400*(3/4),y=130*(3/4))
        volumeonbutton.place_forget()
    homebutton.place(x=20*(3/4),y=10*(3/4))
def unistioptions(prozor):
    options.place_forget()
    volumeonbutton.place_forget()
    volumeoffbutton.place_forget()
    homebutton.place_forget()
def otvorioptions2(prozor):
    global music
    unistipause(prozor)
    options.place(x=0,y=0)
    if music:
        volumeonbutton.place(x=400*(3/4),y=130*(3/4))
        volumeoffbutton.place_forget()
    else:
        volumeoffbutton.place(x=400*(3/4),y=130*(3/4))
        volumeonbutton.place_forget()
    backbutton.place(x=20*(3/4),y=10*(3/4))
    options.lift();volumeonbutton.lift();volumeoffbutton.lift();backbutton.lift()
def unistioptions2(prozor):
    options.place_forget()
    volumeonbutton.place_forget()
    volumeoffbutton.place_forget()
    backbutton.place_forget()
def unistipocetnu(prozor):
    pocetna.place_forget()
    startgumb.place_forget()
    optionsgumb.place_forget()
    quitgumb.place_forget()
def otvoripause(prozor):
    unistioptions2(prozor)
    pocetna.place(x=0,y=0)
    pocetna.lift()
    resumegumb.place(x=280*(3/4),y=510*(3/4))
    restartgumb.place(x=280*(3/4),y=580*(3/4))
    optionsgumb2.place(x=280*(3/4),y=650*(3/4))
    quitgumb.place(x=280*(3/4),y=720*(3/4))
    resumegumb.lift();restartgumb.lift();optionsgumb2.lift();quitgumb.lift()
def unistipause(prozor):
    pocetna.place_forget()
    resumegumb.place_forget()
    restartgumb.place_forget()
    optionsgumb2.place_forget()
    quitgumb.place_forget()
def resumefun(prozor):
    unistipause(prozor)
    startgame(prozor,canvas)
def ugasiigru(prozor):
    prozor.destroy()
    PlaySound(None,SND_PURGE)
def homebuttoncommand(prozor):
    unistioptions(prozor)
    otvoripocetnu(prozor)
def ugasimuziku(prozor):
    global music
    PlaySound(None,SND_PURGE)
    volumeonbutton.place_forget()
    volumeoffbutton.place(x=400*(3/4),y=130*(3/4))
    music=False
    f=open(file='config/config.txt',mode='r+')
    f.seek(0)
    f.write(str(int(music))+'\n')
    f.close()
def jakogrmi(prozor):
    global music
    grmi()
    volumeoffbutton.place_forget()
    volumeonbutton.place(x=400*(3/4),y=130*(3/4))
    music=True
    f=open(file='config/config.txt',mode='r+')
    f.seek(0)
    f.write(str(int(music))+'\n')
    f.close()
def otvorigameover(prozor):
    kraj.place(x=0,y=0)
    retrygumb.place(x=280*(3/4),y=520*(3/4))
    leadergumb.place(x=280*(3/4),y=600*(3/4))
    quitgumb.place(x=280*(3/4),y=680*(3/4))
    scoring.place(x=340*(3/4),y=360*(3/4))
    scoring.config(bg='#00a8f3',fg='white')
    hir.place(x=285*(3/4), y=420*(3/4))
    his.place(x=430*(3/4), y=420*(3/4))
    hir.config(bg='#00a8f3',fg='white')
    his.config(bg='#00a8f3',fg='white')
    kraj.lift();retrygumb.lift();leadergumb.lift();quitgumb.lift();scoring.lift();hir.lift();his.lift()
def character_limit():
    rijec=imevar.get()
    if len(rijec) > 18:
        imevar.set(rijec[:-1])
def gasigameover(prozor):
    kraj.place_forget()
    retrygumb.place_forget()
    quitgumb.place_forget()
    leadergumb.place_forget()
def otvorigameover2(prozor):
    gasileader(prozor)
    otvorigameover(prozor)
def otvorileader(prozor):
    global lead
    leaderlabel.place(x=0,y=0)
    leaderlabel.lift()
    gasigameover(prozor)
    prozor.update()
    ispisileaders(prozor)
    back2button.place(x=20*(3/4),y=10*(3/4))
    his.place(x=310,y=86)
    e.place(x=310,y=155)
    imevar.set('')
    submitbutton.place(x=325,y=188)
    his.config(font=("Arial 20 bold"))
    back2button.lift();his.lift();e.lift();submitbutton.lift()
    for c in lead:
        c.lift()
def gasileader(prozor):
    for c in lead:
        c.place_forget()
    leaderlabel.place_forget()
    back2button.place_forget()
    his.config(font=("Arial 15 bold"))
    his.place_forget()
    e.place_forget()
    submitbutton.place_forget()
def submitleader():
    global key
    global ime
    ime=imevar.get()
    if ime!='':
        if key=='':
            cuvaj=db.child("scores").push({ime:highscore})
            key=cuvaj['name']
            f=open('config/leaderconfig.txt',mode='r+')
            f.write(key)
            f.close()
        else:
            db.child("scores").child(key).remove()
            db.child("scores").child(key).set({ime:highscore})
        readleader()
        ispisileaders(prozor)
def readleader():
    global leaders
    leaders=[]
    users=db.child('scores').get()
    for c in users.each():
        leaders.append((list(c.val().keys())+list(c.val().values())))
    leaders.sort(key=lambda t:t[1],reverse=True)
    leaders=leaders[:10]
def ispisileaders(prozor):
    global leaders
    global lead
    for c in lead:
        c.destroy()
    loadaj()
    for i in range(0,20,2):
        lead[i].place(x=100,y=250+(i//2)*30)
        lead[i+1].place(x=450,y=250+(i//2)*30)
def loadaj():
    global lead
    global leaders
    lead=[]
    for i in range(10):
        lead.append(Label(prozor,text='{}. {}'.format(i+1,leaders[i][0]),font=("Arial 15 bold"),bg='#00a8f3',fg='white'))
        lead.append(Label(prozor,text='{}'.format(str(leaders[i][1])),font=("Arial 15 bold"),bg='#00a8f3',fg='white'))
polozaj=[]
pg.mixer.init(44100,-16,1,512)
pg.init()
pg.mixer.set_num_channels(10)
zvuk1=pg.mixer.Sound('audio/1red.wav')
zvuk2=pg.mixer.Sound('audio/2reda.wav')
zvuk3=pg.mixer.Sound('audio/3reda.wav')
zvuk4=pg.mixer.Sound('audio/4reda.wav')
sirinabloka=30
prozor=Tk()
prozor.resizable(0,0)
prozor.title('Tetris')
prozor.iconbitmap('@images/icon.xbm')
score=0
level=1
levelbr=0
vrijeme=1
pyrconfig = {
  "apiKey": "AIzaSyDOjjiHf4tbqcXyPS8ncXK1qd_aY8cmA3o",
  "authDomain": "tetris-79e5d.firebaseapp.com",
  "databaseURL": "https://tetris-79e5d.firebaseio.com",
  "projectId": "tetris-79e5d",
  "storageBucket": "tetris-79e5d.appspot.com",
  "serviceAccount": "config/key.json"
  
}
firebase = pyrebase.initialize_app(pyrconfig)
db=firebase.database()
ime=''
f=open(file='config/leaderconfig.txt',mode='r+')
ldr=f.readlines()
if len(ldr)==0:
    key=''
else:
    key=ldr[0]
f.close()
leaders=[]
readleader()
canvas=Canvas(master=prozor,width=300+10*sirinabloka,height=20*sirinabloka)
canvas.config(bg='#00a8f3')
screen=TurtleScreen(canvas)
t=RawTurtle(screen)
oblici=[randint(0,6)]
pocetak(prozor,canvas,screen,t,sirinabloka)
f=open(file='config/config.txt',mode='r+')
conf=f.readlines()
music=bool(int(conf[0].strip('\n')))
highscore=int(conf[1].strip('\n'))
f.close()
if music:
    grmi()
gameover=False
paused=False
spustenododna=True
prvopaljenje=True
nextup=Label(prozor)
nextup.place(x=10*(3/4),y=0)
displayscore=StringVar(value='Score:0')
displaylevel=StringVar(value='Level: 1')
highs=StringVar(value=str(highscore))
scoring=Label(prozor,textvariable=displayscore,font=("Arial 15 bold"))
scoring.place(x=610*(3/4),y=40*(3/4))
le=Label(prozor,textvariable=displaylevel,font=("Arial 15 bold"))
le.place(x=610*(3/4),y=240*(3/4))
hir=Label(prozor,text='Highscore:',font=("Arial 15 bold"))
hir.place(x=610*(3/4),y=120*(3/4))
his=Label(prozor, textvariable=highs ,font=("Arial 15 bold"))
his.place(x=610*(3/4),y=160*(3/4))
polja=[[0 for i in range(10)] for j in range(20)]
poljaslike=[[None for i in range(10)] for j in range(20)]
padajuce=[]
imevar=StringVar()
imevar.trace("w", lambda *args: character_limit())
slike=[PhotoImage(file='images/polje_svj_plavo.png'),PhotoImage(file='images/polje_plavo.png'),PhotoImage(file='images/polje_narancasto.png'),PhotoImage(file='images/polje_zuto.png'),PhotoImage(file='images/polje_zeleno.png'),PhotoImage(file='images/polje_crveno.png'),PhotoImage(file='images/polje_ljubicasto.png')]
nextslike=[PhotoImage(file='images/next_svj_plavo.png'),PhotoImage(file='images/next_plavo.png'),PhotoImage(file='images/next_narancasto.png'),PhotoImage(file='images/next_zuto.png'),PhotoImage(file='images/next_zeleno.png'),PhotoImage(file='images/next_crveno.png'),PhotoImage(file='images/next_ljubicasto.png')]
startscreen=PhotoImage(file='images/startscreen.png')
endscreen=PhotoImage(file='images/endscreen.png')
leaderboardsscreen=PhotoImage(file='images/leaderboardsscreen.png')
quitimage=PhotoImage(file='images/quitbutton.png')
retryimage=PhotoImage(file='images/retrybutton.png')
startimage=PhotoImage(file='images/startbutton.png')
optionsscreen=PhotoImage(file='images/optionsscreen.png')
resumeimage=PhotoImage(file='images/resumebutton.png')
leaderboardsimage=PhotoImage(file='images/leaderboardsbutton.png')
optionsimage=PhotoImage(file='images/optionsbutton.png')
restartimage=PhotoImage(file='images/restart.png')
back=PhotoImage(file='images/back.png')
volumeon=PhotoImage(file='images/volumeon.png')
volumeoff=PhotoImage(file='images/volumeoff.png')
home=PhotoImage(file='images/home.png')
submitimage=PhotoImage(file='images/submitbutton.png')
pocetna=Label(prozor,image=startscreen)
kraj=Label(prozor, image=endscreen)
e=Entry(prozor,font=("Arial 15 bold"),textvariable=imevar)
leaderlabel=Label(prozor,image=leaderboardsscreen)
startgumb=Button(prozor,image=startimage,command=lambda: startgame(prozor,canvas))
optionsgumb=Button(prozor,image=optionsimage,command=lambda: otvorioptions(prozor))
optionsgumb2=Button(prozor,image=optionsimage,command=lambda: otvorioptions2(prozor))
quitgumb=Button(prozor,image=quitimage,command=lambda: ugasiigru(prozor))
resumegumb=Button(prozor,image=resumeimage,command=lambda: resumefun(prozor))
retrygumb=Button(prozor,image=retryimage,command=lambda: restartgame(prozor,canvas))
restartgumb=Button(prozor,image=restartimage,command=lambda: restartgame(prozor,canvas))
options=Label(prozor,image=optionsscreen)
volumeonbutton=Button(prozor,image=volumeon,command=lambda: ugasimuziku(prozor))
volumeoffbutton=Button(prozor,image=volumeoff,command=lambda: jakogrmi(prozor))
homebutton=Button(prozor,image=home,command=lambda: homebuttoncommand(prozor))
backbutton=Button(prozor,image=back,command=lambda: otvoripause(prozor))
back2button=Button(prozor,image=back,command=lambda: otvorigameover2(prozor))
leadergumb=Button(prozor,image=leaderboardsimage,command=lambda: otvorileader(prozor))
submitbutton=Button(prozor,image=submitimage,command=lambda: submitleader())
lead=[]
otvoripocetnu(prozor)
prozor.mainloop()
