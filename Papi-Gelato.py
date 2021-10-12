## start Text
import time
restart = 0
while restart == 0:
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
    time.sleep(1)
    bOh = 0
    aardbei = 0
    choco = 0
    munt = 0
    Vanil = 0
    while bOh == 0:
        bolletjes = input('Hoeveel bolletjes wilt u? ')
        if int(bolletjes) <= 3:
            BakjeOfHoorn = input('Wilt u deze '+ str(bolletjes)+' bolletje(s) in A) een hoorntje of B) een bakje? ')
            if BakjeOfHoorn.lower() == "a":
                bOh= "hoorn"
            elif BakjeOfHoorn.lower() == "b":
                bOh= "bakje"
        elif int(bolletjes) > 8:
            print("Sorry, zulke grote bakken hebben we niet")
            time.sleep(1)
            print("probeer het opnieuw")
            time.sleep(1)
        elif int(bolletjes) >= 4:
            bOh = "bakje"
        else:
            print("Sorry, dat begrijp ik niet!")
        for i in range(1,int(bolletjes)+1):
            Smaak = input('welke smaak wilt u bij bolletje '+str(i)+'? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
            if Smaak.lower() == "a":
                aardbei += 1
            elif Smaak.lower() == "c":
                choco += 1
            elif Smaak.lower() == "m":
                munt += 1
            elif Smaak.lower() == "v":
                Vanil += 1
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
        print("Bedankt voor jouw bestelling!")
        time.sleep(1)
        print("het programma sluit nu af")
        time.sleep(2)
        exit()