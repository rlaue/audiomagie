# Skills for magic tricks with Amazon's Alexa (in German language)

# Al Hexa - Zaubertricks für Alexa-Lautsprecher
Die Unterverzeichnisse dieses Repositorys beinhalten Skills, mit denen Zaubertricks mit dem Sprachassistenten *Alexa* von Amazon vorgeführt werden können. Hierfür ist ein eigenes Endgerät (Laptop / Smartphone) und ein Alexa-Lautsprecher, z. B. [Echo Dot 5](https://amzn.to/4fFtwGw), erforderlich.

Im Folgenden wird beschrieben, wie die Skills für die Vorführung genutzt werden können. Dafür ist ein eigenes Amazon-Developer-Konto erforderlich, da die Skills nicht öffentlich über den Amazon Skill Store angeboten werden.

Hinweise zur Vorführung finden sich in einer PDF-Datei innerhalb des jeweiligen Verzeichnisses.

## Einrichtung eines Developer-Kontos und Aufruf der Alexa-Developer-Konsole
- Falls man noch kein Developer-Konto bei Amazon hat, kann man sich eines unter <https://developer.amazon.com/de/> einrichten. Amazon-Kunden können die bestehenden Zugangsdaten nutzen, müssen aber trotzdem ein neues Konto als Entwickler einrichten.
- Jetzt wird die Developer-Konsole für Alexa unter <https://developer.amazon.com/alexa/console/ask> aufgerufen.

## Herunterladen der erforderlichen Dateien
- Jeder Unterordner in diesem Repository beinhaltet einen Zaubertrick. Zum Installieren sind zwei Dateien wichtig: das ZIP-Archiv sowie die Datei interactionModels/custom/de-DE. Beide müssen zunächst auf das lokale Gerät heruntergeladen werden, um dann später in der Alexa-Developer-Konsole zur Ausführung bei Amazon hochgeladen zu werden.

## Installieren eines Zaubertrick-Skills in der Developer-Konsole
- Klicken auf die blaue Schaltfläche "Skill erstellen"
- Unter "Name your Skill" wird ein Name angegeben. Das muss noch nicht der Name sein, unter dem der Skill dann später per Sprachsteuerung aufgerufen wird.
- Unter "Choose a primary locale" wird "German" angegeben, dann Klick auf die blaue Schaltfläche "Next" rechts oben
- Unter "Choose a type of experience" wird "Other" angegeben. Unter "Choose a model" wird "Custom" ausgewählt, darunter dann unter "Hosting services": "Alexa-hosted (Python)" und schließlich unter "Hosting region": "EU (Ireland)". Dann wieder ein Klick auf die blaue Schaltfläche "Next" rechts oben.
- Unter "Templates" wird ausgewählt: "Start vom Scratch", dann erneut auf "Next" klicken.
- Im nächsten Fenster wird auf "Create Skill" (rechts oben) geklickt und auf das Ende des Erstellvorgangs gewartet.
- Im Menü oben jetzt auf "Code" klicken, dann auf "Import Code" unterhalb dieses Menüs
- Jetzt wird das ZIP-Archiv angegeben, das zuvor aus dem Repository heruntergeladen wurde. Nach Klicken auf die Schaltfläche "Next" wird abgefragt, welche Dateien aus dem ZIP-Archiv importiert werden sollen. Hier wird einfach das oberste Kästchen markiert, wodurch alle im ZIP-Archiv enthaltenen Dateien ausgewählt werden. Danach auf "Next" und dann auf "Import" klicken und den Importvorgang abwarten. Anschließend auf die Schaltfläche "Deploy" (rechts oben) klicken und ds Ende des Deploy-Vorgangs abwarten.
- Jetzt wird oben im Menü "Build" angeklickt. In dem Menü auf der linken Seite 	öffnen wir "Interaction Model" und darunter "JSON Editor". Auf dem rechten Teil des Bildschirms gibt es jetzt eine Fläche mit der Aufschrift "Drag and drop a .json File". Dorthin wird die zuvor heruntergeladene Datei de-DE.json gezogen. Danach auf "Build Skill" (blaue Schaltfläche rechts oben) klicken.
- Schließlich kann noch der Name geändert werden, unter dem der Skill aufgerufen werden kann ("Alexa, starte Gedanken lesen"). Dazu wählt man im Menü links unter "Invocations" "Skill Invocation Name" und gibt den gewünschten Aufrufnamen in Kleinbuchstaben (!) ein. Nach einer Änderung muss man nochmals auf "Build Skill" klicken. An dieser Stelle wird einem gesagt, dass ein Aufrufname aus mindestens zwei Wörtern bestehen muss. Das kann man aber ruhig ignorieren, solange der Skill nur lokal betrieben wird.

## Testen
- Im Menü oben kann jetzt "Test" aufgerufen werden, dabei muss ggf. der Browser die Berechtigung zum Zugriff auf das Mikrofon bekommen.
- Zunächst steht hier jetzt noch "Test is disabled for this skill." Um das zu ändern, schaltet man von "Off" auf "Development".
- Jetzt kann man den neuen Skill starten. Es gibt zwei Möglichkeiten, mit „Alexa“ zu kommunizieren:
	- Man tippt in das Eingabefeld und schließt die Eingabe mit Enter ab. Wenn diese Art der Kommunikation funktioniert, ist das aber noch lange keine Garantie, dass Alexa das auch per gesprochener Sprache versteht. Es empfiehlt sich also unbedingt, auch per Spracheingabe zu testen:
	- Man klickt auf das Mikrofonsymbol am rechten Rand des Eingabefeldes, hält die Maustaste gedrückt (!) und spricht seine Eingabe in Mikrofon. Die Maustaste muss nach dem Ende des Sprechens noch eine kurze Zeit gedrückt bleiben, sonst wird die Spracheingabe abgeschnitten.
- Es muss unbedingt getestet werden, ob der gewählte Aufrufname (Skill Invocation Name) per Spracheingabe zuverlässig erkannt wird. Das ist häufig nicht der Fall, insbesondere wenn zusammengesetzte Substantive verwendet werden sollen. Bei dem für "Compucard" voreingestellten Aufrufnamen "Gedanken lesen" muss eine deutliche Sprechpause zwischen den beiden Worten eingelegt werden. Mit dem zusammengesetzten "Gedankenlesen" konnte Alexa in den Tests nicht gut umgehen.

## Koppeln an "Alexa"-Lautsprecher
- Auf einem Smartphone die [Alexa App](https://alexa.amazon.com/) installieren
- Dort auf das Plus-Zeichen und "Hinzufügen Gerät"
- Sprache auf Deutsch stellen
- Der Skill muss jetzt unbedingt noch einmal mit dem Lautsprecher getestet werden, da die Spracherkennung und zum Beispiel auch die Länge von Pausen anders sind als beim Test am PC. Das Kommando zum Starten ist: "Alexa, starte [Aufrufname]), mit dem im vorigen Schritt festgelegten Aufrufnamen.

# Lizenz, Verbesserungen und Rückmeldungen
Die Skills entstanden im Rahmen eines Projekts im Informatikstudium an der Westsächsischen Hochschule Zwickau. Alle von uns entwickelten Programmteile stehen unter einen offenen [Apache 2.0-Lizenz](LICENSE).

Vorschläge für Verbesserungen und weitere magische Alexa-Skills sowie Fragen sind willkommen an <Ralf.Laue@fh-zwickau.de>.



