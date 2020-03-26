# HOT Home Office Timer
# Mathias Harlfinger
# mathias@harlfinger.net
#
# Version 0.91
# 25.03.2020
#
# free use and distributance
# 
import RPi.GPIO as GPIO
import time
import datetime
from datetime import datetime
import os.path
import os
import stat

# Variablen initialisieren

WorkSwitch=4    # Schalter auf Pin 4
LED_Work=14     # LED Arbeiten auf Pin 14
LED_NoWork=15   # LED Freizeit auf Pin 15
status=0        # Freizeit=0; Arbeiten=1
stopp=0         # Zeitpunkt fallende Flanke 
start=0         # Zeitpunkt steigende Flanke
timestamp=0
timestamp_time=0
timestamp_date=0
sstart_date=0
sstart_time=0
sstopp_date=0
sstopp_time=0
path=""

GPIO.setmode(GPIO.BCM)  # Zaehlweise der Pins auf BCM festlegen

GPIO.setup(WorkSwitch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)# Festlegung fuer Schalter als Eingang mit PullDown Widerstand
GPIO.setup(LED_Work, GPIO.OUT)# Festlegung auf Ausgang fuer LED Arbeiten
GPIO.setup(LED_NoWork, GPIO.OUT)# Festlegung auf Ausgang fuer LED Freizeit
GPIO.output(LED_Work, GPIO.LOW)# LED Arbeiten ausschalten
GPIO.output(LED_NoWork, GPIO.LOW)# LED Freizeit ausschalten

# Wenn Aenderung der Schalterstellung erkannt wird dann springt der Interrupt hier rein     
def get_timestamp():
    global timestamp
    global timestamp_time
    global timestamp_date 
    
    timestamp = datetime.now().strftime('%d.%m.%Y %H:%M:%S')    #Aktueller Zeitstempel mit Datum & Uhrzeit
    timestamp_date = datetime.now().strftime('%d.%m.%Y')        #Aktueller Zeitstempel mit Datum
    timestamp_time = datetime.now().strftime('%H:%M:%S')        #Aktueller Zeitstempel mit Uhrzeit
    
# Wenn Aenderung der Schalterstellung erkannt wird dann springt der Interrupt(Zeile 100) hier rein     
def keypress(channel):
    #Verwendung globaler Variablen
    global start  
    global stopp 
    global WorkSwitch
    global LED_Work
    global LED_NoWork
    global status
    global timestamp
    global timestamp_time
    global timestamp_date
    global sstart_date
    global sstart_time  
    global sstopp_date
    global sstopp_time
  
    now = datetime.now()
  
    if status == 0:       # aus Freizeit kommend, Startzeit speichern
        get_timestamp() #Zeitstempel holen
        start=timestamp_time #Startzeit zwischenspeichern fuer Deltaberechnung
        sstart_date="%s" % (timestamp_date)#Startdatum als String zwischenspeichern fuer Tabelleneintrag 
        sstart_time="%s" % (timestamp_time)#Startzeit als String zwischenspeichern fuer Tabelleneintrag 
        status=1        #Status auf Arbeiten setzen

        GPIO.output(LED_Work, GPIO.HIGH)# LED Arbeiten einschalten
        GPIO.output(LED_NoWork, GPIO.LOW)# LED Freizeit ausschalten
        print("Start Work: %s" % (timestamp))

    else:                         # aus Arbeitszeit kommend, Stoppzeit speichern und in Datei schreiben
        get_timestamp()         #Zeitstempel holen
        stopp=timestamp_time #Stopp zwischenspeichern fuer Deltaberechnung
        sstopp_date="%s" % (timestamp_date)#Stoppdatum als String zwischenspeichern fuer Tabelleneintrag 
        sstopp_time="%s" % (timestamp_time)#Stoppzeit als String zwischenspeichern fuer Tabelleneintrag 
        status=0            #Status auf Freizeit setzen
        tdelta = datetime.strptime(stopp, '%H:%M:%S') - datetime.strptime(start, '%H:%M:%S') # Zeitdifferenz berechnen
        stdelta="%s"% tdelta    #Time-Delta in String umwandeln

        GPIO.output(LED_Work, GPIO.LOW)# LED Arbeiten ausschalten
        GPIO.output(LED_NoWork, GPIO.HIGH)# LED Freizeit einschalten
        print("End Work: %s" % (timestamp))
        print("Working Time = %s"% tdelta)

        f= open("/home/pi/hot/hot.csv","a+")    #CSV-Datei oeffnen
        f.write(sstart_date+","+sstart_time+","+sstopp_date+","+sstopp_time+","+ stdelta +"\r\n") #Zeile mit Start-, Stopp- und Zeitstempel und Differenzzeit speichern
        f.close()       #Datei schliessen








# Interrupt fuer steigende Flanke aktivieren. Bei Tasterstellungsaenderung Sprung in Funktion "keypress()", Schalterentprellung fuer 1000ms
GPIO.add_event_detect(WorkSwitch, GPIO.RISING, callback=keypress, bouncetime=1000)    
    
    

# Hauptschleife - ueberprueft csv Datei, legt Ueberschrift an, wenn nicht existend, laeuft dann in Endlosschleife (gibt nur Wartemeldung im Sekundentakt aus(Zeile 139), wenn erforderlich...)
def main():
    global path
    
    hot_path = "/home/pi/hot/"
    hot_file = "hot.csv"

    folder_exists = os.path.isdir(hot_path)             #Pruefe Ordner Verfuegbarkeit
    file_exists = os.path.isfile(hot_path+hot_file)     #Pruefe Datei Verfuegbarkeit

    if folder_exists == False:  # Ordner fehlt, dann
        os.mkdir(hot_path)      # Lege Ordner an
        os.chmod(hot_path , stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)   #umfassende Schreibrechte auf den Ordner

    
    if file_exists: 
        print("CSV-File exists\r\n")
    else:   #Datei fehlt, dann
        f= open("/home/pi/hot/hot.csv","a+") #Lege Datei an
        f.write("Start work date,Start work time,End work date,End work time,Working time"+"\r\n") #schreibe ueberschriften ueber die Spalten
        f.close() #Schliesse Datei
        os.chmod("/home/pi/hot/hot.csv" , stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)   #umfassende Schreibrechte auf die Datei
        print("CSV-File not existing - generated\r\n")

    print("Stop with CTRL+C\r\nwaiting for start working key press")
    GPIO.output(LED_NoWork, GPIO.HIGH)# LED Freizeit einschalten: Betriebsbereitschaft    
    while 1: #Endlosschleife
        #print ("Wait....") #Ausgabe im Sekundentakt "#" entfernen!
        #time.sleep(1)  
        pass    #No operation
 
 
 
 
 

if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            GPIO.output(LED_Work, GPIO.LOW)# LED Arbeiten ausschalten
            GPIO.output(LED_NoWork, GPIO.LOW)# LED Freizeit ausschalten
            GPIO.cleanup()
            print("\n\n Test finished ! \n") 
            sys.exit()

