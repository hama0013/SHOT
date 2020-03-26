<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 6.1.5.2 (Linux)"/>
	<meta name="created" content="2020-03-25T15:57:57.426724777"/>
	<meta name="changed" content="2020-03-26T21:54:13.098849840"/>
</head>
<body lang="de-DE" dir="ltr">
<table width="100%" cellpadding="4" cellspacing="0" style="page-break-before: always; page-break-inside: avoid">
	<col width="85*"/>

	<col width="85*"/>

	<col width="85*"/>

	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p align="center">
			<font size="7" style="font-size: 36pt"><b>SHOT</b></font><br/>
Simple
			Home Office Timer</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
<p><b>Wie das Projekt entstand:</b></p>
<p>Aufgrund der Corona-Krise werden ja zunehmend Mitarbeiter von
Ihren Firmen nach Hause ins „Home Office“ geschickt. Zum „Home
Office“ kann man nun unterschiedliche Einstellungen haben (ich
enthalte mich hier einer Wertung), allerdings ist das unbestritten
die geeignetste Möglichkeit um den sozialen Kontakt in der
Arbeitswelt einzuschränken und somit die Ausbreitung des Virus zu
verhindern. Was mich jedoch massiv nervt, sind die Maßnahmen zur
Dokumentation der Arbeitszeit. Entweder vergesse ich es zu notieren
oder bin aufgrund der Tätigkeit verhindert die korrekten Start- und
Endezeiten sowie Unterbrechungen zu notieren. Auf dem Papier
funktioniert es überhaupt nicht… Per Excel-Tabelle auf dem PC auch
nicht viel besser. Also schrieb ich ein kleines Excel-(VBA) Script,
mit dem ich per Button meine Start- und Stoppzeiten anklicken konnte
und die Zeitstempel in einer Excle-Liste registriert wurden. Das
funktionierte schon besser, allerdings war es sehr problematisch, da
ich abhängig vom laufenden Computer war: Hier passierte es, dass ich
mich an den Arbeitsplatz setzte, bereits ein Telefongespräch begann
und den Rechner startete. Bis der Recher hochgefahren war, ich mich
einloggte, hatte ich auch schon wieder vergessen mein Script zu
bedienen und meine Startzeit nicht registriert. Auch Unterbrechungen
durch meine Frau/Kind konnte ich oft nicht rechtzeitig aktivieren, da
der Rechner gerade in Stand-By war oder ich schlicht den Button nicht
im Sichtfeld hatte und vergas. <br/>
Nächste Überlegung war, das
selbe Script für eine Handy-App oder über den Raspberry anzupassen.
Ich entschied mich für den Raspberry, da bereits viele identische
Tools für Handys im AppStore verfügbar sind aber keines meiner
Erwartung entsprach. Entweder komplett überladen oder durch Werbung
zugemüllt oder zu teuer. Auch die Anwendung über das Mobiltelefon
ist nur bedingt komfortabler, da, wie beim PC, eine Anmeldung und
Starten der App mit weiteren Schritten erforderlich ist. <br/>
Was
ich benötige ist einfach ein Taster und 2 LEDs, die mir den
aktuellen Zustand zeigen (Arbeiten oder Freizeit) und bei dem ich
ausser einem Tastendruck nichts weiteres machen muss. Jeder
Tastendruck soll dann lediglich in einer Excel-Tabelle den Start und
den Stopp der Arbeitszeit registrieren und bei Bedarf als Datei
ausgelesen werden können. <b>Ich möchte </b><u><b>nichts </b></u><b>zusätzlich
starten, anmelden oder zusätzlich </b><b>bedienen</b><b> müssen.</b></p>
<p><i><b>Das Ergebnis ist der SHOT (Simple Home Office Timer):</b></i></p>
<p><br/>
<br/>

</p>
<table width="100%" cellpadding="4" cellspacing="0" style="page-break-inside: avoid">
	<col width="85*"/>

	<col width="85*"/>

	<col width="85*"/>

	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><font size="4" style="font-size: 14pt"><b>Das
			Komplettsystem SHOT</b></font><img src="images/IMG_0454.JPG" name="Bild5" align="bottom" width="622" height="466" border="0"/>
</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
<p>Wie man hier sehen kann besteht das ganze lediglich aus dem Gerät
mit Spannungsversorgung, einem Taster und 2 LEDs. Die LEDs sind
farblich unterschieden, sodass der aktuelle Zustand: Arbeitszeit
(Rot) und Freizeit (Grün) auch eindeutig zu sehen ist. Mit dem
Taster wird lediglich zwischen den Zuständen Arbeit oder Freizeit
hin- und hergeschaltet. Nach dem Einschalten bzw. bestromen sind erst
mal beide LEDs aus, da das Betriebssystem hochfahren muss.
Betriebsbereitschaft wird durch Leuchten der grünen „Freizeit-LED“
angezeigt. Nach dem ersten Betätigen der Taste schaltet die rote LED
ein um zu zeigen, dass der Start der Arbeitszeit registriert wurde
und man sich momentan in der Arbeitsphase befindet. Beim erneuten
Drücken der Taste bzw. Umschalten der LEDs wird jedesmal der
Zeitpunkt registriert und in einer Excel-Tabelle (CSV) zeilenweise
hinterlegt. Zusätzlich wird stets am Ende eines Arbeitszyklus, also
Schalten von Arbeit nach Freizeit das Delta zwischen Start und Stopp
der Arbeitsphase in der Zeile in „Stunden:Minuten:Sekunden“
hinterlegt. Die Datei kann jederzeit ausgelesen und zum Übertrag in
die eigenen Zeitsysteme verwendet werden. Ein einfacher WEB-Zugriff
auf den SHOT ist in Vorbereitung.</p>
<table width="100%" cellpadding="4" cellspacing="0" style="page-break-inside: avoid">
	<col width="85*"/>

	<col width="85*"/>

	<col width="85*"/>

	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><font size="4" style="font-size: 14pt"><b>Die
			automatisch erstellte CSV-Datei. Kann mit
			Tabellenkalkulationsprogrammen wie Excel oder LibreOffice
			problemlos geöffnet werden.</b></font><img src="README.md_html_f8b773daa3a89999.jpg" name="Bild6" align="bottom" width="622" height="403" border="0"/>
</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
<p>Da ich selbst begeisterter Raspi-Anwender bin versuche ich auch
stets andere von meinem Hobby zu begeistern. Das Projekt wendet sich
an alle interessierte Raspi-Neulinge und Anwender, die nach
nachbaubaren Projekten suchen. Evtl. findet der eine oder andere über
solch ein kleines Projekt den Einstieg in die Raspi-Verwendung und
Python-Programmierung. Da ich selbst bereits ein wenig Erfahrung in
der Erwachsenen- und Schulkinder-Pädagogik mitbekommen habe, ist mir
bewusst, dass man nur mit nachvollziehbarer Dokumentation Spass an
DIY-Projekten vermitteln kann. Dieses Projekt kann in 4 wesentliche
Rubriken unterteilt werden:</p>
<ol>
	<li><p>Raspberry Systemaufbau allgemein</p>
	<li><p>SHOT Komponenten und Gehäuse</p>
	<li><p>Software Vorbereitung für SHOT und Einbindung in den
	Raspberry</p>
	<li><p>Programmbeschreibung SHOT</p>
</ol>
<p><br/>
<br/>

</p>
<p><font size="4" style="font-size: 14pt"><b>1. Raspberry
Systemaufbau allgemein</b></font></p>
<p>Da das gesamte System auf einem RaspberryPi mit aktuellem
Betriebssystem aufgebaut ist, sind die Vorbereitungen zur Verwendung
hier nicht detailliert beschrieben. Man muss erst das Betriebssystem
auf die Flash-Karte spielen und den Raspi mit Tastatur, Monitor und
ggf. Maus und Spannungsversorgung verbinden. Diese Vorgehensweise
findet man perfekt beschrieben hier:</p>
<p><a href="https://www.digitalewelt.at/raspberry-pi-4-rasbian-buster-installieren-und-einrichten/" target="_blank">https://www.digitalewelt.at/raspberry-pi-4-rasbian-buster-installieren-und-einrichten/</a></p>
<p>Als Hardware reicht ein einfacher Raspberry ZERO, am besten in der
Variante W (mit WLAN on Board) aus. Einfacher wird es noch in der
Variante WH (WLAN und mit angelöteten Header-Pins) oder gleich einen
Raspberry A, B(1-4) …. (Bezugsquellen siehe Punkt 2.)<br/>
<br/>
<br/>

</p>
<p><br/>
<br/>

</p>
<p><font size="4" style="font-size: 14pt"><b>2. SHOT Komponenten und
Gehäuse</b></font></p>
<p>Als notwendige Komponenten sind erforderlich:</p>
<ol>
	<li><p>Ein Taster (Schließer)</p>
	<li><p>Zwei Low-Power LEDs (2mA) Grün und Rot</p>
	<li><p>Zwei Widerstände 330 Ohm (Orange-Orange-Braun)</p>
	<li><p>Wenige Zentimeter Kabel</p>
	<li><p>Ein Raspberry (Typ beliebig)</p>
	<li><p>Ein Micro-USB Netzteil</p>
	<li><p>Ein Gehäuse, passend für die Raspberry-Variante</p>
</ol>
<p>Zum Gehäuse kann man beliebige Varianten, vom Eigenbau-Karton bis
zum teuren Metal-Case verwenden. Es müssen lediglich drei Löcher
für LEDs und den Taster rein. Wer noch kein Raspi oder Gehäuse
besitzt schaut sich am besten bei einschlägigen Lieferanten um. Dort
sind auch LEDs und Widerstände erhältlich:</p>
<p><a href="https://www.berrybase.de/" target="_blank">https://www.berrybase.de/</a></p>
<p><a href="https://www.rasppishop.de/" target="_blank">https://www.rasppishop.de/</a></p>
<p><a href="https://shop.pimoroni.com/" target="_blank">https://shop.pimoroni.com/</a></p>
<p>Der Taster wird einfach nur zwischen Pin 1 (3.3V) und Pin 7(GPIO4)
angeschlossen. Im Code wird nur die Aufwärtsflanke von 0 nach 3.3V
(Interrupt) ausgewertet. Ein notwendiger „Pull-Down-Widerstand“
um den Pegel im geöffneten Tasterzustand definiert auf 0V
herunterzuziehen, wird softwareseitig zugeschaltet. <br/>
Die LEDs
werden jeweils in Reihenschaltung mit dem 330Ohm Widerstand zwischen
Pin 6 (GND) und Pin 8 (GPIO14) für LED Rot (Arbeiten) sowie zwischen
Pin 6 (GND) und PIN 10 (GPIO15) für LED Grün (Freizeit)
angeschlossen. Auch wenn hier ein Bild des RaspberryPI TypB3
abgebildet ist, ist das Pin-Layout für alle Raspberry-Typen für
dieses Projekt identisch.</p>
<table width="100%" cellpadding="4" cellspacing="0" style="page-break-inside: avoid">
	<col width="85*"/>

	<col width="85*"/>

	<col width="85*"/>

	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="background: transparent" style="border: none; padding: 0cm"><p>
			<font size="4" style="font-size: 14pt"><b>Pin-Belegung eines
			Raspberry Pi</b></font><img src="README.md_html_ace9d8c5c1e4f3c0.jpg" name="Bild4" align="bottom" width="600" height="491" border="0"/>
</p>
			<p><br/>
<br/>

			</p>
			<p> 
			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><font size="4" style="font-size: 14pt"><b>Notwendige
			Hardwarebeschaltung für den SHOT. Zu beachten ist, dass die LEDs
			mit dem Minus-Pin (abgeflachte Seite am Leuchtkörper oder kurzes
			Beinchen) an Pin 6 (GND) angeschlossen werden. Der Widerstand kann
			am Plus- oder Minus-Pin der LED angeschlossen werden. </b></font>
			<img src="README.md_html_59e1196ad85319e3.jpg" name="Bild2" align="bottom" width="622" height="303" border="0"/>
</p>
			<p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p> 
			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><font size="4" style="font-size: 14pt"><b>Alle notwendigen
			Teile (ohne Netzteil)<img src="images/IMG_0449.JPG" name="Bild9" align="bottom" width="622" height="466" border="0"/>
</b></font></p>
			<p> 
			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><br/>
<br/>

			</p>
			<p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><font size="4" style="font-size: 14pt"><b>So sieht es real aus<img src="images/IMG_0451.JPG" name="Bild7" align="bottom" width="622" height="466" border="0"/>
</b></font></p>
			<p> 
			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><font size="4" style="font-size: 14pt"><b>Hier wurden die LEDs
			von hinten in den Deckel geklebt und der Taster angeschraubt<img src="images/IMG_0452.JPG" name="Bild8" align="bottom" width="622" height="466" border="0"/>
</b></font></p>
			<p> 
			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><font size="4" style="font-size: 14pt"><b>Das
			Gerät in Aktion<img src="images/IMG_0455.JPG" name="Bild10" align="bottom" width="622" height="466" border="0"/>
</b></font></p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
<p><br/>
<br/>

</p>
<p><font size="4" style="font-size: 14pt"><b>3. Software Vorbereitung
für SHOT</b></font></p>
<p>Die meisten Befehle zur Inbetriebnahme des SHOT kann man über das
Terminal tätigen:</p>
<p>Soweit alles vorbereitet ist und der Raspberry läuft, muss zuerst
das Arbeitsverzeichniss angelegt werden. Ich schlage einfach einen
Unterordner im Home-Verzeichnis vor:<br/>
Zuerst ein Unterverzeichnis
„shot“ anlegen:</p>
<p><b>sudo mkdir shot </b>
</p>
<p>Jetzt noch die Rechte vergeben, damit jeder in dem Ordner
schreiben und lesen darf:</p>
<p><b>sudo chmod -R 777 shot</b></p>
<p>Vorzugsweise arbeite ich auf dem Raspi zum Programmieren mit
„Geany“. Zum Start das Programm auf dem Raspberry im Bereich
„Entwicklung“ öffnen und mit „Datei → Neu“ eine leere
Datei anlegen. Jetzt kann der Code von dieser WEB-Seite kopiert und
in die leere Datei eingefügt werden. Danach mit „Datei→
Speichern unter“ unter „<i>home/</i><span style="font-style: normal">pi/shot/“
mit dem Dateinamen „shot.py“</span> abspeichern. Eigentlich wars
das schon zur Software. Ausprobieren kann man das Programm über den
Pfeil in der Symbolleiste des „Geany“ oder direkt über das
Terminal mit der Befehlszeile:</p>
<p><b>sudo python /shot/shot.py</b></p>
<p>Damit das Programm nun auch beim Neustart automatisch losläuft,
muss es noch in die Start-Routine integriert werden:</p>
<p><b>sudo nano /etc/rc.local</b></p>
<p>ganz nach unten blättern und vor der Zeile „exit 0“ folgende
Zeile einfügen:</p>
<p><b>python /home/pi/shot/shot.py &amp;</b></p>
<p>Danach mit <b>CTRL+O</b> abspeichern und mit <b>CTRL+X</b>
beenden.</p>
<p>Nach einem Neustart mit:</p>
<p><b>sudo reboot</b></p>
<p>fährt der Raspi mit der Software automatisch hoch und ist ohne
weitere Eingaben bedienbar.</p>
<p><br/>
<br/>

</p>
<p><font size="4" style="font-size: 14pt"><b>4. Programmbeschreibung</b></font></p>
<p style="font-weight: normal"><font size="4" style="font-size: 14pt">Auch
wenn der Code auf den ersten Blick ein wenig verwirrend ausschaut,
folgt er doch einer klaren Struktur:</font></p>
<table width="100%" cellpadding="4" cellspacing="0" style="page-break-inside: avoid">
	<col width="85*"/>

	<col width="85*"/>

	<col width="85*"/>

	<tr valign="top">
		<td width="33%" style="background: transparent" style="border: none; padding: 0cm"><p>
			<br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><img src="README.md_html_5791cdbc8195d4f9.gif" name="Bild1" align="bottom" width="612" height="567" border="0"/>
</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
	<tr valign="top">
		<td width="33%" style="background: transparent" style="border: none; padding: 0cm"><p>
			<br/>

			</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>
<br/>

			</p>
			<p><font size="4" style="font-size: 14pt"><b>Funktionsblöcke im
			Code</b></font><img src="README.md_html_7b91292b68170727.jpg" name="Bild3" align="bottom" width="622" height="224" border="0"/>
</p>
		</td>
		<td width="33%" style="border: none; padding: 0cm"><p><br/>

			</p>
		</td>
	</tr>
</table>
<p><br/>
<br/>

</p>
<p>Bis zur Zeile 32 befinden sich nur Variablendefinitionen und
Vorbelegungen zur Initialisierung. Die Hauptroutine „main()“
befindet sich ab Zeile 105. Sie wird nach der Initialisierung
aufgerufen und hat nur die Funktion der Überprüfung der CSV-Datei
und danach Aufenthalt in einer Endlosschleife. Sobald ein
Signalwechsel durch den Taster erkannt wird (Interrupt), wird in
Zeile 100 gesprungen und definiert, wohin gesprungen werden muss: In
Zeile 45 „keypress()“. Hier laufen nun Aktionen des Status,
Uhrzeitabfrage und Ausgabe bzw. Steuerung der LEDs und Speicherung in
Datei ab. Eine weitere Unterroutine „get_timestamp()“ ab Zeile 35
liest lediglich die momentane Zeit aus. Dies wurde als eigenständige
Funktion abgetrennt, da der Vorgang mehrfach identisch aufgerufen
wird.<br/>
Die CSV-Datei wird im Unterordner <i>home/</i><span style="font-style: normal">pi/shot/
mit dem Dateiname „shot.csv“ gespeichert und kann über die
Standard Dateizugriffe des Raspberry entnommen werden. Ein Zugriff
über eine WEB-Seite ist in Vorbereitung und wird zeitnah hier
hinterlegt. </span>
</p>
<p>Ich habe versucht die Zeilen möglichst detailliert zeilenweise zu
dokumentieren. Bei Fragestellungen oder Unklarheiten bin ich jedoch
gerne behilflich. Änderungsvorschläge ausdrücklich willkommen!</p>
<p>harlfinger@gmx.de</p>
<p><br/>
<br/>

</p>
<p>  
</p>
<p><br/>
<br/>

</p>
<p><br/>
<br/>

</p>
<p><br/>
<br/>

</p>
</body>
</html>