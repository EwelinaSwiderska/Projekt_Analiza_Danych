import intro
import calcul

liczbaPowtórzeń=10

def main():
    print('\nLICZBA KLASTRÓW ',calcul.liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    print('Wczytano:',len(intro.krotkiNormal),'rekordow')
    calcul.losujCentroidy()
    calcul.wypiszCentroidy()
    calcul.przypiszKrotkomNumeryKlastrów()
    calcul.utwórzKlastry()
    calcul.podsumujKlastry()

    repeat=0
    while repeat < liczbaPowtórzeń:
        calcul.newCentroidy()
        calcul.wypiszCentroidy()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul.utwórzKlastry()
        calcul.podsumujKlastry()
        repeat+=1

    if len(intro.krotkiNormal) > 0:
        print('\nZAKRESY PO NORMALIZACJI:')
        for j,name in enumerate(['Income','Gender','Age','Smoking','BMI','Risk']):
            vals = [k[j] for k in intro.krotkiNormal]
            print('  %8s: %6.1f - %6.1f  (rozpietosc: %.1f)' % (name,min(vals),max(vals),max(vals)-min(vals)))
    else:
        print('\nBLAD: brak danych - sprawdz plik DiabetesRisk.txt')

main()