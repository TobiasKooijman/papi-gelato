## start Text
import time
restart = 0
bOh = 0
aardbei = 0
choco = 0
munt = 0
bkje = 0
hrrn = 0
Vanil = 0
while restart == 0:
    print("Welkom bij Papi Gelato!")
    time.sleep(1)
    res = 0
    while res == 0:
        bolletjes = input('Hoeveel bolletjes wilt u? ')
        if int(bolletjes) <= 3:
            BakjeOfHoorn = input('Wilt u deze '+ str(bolletjes)+' bolletje(s) in A) een hoorntje of B) een bakje? ')
            if BakjeOfHoorn.lower() == "a":
                bOh= "hoorn"
                hrrn += 1
            elif BakjeOfHoorn.lower() == "b":
                bOh= "bakje"
                bkje += 1
        elif int(bolletjes) > 8:
            print("Sorry, zulke grote bakken hebben we niet")
            time.sleep(1)
            print("probeer het opnieuw")
            time.sleep(1)
        elif int(bolletjes) >= 4:
            bOh = "bakje"
            bkje += 1
        else:
            print("Sorry, dat begrijp ik niet!")
        for i in range(1,int(bolletjes)+1):
            Smaak = input('welke smaak wilt u bij bolletje '+str(i)+'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak.lower() == "a":
                aardbei += 1
                res = 1
            elif Smaak.lower() == "c":
                choco += 1
                res = 1
            elif Smaak.lower() == "m":
                munt += 1
                res = 1
            elif Smaak.lower() == "v":
                Vanil += 1
                res = 1
            else:
                print("Dit is geen geldig antwoord")
                i -= 1

    if aardbei >= 1:
        ab = 'Uw krijgt '+str(aardbei)+ ' bolletjes met aardbij smaak'
        print(ab)
    if choco >= 1:
        ch = 'Uw krijgt '+str(choco)+ ' bolletjes met chocolade smaak'
        print(ch)
    if munt >= 1:
        mu = 'Uw krijgt '+str(munt)+ ' bolletjes met munt smaak'
        print(mu)
    if Vanil >= 1:
        van = 'Uw krijgt '+str(Vanil)+ ' bolletjes met vanille smaak'
        print(van)
    print('Dan krijgt u van mij een '+str(bOh)+' met '+ str(bolletjes) +' bolletjes')
    time.sleep(1)
    again = input('wilt u nog meer bestellen? Y/N ')
    if again.lower() == "n":
        time.sleep(1)
        print("-------------[Papi-Gelato]--------------")
        print("")
        bol_tot = int(bolletjes) * 1.10
        rek_bol = 'Bolletjes      ' + str(bolletjes) + ' X 1.10 = ' + str(bol_tot)
        print(rek_bol)
        bkje_tot = int(bkje)* 0.75
        hrrn_tot = int(hrrn)*1.25
        if bkje >= 1:
            rek_bkj = 'bakje          '+str(bkje)+' X 0.75 = '+ str(bkje_tot)
            print(rek_bkj)
        if hrrn >= 1:
            rek_hrrn = 'Hoorn          '+str(hrrn)+' X 1.25 = '+ str(hrrn_tot)
            print(rek_hrrn)
        print("              ---------- +")
        totaal = int(bkje_tot) + int(hrrn_tot) + int(bol_tot)
        print("Totaal:          "+ str(totaal)+" euro")
        exit()