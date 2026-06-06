# modul przechowuje:
# oryginalne i znormalizowane krotki danych,
# slowniki normalizacyjne do zmiennych tekstowych,
# funkcje wczytywania i wypisywania krotek,
# funkcje normalizacji danych

def test():
    wczytajDane()
    normalizujDane()
    wypiszKrotkiNormal()

krotkiDane=[]
krotkiNormal=[]

#podmienione na poziomy dochodow
states={'Low':2,'Lower-Middle':4,'Middle':6,'Upper-Middle':8,'High':10}
#podmienione wartosci pasujace do nowego zbioru danych
sex={'F':20,'M':40}
#podmienione wartosci na status palenia
names={'Current':10,'Former':20,'Never':30}

def wczytajDane():
   #podmiana pliku na nowy
   import csv
   with open('DiabetesRisk.txt','r') as csvfile:
      csvreader = csv.reader(csvfile)
      next(csvreader)
      for krotka in csvreader:
         krotkiDane.append(krotka)

def wypiszDane():
   #zmiana formatu pod nowy zbior
   for krotka in krotkiDane:
      print(krotka[0]," ",krotka[1]," ",krotka[2],'%-10s'%(krotka[3]),'%6s'%krotka[4],'%6s'%krotka[5])

def wypiszKrotkiNormal():
   # wypisuje zawartosc listy krotkiNormal do interpretera
   print('KROTKI NORMAL')
   for krotka in krotkiNormal:
      #zmiana formatu pod nowy zbior
      print ('%4d %4d %4d %4d %7.1f %7.1f %4d'%(krotka[0],krotka[1],krotka[2],krotka[3],krotka[4],krotka[5],krotka[6]))

def normalizujDane():
   # normalizuje dane surowe z listy *krotki* i wpisuje je do listy *krotkiNormal*
   # -1 oznacza, ze nie wpisano jeszcze numeru klastra, do ktorego nalezy krotka
   for i in range(len(krotkiDane)):
      krotka=[]
      first=krotkiDane[i][0]
      krotka.append(states[first])
      second=krotkiDane[i][1]
      krotka.append(sex[second])
      third=krotkiDane[i][2]
      result=int(third)-18
      krotka.append(result)
      forth=krotkiDane[i][3]
      krotka.append(names[forth])
      fifth=krotkiDane[i][4]
      result=float(fifth)
      krotka.append(result)
      sixth=krotkiDane[i][5]
      result=0.5*float(sixth)
      krotka.append(result)
      krotka.append(-1)
      krotkiNormal.append(krotka)



