## start Text
import time
restart = 0
while restart == 0:
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
    time.sleep(1)
    bOh = 0
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

    print('Dan krijgt u van mij een '+str(bOh)+' met '+ str(bolletjes) +' bolletjes')
    time.sleep(1)
    again = input('wilt u nog meer bestellen? Y/N ')
    if again.lower() == "n":
        print("Bedankt voor jouw bestelling!")
        time.sleep(1)
        print("het programma sluit nu af")
        time.sleep(2)
        exit()