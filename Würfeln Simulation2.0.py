# Simulation Würfeln 2.0 #


#random importieren
from random import randrange
#tkinter für GUI importieren
import tkinter as tk

#eine Funktion um den Main-Screen zu zerstören
def destroy_main():
    main.destroy()

#eine Funktion um den Output-Screen zu zerstören
def destroy_o_screen():
    o_screen.destroy()

#die funktion die würfelt
def würfeln():
        #die nötigen Variablen globalisieren
        global z_1, z_2, z_3, z_4, z_5, z_6


        n = 1           
        würfeln = 1

        while n < int(n_max):      # solange ausführen bis Anzahl der Würfe erreicht ist

                z_1 = 0           # Zähler initialisieren
                z_2 = 0
                z_3 = 0
                z_4 = 0
                z_5 = 0
                z_6 = 0
                
                n = n*10        # jede Stufe um das Zehnfache erhöhen 
                
                for i in range(1, n + 1):      # bis inkl. n ausführen
                        würfeln = randrange(1, 7)   # Würfeln
                        if würfeln == 1:      # wenn eine 1 gewürfelt wird
                                z_1 = z_1 + 1                   # Zählen
                        elif würfeln == 2:
                                z_2 = z_2 + 1
                        elif würfeln == 3:
                                z_3 = z_3 +1 
                        elif würfeln == 4:
                                z_4 = z_4 + 1
                        elif würfeln == 5:
                                z_5 = z_5 + 1
                        else:
                                z_6 = z_6 + 1

        tk.Label(o_screen, text="Würfe:  1:               2:               3:                   4:                 5:           6:").pack()
        tk.Label(o_screen, text="--------------------------------------------------------------------------------------").pack()
        #das würfelergebnis auf dem output-screen anzeigen
        tk.Label(o_screen, text=str("%10d,%10.6f,%10.6f,%10.6f,%10.6f,%10.6f,%10.6f"%(n, z_1/n, z_2/n, z_3/n, z_4/n, z_5/n, z_6/n))).pack()


def output_screen():
        global o_screen, n_max
        
        #die anzahl an würfen die gemacht werden sollen mit get() aus einer eingabe bekommen
        n_max = eingabe.get()
        #das eingabe feld leeren (nur für den look)
        eingabe.delete(0, tk.END)


        #eine GUI- output-screen mit tkinter erstellen
        o_screen = tk.Tk()
        #die grösse anpassen in pixeln
        o_screen.geometry("1200x300")
        #den titel verändern
        o_screen.title("Würfeln")
        #ein button um das programm vom anfang wieder zu beginenn
        destroy = tk.Button(o_screen, text="Neue Eingabe tätigen", command= lambda:[destroy_main(), destroy_o_screen(), main_screen() ])
        destroy.pack()
        
        #ein button der die würfeln funktion auslöst
        würfeln_bttn = tk.Button(o_screen, text="Würfeln", command=würfeln, bg="grey")
        würfeln_bttn.pack()
        
        #das programm in die mainloop stecken sodass es angezeigt wird
        o_screen.mainloop()


#die funktion die unser main-screen ist
def main_screen():
        global main
        global eingabe
        
        #einen main-screen erstellen
        main = tk.Tk()
        #die grösse anpassen in pixeln
        main.geometry("300x300")
        #den titel verändern
        main.title("Würfel --Wahrscheinligkeit")

        #eine Integer Variable initialisieren in der  die eingabe notiert wird
        eingabe = tk.IntVar()
        #ein Label erstellen dass einen Text anzeigt
        label = tk.Label(main, text="Wie oft soll gewürfelt werden?")
        label.pack()
        #ein Eingabefeld, dass die eingegebenen informationen an die Variable "eingabe" gibt
        eingabe = tk.Entry(main, textvariable=eingabe)
        eingabe.pack()
        #ein button, der den output screen öffnet
        buttn = tk.Button(main, text="Bestätigen!", command= lambda: [output_screen()])
        buttn.pack()
        #das programm in die mainloop stecken sodass es angezeigt wird
        main.mainloop()
        

#der main-screen wird beim ersten mal auführen augerufen
main_screen()