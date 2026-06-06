#moduł przechowuje początkową liczbę klastrów,
#oraz poczatkową pustą listę klastrów i centroidów.
#UWAGA: wartości poczatkowe zmiennych modułowych
#       są dostępne po każdorazowym załadowaniu modułu

import math
import random
import intro

liczbaKlastrów=8
# poczatkowa liczba klastrów
klastry=[]
#każdy z klastrów jest listą krotekNormal położonych najbliżej centroidy
Centroidy=[]

def test():
    print('\nLICZBA KLASTRÓW ',liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    losujCentroidy()
    wypiszCentroidy()
    przypiszKrotkomNumeryKlastrów()
    #intro.wypiszKrotkiNormal()
    utwórzKlastry()
    wypiszKlastry()
    newCentroidy()
    wypiszCentroidy()

def losujCentroide():
# losuje początkowe położenie centroidy dla pojedynczego klastra
# zakresy dopasowane do znormalizowanych danych diabetes
    centroida=[]
    state=random.choice([2,4,6,8,10])       # IncomeLevel: 2-10
    centroida.append(state)
    sex=random.choice([20,40])               # Gender: 20/40
    centroida.append(sex)
    year=random.randint(0,72)                # Age: 0-72
    centroida.append(year)
    name=random.choice([10,20,30])           # SmokingStatus: 10/20/30
    centroida.append(name)
    evens=random.uniform(15.0,39.2)          # BMI: 15.0-39.2
    centroida.append(evens)
    risk=random.uniform(1.4,33.6)            # RiskScore: 1.4-33.6
    centroida.append(risk)
    return centroida

def losujCentroidy():
# losuje określoną przez liczbę klastrów poczatkowe położenia centroid
    i=1
    while i<=liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i=i+1

def wypiszCentroide(centroida):
       print ('%4d %4d %4d %4d %7.1f %7.1f'%(centroida[0],centroida[1],centroida[2],centroida[3],centroida[4],centroida[5]))

def wypiszCentroidy():
# wypisuje do interpretera aktualne wartości wszystkich centroid
   print('CENTROIDY')
   for centroida in Centroidy:
      wypiszCentroide(centroida)

def EuklidesPower(krotkaNormal,centroida):
# zwraca kwadrat odległości euklidesowej danej krotkiNormal od danej centroidy
# usunięto if i != 1 — po naprawieniu skali Gender wszystkie cechy uczestniczą
   suma=0
   for i in range(0,len(krotkaNormal)-1):
       dif=centroida[i]-krotkaNormal[i]
       difpow=math.pow(dif,2)
       suma+=difpow
   distance=math.sqrt(suma)
   return math.pow(distance,2)

def ManhattanDist(krotkaNormal,centroida):
# zwraca odległość Manhattan danej krotkiNormal od danej centroidy
# do porównania z odległością euklidesową
   suma=0
   for i in range(0,len(krotkaNormal)-1):
       suma+=abs(centroida[i]-krotkaNormal[i])
   return suma

def przypiszKrotkomNumeryKlastrów():
# przypisuje każdej znormalizowanej krotce najbliższą centroidę
    for krotkaNormal in intro.krotkiNormal:
        minimum=1e100
        for i in range(len(Centroidy)):
            next=EuklidesPower(krotkaNormal,Centroidy[i])
            if next<minimum:
                minimum=next
                minimumIndex=i
        krotkaNormal[6]=minimumIndex

def utwórzKlastry():
    global klastry
    klastry=[]
    for i in range(0,len(Centroidy)):
        klaster=[]
        for krotka in intro.krotkiNormal:
            if krotka[6]==i:
                klaster.append(krotka)
        klastry.append(klaster)

def wypiszKlaster(nrKlastra):
    print('NUMER KLASTRA ',nrKlastra)
    for krotka in klastry[nrKlastra]:
        print ('%4d %4d %4d %4d %7.1f %7.1f %4d'%(krotka[0],krotka[1],krotka[2],krotka[3],krotka[4],krotka[5],krotka[6]))

def wypiszKlastry():
# wypisuje do interpretera aktualne wartości wszystkich klastrów
    for numer in range(0,len(Centroidy)):
       wypiszKlaster(numer)

def newCentroide(klaster):
# oblicza nowe położenie centroidy we wskazanym klastrze
# i zwraca wynik w postaci nowej centroidy dla wskazanego klastra
    if len(klaster)==0:
        return losujCentroide()
    sumState=sumYear=sumEven=sumRisk=0
    numFem=numMal=0
    smokeCounts={10:0,20:0,30:0}
    centroida=[]
    for krotka in klaster:
        sumState+=krotka[0]
        if krotka[1]==40:
            numMal+=1
        else:
            numFem+=1
        sumYear+=krotka[2]
        smokeCounts[krotka[3]]=smokeCounts.get(krotka[3],0)+1
        sumEven+=krotka[4]
        sumRisk+=krotka[5]
    centroida.append(sumState//len(klaster))
    if numFem>=numMal:
        centroida.append(20)
    else:
        centroida.append(40)
    centroida.append(sumYear//len(klaster))
    centroida.append(max(smokeCounts,key=smokeCounts.get))
    centroida.append(sumEven/len(klaster))
    centroida.append(sumRisk/len(klaster))
    return centroida

def newCentroidy():
    global Centroidy
    Centroidy=[]
    print('\nprzesunieto centroidy -----------')
    for nr in range(liczbaKlastrów):
        Centroidy.append(newCentroide(klastry[nr]))

