## start Text
import time
restart = 0
toppie = 0
bOh = 0
aardbei = 0
choco = 0
munt = 0
bkje = 0
hrrn = 0
Vanil = 0
sprink = 0
slag = 0
geen = 0
caramel = 0
zijn = 0
begn = 0
liters = 0
while begn == 0:
    zijn = input('Bent u A) particulier of B) zakelijk? ')
    if zijn.lower() == "a":
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
                    Smaak = input('welke smaak wilt u bij bolletje '+str(i)+'? A) Aardbei, C) Chocolade of V) Vanille? ')
                    if Smaak.lower() == "a":
                        aardbei += 1
                        res = 1
                    elif Smaak.lower() == "c":
                        choco += 1
                        res = 1
                    elif Smaak.lower() == "v":
                        Vanil += 1
                        res = 1
                    else:
                        print("Sorry dat is geen optie die we aanbieden...")
                        i = i - 1
                topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
                if topping.lower() == "a":
                    geen += 1
                elif topping.lower() == "b":
                    slag += 1
                elif topping.lower() == "c":
                    sprink += 1
                elif topping.lower() == "d":
                    caramel += 1
            if aardbei >= 1:
                ab = 'Uw krijgt '+str(aardbei)+ ' bolletjes met aardbij smaak'
                print(ab)
            if choco >= 1:
                ch = 'Uw krijgt '+str(choco)+ ' bolletjes met chocolade smaak'
                print(ch)
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
                bol_tot = int(bolletjes) * 0.95
                rek_bol = 'Bolletjes      ' + str(bolletjes) + ' X 0.95 = ' + str(bol_tot)
                print(rek_bol)
                bkje_tot = int(bkje)* 0.75
                hrrn_tot = int(hrrn)*1.25
                if bkje >= 1:
                    rek_bkj = 'Bakje          '+str(bkje)+' X 0.75 = '+ str(bkje_tot)
                    print(rek_bkj)
                if hrrn >= 1:
                    rek_hrrn = 'Hoorn          '+str(hrrn)+' X 1.25 = '+ str(hrrn_tot)
                    print(rek_hrrn)
                if geen > 0:
                    topping_bon = 'Topping                 = '+ str(0)
                    toppie = 0
                if slag > 0:
                    topping_bon = 'Topping                 = '+ str(0.50)
                    toppie = 0.50
                if sprink > 0:
                    topping_bon = 'Topping                 = '+ str(0.30)
                    toppie = 0.30
                if caramel > 0:
                    if bkje >= 1:
                        topping_bon = 'Topping                  = '+ str(0.90)
                        toppie = 0.90
                    if hrrn >= 1:
                        topping_bon = 'Topping                  = '+ str(0.60)
                        toppie = 0.60
                print(topping_bon)
                print("                   ---------- +")
                totaal = float(bkje_tot) + float(hrrn_tot) + float(bol_tot) + float(toppie)
                print("Totaal:                   "+ str(totaal)+" euro")
                exit()
    if zijn.lower() == "b":
        liters = input('Hoeveel liter wilt u? ')
        for i in range(1,int(liters)+1):
            Smaak = input('welke smaak wilt u bij het '+str(i)+'e liter? A) Aardbei, C) Chocolade of V) Vanille? ')
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
                print("Sorry dat is geen optie die we aanbieden...")
                i = i - 1
        print("")
        print("-------------[Papi-Gelato]--------------")
        print("")
        liters_tot = int(liters) * 9.80
        Liter_bon = 'Liter       ' + str(liters) + ' X 9.80 = '+ str(liters_tot)
        print(Liter_bon)
        print("                    -------- +" )
        print("Totaal               = "+ str(liters_tot))
        bon_btw = int(liters_tot) / 100 * 6
        print("BTW (6%)             = "+str(bon_btw))
        exit()
    else:
        print("Sorry dat is geen optie die we aanbieden...")