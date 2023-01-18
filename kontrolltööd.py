from random import *
#Variant 3
#Ülesanne 1
#while True:
#    try:
#        linnumaju = int(input("kui palju linnumaju sa tahad näha? (0-9) "))
#        if linnumaju < 0:
#            print("see on see on väga vähe")
#        if linnumaju > 9:
#            print("see on palju")
#        if linnumaju >=0 and linnumaju <=9:
#            for i in range (0,linnumaju,1):
#                print ("   -----")
#                print ("  |  O  |")
#                print ("  !  -  !")
#                print ("   -----")
#                print ()
#            break
#    except:
#        print("see on viga")

#Ülesanne 2
#print("valige arv, kraad ja programm annab teile kõik protsendimäärad loomulikest arvudest, mis on väiksemad kui valitud arv.")
#while True:
#    try:
#        arv1 = 0
#        print()
#        arv2 = int(input("vali arv "))
#        kraad = int(input("ja vali kraad naturaalide jaoks "))
#        if arv2>0 and kraad>0 :
#            for c in range (0,arv2,1):
#                arv3 = arv1 ** kraad
#                if arv3 < arv2:
#                    print(f"{arv3} (see on {arv1} in {kraad})")
#                    arv1 +=1
#                if arv3 >= arv2:
#                    break
#            break
#        if arv2 < 0 or kraad < 0:
#            print("ainult positiivsed numbrid")
#    except:
#        print("see ei ole arv")

#Ülesanne 3
#while True:
#    try:
#        keskmine = 0
#        õpilased = int(input("kui palju õiplased sisse klassis "))
#        if õpilased == 0 :
#            print ("klassis ei ole õpilased")
#        if õpilased < 0 :
#            print ("see ei ole õige")
#        if õpilased > 0:
#            for i in range(1,õpilased+1,1):
#                hind = randint(1,5)
#                print(f"{i} õpilane hind = {hind}")
#                keskmine += hind
#            keskminevastus = keskmine / õpilased
#            print(f"keskmine = {keskmine} / {õpilased} = {keskminevastus}")
#            break
#    except:
#        print("see ei ole arv")

#Ülesanne 4
#minuraha = 0
#aasta = 1
#print("kui saan 100 dollarit ")
#print("peale mu esimest sünnipäeva mul on 1 dollar")
#while minuraha <=100:
#    minuraha  += aasta
#    print (f"pärast {aasta} aasta minuraha = {minuraha} dollarit ")
#    aasta +=1
#    print ()
