# Simulation Würfeln #

from random import randrange


weiter="j"    # die Abfrage wird auf "j" gesetzt, damit die Schleife beginnen kann
zähler1 = 0    # die Anzahl der Teiler wird initialisiert

while weiter =="j":


    n_max = int(input("Anzahl der Würfe: "))
    n = 1               #
    würfeln = 1

    print
    print('         n   h_n(z_1)   h_n(z_2)   h_n(z_3)   h_n(z_4)   h_n(z_5)   h_n(z_6)  ')
    print('______________________________________________________________________________')

    while n<n_max:      # solange ausführen bis Anzahl der Würfe erreicht ist

        z_1 = 0           # Zähler initialisieren
        z_2 = 0
        z_3 = 0
        z_4 = 0
        z_5 = 0
        z_6 = 0
        
        n = n*10        # jede Stufe um das Zehnfache erhöhen 
        
        for i in range(1,n+1):      # bis inkl. n ausführen
            würfeln = randrange(1,7)   # Würfeln
            if würfeln ==1:      # wenn eine 1 gewürfelt wird
                    z_1=z_1+1                   # Zählen
            elif würfeln ==2:
                    z_2=z_2+1
            elif würfeln ==3:
                    z_3=z_3+1
            elif würfeln ==4:
                    z_4=z_4+1
            elif würfeln ==5:
                    z_5=z_5+1
            else:
                    z_6=z_6+1

        print("%10d,%10.6f,%10.6f,%10.6f,%10.6f,%10.6f,%10.6f"%(n,z_1/n,z_2/n,z_3/n,z_4/n,z_5/n,z_6/n))
        #print(n,'    ',z_1/n,'   ',z_2/n,'    ',z_3/n,'    ',z_4/n,'   ',z_5/n,'    ',z_6/n)    
            # end if


        print()
        print()
weiter=str(input('Noch eine Zahl eingeben? j/n:'))
print()
print()
        

    
