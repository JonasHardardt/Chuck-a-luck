#--------------------------------------------------------------------------#
#Name des Schülers: Jonas Hardardt
#Stufe: MSS 11
#Kurs: INF
#Lehrer: Hr. Wagner
#Projekt: Spiel Chuck a Luck grafisch implementieren
#Datum: 16.12.2022
#--------------------------------------------------------------------------#

#Falls das Programm sich aufhängt, Fenster bitte schließen, Stop Button in Thonny drücken und noch einmal starten

#Sie können um zu tippen die Zahlen ankicken. Dann vergrößert sich die Zahl darunter um 1.
#Sie können auch die Zahl unter den großen Zahlen direkt ändern, in dem sie diese löschen und eine neue eingeben.
#Zum Würfeln auf würfel-Button klicken.

from tkinter import *
import tkinter as tk
from random import *
import time
import tkinter.font as font
fenster = Tk()

#Größe des Bildschirms bestimmen
def groesse():
    fw = int(fenster.winfo_screenwidth())
    fh = int(fenster.winfo_screenheight())
    return[fw, fh]

#Alle Werte für die Zahlen beim Tippen bestimmen(x-, y-Koordinate, Breite, Höhe) in Relation zur Fenstergröße
def werte_tipp(fw, fh):
    xWerte = []
    for i in range(1, 7):
        xWerte += [int((i-1) * 0.13 * fw + i * 0.03 * fw)]
        
    yWert = int(0.5 * fh)
    height = int(0.25 * fh)
    width = int(0.13 * fw)
    seize = int(width * 0.4)
    yWertEingabe = int(0.79 * fh)
    heightEingabe = int(0.075 * fh)
    seizeEingabe = int(0.15 * width)
    return [xWerte, yWert, height, width, seize, yWertEingabe, heightEingabe, seizeEingabe]

#Alle Werte für die Würfel und den wuerfeln Button bestimmen(x-, y-Koordinate, Breite, Höhe) in Relation zur Fenstergröße
def werteWuerfel(fw, fh):
    xWerte = []
    for i in range(1, 4):
        xWerte += [int((i-1) * 0.126 * fw + i * 0.03 * fw)]
    width = int(0.126 * fw)
    yWert = int(0.25 * (0.5* fh - width))
    buttonHeight = yWert
    buttonyWertWuerfeln = int(2 * yWert + width)
    buttonxWertWuerfeln = int(0.2 * fw)
    buttonWidthWuerfeln = int(0.1 * fw)
    return [xWerte, width, yWert, buttonHeight, buttonyWertWuerfeln, buttonxWertWuerfeln, buttonWidthWuerfeln]

#Alle Werte für die Kontostandanzeige und die ueberschrift bestimmen(x-, y-Koordinate, Breite, Höhe) in Relation zur Fenstergröße
def werteKonto(fw, fh):
    xWertBeide = int(0.55 * fw)
    yWertUeberschrift = int(0.05 * fh)
    heigthUeberschrift = int(0.1 * fh)
    widthUeberschrift = int(0.4 * fw)
    yWertKontostand = int(0.2 * fh)
    heightKontostand = int(0.25 * fh)
    fontsize = int(0.075 * fw)
    widthKontostand = int(0.4 * fw)
    return [xWertBeide, yWertUeberschrift, heigthUeberschrift, widthUeberschrift, yWertKontostand, heightKontostand, fontsize, widthKontostand]

#festlegen was passiert wenn auf die Zahlen geklickt wird
def buttonTipp1_click():
    v1.set(str(int(v1.get())+1))#Textvariable des Textfeldes unter dem Button wird um 1 erhöht. Variable kann nur den Typ string annehmen
    
def buttonTipp2_click():
    v2.set(str(int(v2.get())+1))
    
def buttonTipp3_click():
    v3.set(str(int(v3.get())+1))
    
def buttonTipp4_click():
    v4.set(str(int(v4.get())+1))
    
def buttonTipp5_click():
    v5.set(str(int(v5.get())+1))
    
def buttonTipp6_click():
    v6.set(str(int(v6.get())+1))
    
#Es wird geprüft, ob schon auf eine Zahl gesetzt wurde. Wenn ja wird der Button "klickbar" gemacht, wenn nicht gesperrt
def pruefeTipp(event):
    if int(v1.get()) == 0 and int(v2.get()) == 0 and int(v3.get()) == 0 and int(v4.get()) == 0 and int(v5.get()) == 0 and int(v6.get()) == 0:
        buttonWuerfel['state'] = tk.DISABLED
    else:
        buttonWuerfel['state'] = tk.NORMAL

#Es wird ausgewertet, wie viel man gewonnen oder verloren hat, abhängig von den uebergebenen Wuerfelergebnissen
def auswertung(wErgebnis):
    kontostand = int(vKontostand.get())
    getippt = [int(v1.get()), int(v2.get()), int(v3.get()), int(v4.get()), int(v5.get()), int(v6.get())]
    gewuerfelt = [0, 0, 0, 0, 0, 0]
    for element in wErgebnis:
        x = gewuerfelt[element-1]
        x += 1
        del gewuerfelt[element-1]
        gewuerfelt.insert(element-1, x)
    for i in range(6):
        wuerfel = gewuerfelt[i]
        tipp = getippt[i]
        if wuerfel == 0:
            wuerfel = -1
        kontostand += tipp * wuerfel
        gewinn = kontostand - int(vKontostand.get())
    vKontostand.set(str(kontostand))
    #wenn man weiterspielen möchte
    def buttonJaKlick():
        #Default Bild der Würfel
        labelWuerfel1.config(image = augenzahl1)
        labelWuerfel2.config(image = augenzahl1)
        labelWuerfel3.config(image = augenzahl1)
        #getipptes aus Vorrunde entfernen
        v1.set('0')
        v2.set('0')
        v3.set('0')
        v4.set('0')
        v5.set('0')
        v6.set('0')
        #Buttons freischalten
        buttonTipp1['state'] = tk.NORMAL
        buttonTipp2['state'] = tk.NORMAL
        buttonTipp3['state'] = tk.NORMAL
        buttonTipp4['state'] = tk.NORMAL
        buttonTipp5['state'] = tk.NORMAL
        buttonTipp6['state'] = tk.NORMAL
        #Eingabefelder zum Tippen freischalten
        entryTipp1['state'] = tk.NORMAL
        entryTipp2['state'] = tk.NORMAL
        entryTipp3['state'] = tk.NORMAL
        entryTipp4['state'] = tk.NORMAL
        entryTipp5['state'] = tk.NORMAL
        entryTipp6['state'] = tk.NORMAL
        neuTop.quit()
        neuTop.destroy()
    #Wenn nicht Spiel schließen   
    def buttonNeinKlick():
        exit()
        sys.exit()
    #Neues Fenster öffnen und Position und Größe definieren
    neuTop = Toplevel()
    neuTop.title('Auswertung')
    neuTop.geometry('320x120+' + str(int(groesse()[0]*0.47)) + '+' + str(int(groesse()[1]*0.1)) )
    antwort = ''
    #Je nachdem, ob man gewonnen, verloren hat oder nichts passiert ist, entsprechenden Text ins Fenster schreiben
    if gewinn < 0:
        antwort = 'Du hast ' + str(gewinn*-1) + ' verloren \n Dein neuer Kontostand ist: '+ str(kontostand) + '\nWillst du noch einmal würfeln?'
    elif gewinn > 0:
        antwort = 'Du hast ' + str(gewinn) + ' gewonnen \n Dein neuer Kontostand ist: '+ str(kontostand) + '\nWillst du noch einmal würfeln?'
    elif gewinn == 0:
        antwort = 'Du hast nichts gewonnen bzw. verloren \n Dein neuer Kontostand ist: '+ str(kontostand) + '\nWillst du noch einmal würfeln?'
    #Label, in das der Text geschriben wird, deklarieren
    labelNeuTop = Label(master = neuTop, text = antwort )
    labelNeuTop.place(x = 10, y = 5, width = 300, height = 60)
    #Button zum Weitermachen und Verlassen definieren
    buttonJa = Button(master = neuTop, text='Ja', command = buttonJaKlick)
    buttonJa.place(x = 10, y = 90, width = 150, height = 20)
    buttonNein = Button(master = neuTop, text = 'Nein', command = buttonNeinKlick)
    buttonNein.place(x = 160, y = 90, width = 150, height = 20)

#würfeln (Animation)
def wuerfeln(zeit):
    #Tipp Buttons werden gesperrt, sodass Auswertung korrekt erfolgt
    buttonTipp1['state'] = tk.DISABLED
    buttonTipp2['state'] = tk.DISABLED
    buttonTipp3['state'] = tk.DISABLED
    buttonTipp4['state'] = tk.DISABLED
    buttonTipp5['state'] = tk.DISABLED
    buttonTipp6['state'] = tk.DISABLED
    
    #Tipp Eingabefelder werden gesperrt, sodass Auswertung korrekt erfolgt
    entryTipp1['state'] = tk.DISABLED
    entryTipp2['state'] = tk.DISABLED
    entryTipp3['state'] = tk.DISABLED
    entryTipp4['state'] = tk.DISABLED
    entryTipp5['state'] = tk.DISABLED
    entryTipp6['state'] = tk.DISABLED
    
    #Fuer die drei Würfel wird jeweils folgendes gemacht:
    #1. zufällige Zahl zwischen 1 und 6 wählen
    #2. je nach Zahl Bild ändern durch anderes Bild mit entsprechender Augenzahl ersetzen 
    augenzahlWuerfel1 = randint(1,6)
    if augenzahlWuerfel1 == 1:
         labelWuerfel1.config(image = augenzahl1)
    elif augenzahlWuerfel1 == 2:
         labelWuerfel1.config(image = augenzahl2)
    elif augenzahlWuerfel1 == 3:
         labelWuerfel1.config(image = augenzahl3)
    elif augenzahlWuerfel1 == 4:
         labelWuerfel1.config(image = augenzahl4)
    elif augenzahlWuerfel1 == 5:
         labelWuerfel1.config(image = augenzahl5)
    elif augenzahlWuerfel1 == 6:
         labelWuerfel1.config(image=augenzahl6)
         
    augenzahlWuerfel2 = randint(1,6)
    if augenzahlWuerfel2 == 1:
         labelWuerfel2.config(image = augenzahl1)
    elif augenzahlWuerfel2 == 2:
         labelWuerfel2.config(image = augenzahl2)
    elif augenzahlWuerfel2 == 3:
         labelWuerfel2.config(image = augenzahl3)
    elif augenzahlWuerfel2 == 4:
         labelWuerfel2.config(image = augenzahl4)
    elif augenzahlWuerfel2 == 5:
         labelWuerfel2.config(image = augenzahl5)
    elif augenzahlWuerfel2 == 6:
         labelWuerfel2.config(image = augenzahl6)
         
    augenzahlWuerfel3 = randint(1,6)
    if augenzahlWuerfel3 == 1:
         labelWuerfel3.config(image = augenzahl1)
    elif augenzahlWuerfel3 == 2:
         labelWuerfel3.config(image = augenzahl2)
    elif augenzahlWuerfel3 == 3:
         labelWuerfel3.config(image = augenzahl3)
    elif augenzahlWuerfel3 == 4:
         labelWuerfel3.config(image = augenzahl4)
    elif augenzahlWuerfel3 == 5:
         labelWuerfel3.config(image = augenzahl5)
    elif augenzahlWuerfel3 == 6:
         labelWuerfel3.config(image = augenzahl6) 
    
    #Abbruchbedingung für Rekursion (Rekursion um Würfelanimation zu machen)
    if zeit > 400:
        #Wenn Zeit größer 400 milisek. 
        wuerfelErgebnis = [augenzahlWuerfel1, augenzahlWuerfel2, augenzahlWuerfel3]#Liste aus Würfelergebnis erstellen
        #Auswertung aufrufen und Würfelergebnis übergeben
        fenster.after(500, lambda: auswertung(wuerfelErgebnis))#nach 500 milisek. die Auswertung mit wuerfelErgebnis aufrufen, da sich in dieser Zeit die Würfel noch einmal ändern
    else:
        fenster.after(zeit, lambda: wuerfeln(zeit+25))#sonst Funktion nach bestimmter Zeit neu aufrufen und Zeit um 25 milisek. vergrößern(Lambda-Funktion habe ich benutz da ich sonst keine Parameter übergeben kann)
        
#Bildschirmgröße durch Funktion bestimmen
bildschirmGroesse = groesse()

#werte_tipp aufrufen mit Bildschirmgrößen und den Variablen die passenden Werte zuweisen
tippWerte = werte_tipp(bildschirmGroesse[0], bildschirmGroesse[1])
tippxWerte = tippWerte[0]
tippButtonyWert = tippWerte[1]
tippButtonHeight = tippWerte[2]
tippButtonWidth = tippWerte[3]
tippButtonFontSeize = tippWerte[4]
tippEingabeyWert = tippWerte[5]
tippEingabeHeight = tippWerte[6]
tippEingabeFontSize = tippWerte[7]

#werteWuerfel aufrufen mit Bildschirmgrößen und den Variablen die passenden Werte zuweisen
wuerfelWerte = werteWuerfel(bildschirmGroesse[0], bildschirmGroesse[1])
xWerteWuerfel = wuerfelWerte[0]
widthWuerfel = wuerfelWerte[1]
yWertwuerfel = wuerfelWerte[2]
buttonHeigthWuerfel = wuerfelWerte[3]
buttonyWertWuerfel = wuerfelWerte[4]
buttonxWert = wuerfelWerte[5]
buttonWidth = wuerfelWerte[6]

#werteKonto aufrufen mit Bildschirmgrößen und den Variablen die passenden Werte zuweisen
werteKontoLabel = werteKonto(bildschirmGroesse[0], bildschirmGroesse[1])
xWertBeide = werteKontoLabel[0]
yWertUeberschrift = werteKontoLabel[1]
heigthUeberschrift = werteKontoLabel[2]
widthUeberschrift = werteKontoLabel[3]
yWertKontostand = werteKontoLabel[4]
heightKontostand = werteKontoLabel[5]
fontsizeKontostand = werteKontoLabel[6]
widthKontostand = werteKontoLabel[7]

#Farben durch Variablen festlegen
backgroundTippButton = 'green'
buttonTextFarbe = 'yellow'
entryTextFarbe = 'yellow'
entryBackgroundFarbe = 'green'
backgroundFarbe = 'green'
fenster['bg'] = 'green'

#Augenzahlenbilder Variablen zuordnen
augenzahl1 = PhotoImage(file='Bilder\A1.gif')
augenzahl2 = PhotoImage(file='Bilder\A2.gif')
augenzahl3 = PhotoImage(file='Bilder\A3.gif')
augenzahl4 = PhotoImage(file='Bilder\A4.gif')
augenzahl5 = PhotoImage(file='Bilder\A5.gif')
augenzahl6 = PhotoImage(file='Bilder\A6.gif')



#Schrift Eigenschaften für Button und Eingabefeld festlegen
buttonFont = font.Font(family = 'Helvetica', size = tippButtonFontSeize, weight = 'bold')
entryFont = font.Font(family = 'Helvetica', size = tippEingabeFontSize, weight = 'bold')
buttonFontWuerfeln = font.Font(family = 'Helvetica', size = int(0.1 * buttonWidth), weight = 'bold')
kontoFont = font.Font(family = 'Helvetica', size = int(0.05 * widthUeberschrift), weight = 'bold')
kontostandFont = font.Font(family = 'Helvetica', size = fontsizeKontostand, weight = 'bold')

#Zahlen, die Buttons sind, erstellen, platzieren und Eigenschaften festlegen
buttonTipp1 = Button(master = fenster, text = '1', command = buttonTipp1_click, font = buttonFont, fg = buttonTextFarbe, bg = backgroundTippButton, relief = 'ridge', state = tk.NORMAL)
buttonTipp1.place(x = tippxWerte[0], y = tippButtonyWert, width = tippButtonWidth , height = tippButtonHeight)

buttonTipp2 = Button(master = fenster, text = '2', command = buttonTipp2_click, font = buttonFont, fg = buttonTextFarbe, bg = backgroundTippButton, relief = 'ridge', state = tk.NORMAL)
buttonTipp2.place(x = tippxWerte[1], y = tippButtonyWert, width = tippButtonWidth , height = tippButtonHeight)

buttonTipp3 = Button(master = fenster, text = '3', command = buttonTipp3_click, font = buttonFont, fg = buttonTextFarbe, bg = backgroundTippButton, relief = 'ridge', state = tk.NORMAL)
buttonTipp3.place(x = tippxWerte[2], y = tippButtonyWert, width = tippButtonWidth , height = tippButtonHeight)

buttonTipp4 = Button(master = fenster, text = '4', command = buttonTipp4_click, font = buttonFont, fg = buttonTextFarbe, bg = backgroundTippButton, relief = 'ridge', state = tk.NORMAL)
buttonTipp4.place(x = tippxWerte[3], y = tippButtonyWert, width = tippButtonWidth , height = tippButtonHeight)

buttonTipp5 = Button(master = fenster, text = '5', command = buttonTipp5_click, font = buttonFont, fg = buttonTextFarbe, bg = backgroundTippButton, relief = 'ridge', state = tk.NORMAL)
buttonTipp5.place(x = tippxWerte[4], y = tippButtonyWert, width = tippButtonWidth , height = tippButtonHeight)

buttonTipp6 = Button(master = fenster, text = '6', command = buttonTipp6_click, font = buttonFont, fg = buttonTextFarbe, bg = backgroundTippButton, relief = 'ridge', state = tk.NORMAL)
buttonTipp6.place(x = tippxWerte[5], y = tippButtonyWert, width = tippButtonWidth , height = tippButtonHeight)

#Textvariablen Typ festlegen
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
#Kontostand als Textvariable auf Default 200 setzten
vKontostand = StringVar()


#Textvariablen auf 0 setzen
v1.set('0')
v2.set('0')
v3.set('0')
v4.set('0')
v5.set('0')
v6.set('0')
#auf Default 200 setzten
vKontostand.set('100')

#Eingabe/Anzeigefelder erstellen, platzieren und EIgenschaften festlegen
entryTipp1 = Entry(master = fenster, background = entryBackgroundFarbe, justify = 'center', font = entryFont, fg = entryTextFarbe, textvariable = v1, relief = 'flat', state = tk.NORMAL, disabledbackground = entryBackgroundFarbe)
entryTipp1.place(x = tippxWerte[0], y = tippEingabeyWert, width = tippButtonWidth, height = tippEingabeHeight)

entryTipp2 = Entry(master = fenster, background = entryBackgroundFarbe, justify = 'center', font = entryFont, fg = entryTextFarbe, textvariable = v2, relief = 'flat', state = tk.NORMAL, disabledbackground = entryBackgroundFarbe)
entryTipp2.place(x = tippxWerte[1], y = tippEingabeyWert, width = tippButtonWidth, height = tippEingabeHeight)

entryTipp3 = Entry(master = fenster, background = entryBackgroundFarbe, justify = 'center', font = entryFont, fg = entryTextFarbe, textvariable = v3, relief = 'flat', state = tk.NORMAL, disabledbackground = entryBackgroundFarbe)
entryTipp3.place(x = tippxWerte[2], y = tippEingabeyWert, width = tippButtonWidth, height = tippEingabeHeight)

entryTipp4 = Entry(master = fenster, background = entryBackgroundFarbe, justify = 'center', font = entryFont, fg = entryTextFarbe, textvariable = v4, relief = 'flat', state = tk.NORMAL, disabledbackground = entryBackgroundFarbe)
entryTipp4.place(x = tippxWerte[3], y = tippEingabeyWert, width = tippButtonWidth, height = tippEingabeHeight)

entryTipp5 = Entry(master = fenster, background = entryBackgroundFarbe, justify = 'center', font = entryFont, fg = entryTextFarbe, textvariable = v5, relief = 'flat', state = tk.NORMAL, disabledbackground = entryBackgroundFarbe)
entryTipp5.place(x = tippxWerte[4], y = tippEingabeyWert, width = tippButtonWidth, height = tippEingabeHeight)

entryTipp6 = Entry(master = fenster, background = entryBackgroundFarbe, justify = 'center', font = entryFont, fg = entryTextFarbe, textvariable = v6, relief = 'flat', state = tk.NORMAL, disabledbackground = entryBackgroundFarbe)
entryTipp6.place(x = tippxWerte[5], y = tippEingabeyWert, width = tippButtonWidth, height = tippEingabeHeight)


#Image Würfel1 einbinden
labelWuerfel1 = Label(master = fenster, image = augenzahl1, bg = backgroundFarbe)
labelWuerfel1.place(x = xWerteWuerfel[0], y = yWertwuerfel, width = widthWuerfel, height = widthWuerfel)

#Image Würfel2 einbinden
labelWuerfel2 = Label(master = fenster, image = augenzahl1, bg = backgroundFarbe)
labelWuerfel2.place(x = xWerteWuerfel[1], y = yWertwuerfel, width = widthWuerfel, height = widthWuerfel)

#Image Würfel3 einbinden
labelWuerfel3 = Label(master = fenster, image = augenzahl1, bg = backgroundFarbe)
labelWuerfel3.place(x = xWerteWuerfel[2], y = yWertwuerfel, width = widthWuerfel, height = widthWuerfel)


#Button zum Würfeln erstellen, platzieren un Eigenschaften festlegen(Lambda-Funktion verwendet um Parameter der Funktion zu übergeben)
buttonWuerfel = Button(master = fenster, text = 'Würfeln', command = lambda: wuerfeln(10), font = buttonFontWuerfeln, fg = buttonTextFarbe, bg = backgroundTippButton, state = tk.DISABLED, relief = 'ridge')
buttonWuerfel.place(x = buttonxWert, y = buttonyWertWuerfel, width = buttonWidth , height = buttonHeigthWuerfel)


#Label mit Überschrift erstellen, platzieren un Eigenschaften festlegen
labelUeberschrift = Label(master = fenster, text = 'Konto:', font = kontoFont, bg = backgroundFarbe, fg = 'white')
labelUeberschrift.place(x = xWertBeide, y = yWertUeberschrift, width = widthUeberschrift , height = heigthUeberschrift)

#Label das Kontostand anzeigt erstellen, platzieren un Eigenschaften festlegen
labelkontostand = Label(master = fenster, font = kontostandFont, textvariable = vKontostand, bg = backgroundFarbe, fg = 'white')
labelkontostand.place(x = xWertBeide, y = yWertKontostand, width = widthKontostand , height = heightKontostand)


#Name und Größe des Fensters(Vollbild) festlegen
fenster.title('chuck a luck')
fenster.geometry(str(bildschirmGroesse[0]) + 'x' + str(bildschirmGroesse[1]))

#wenn man einen Button berührt oder ein Eingabefeld beschreibt, dann rufe pruefeTipp auf um zu prüfen, ob man etwas getippt hat und somit würfeln darf
fenster.bind('<Button>', pruefeTipp)
fenster.bind('<Enter>', pruefeTipp)

#Fenster bauen
fenster.mainloop()
