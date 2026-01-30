# laborsuche-dach
Interaktive Karte mit Anbietern von DEXA-Body-Composition-Scan und selbst zu zahlenden Bluttests in der DACH-Region

![interaktive Karte Österreich](assets/karte_oesterreich.png)


## Projektübersicht
Dieses Projekt ist eine Webanwendung zur interaktiven Darstellung von Laboren und Praxen im DACH-Raum, speziell für **Österreich**, die folgende Untersuchungen anbieten:

- **DEXA Body Composition Scan** (Messung von Körperfettanteil, Muskelmasse und Knochendichte per Ganzkörper-Röntgen)
- **Blutuntersuchungstest als Selbstzahler** (ohne ärztliche Überweisung)

## Inhaltsverzeichnis

1. Features der Kartenansicht
2. Technologien 
3. Beispiel des Datenmodells (JSON)
4. Projektaufbau
5. Lokale Ausführung
    1. Voraussetzungen
    2. Installation
    3. Nutzung
6. Entscheidungen und Begründungen
    1. Daten beschaffen
    2. Interaktive Karte
    3. Datenstruktur
7. Mögliche Erweiterungen bei mehr Zeit

## 1. Features der Kartenansicht 
- Karte zentriert auf die gewählte Region
- Marker pro Standort, farblich unterschieden nach Kategorie
- Popup oder Sidebar mit Details beim Klick auf einen Marker
- Filtermöglichkeit (Alle / nur DEXA / nur Blutlabor)
- Responsive (Desktop + Mobil nutzbar)

## 2. Technologien
- **Programmiersprache**: Python - Version 3.11.5
- **Interaktive Karte**: Folium - Version 0.20.0
- **Datenformat**: Json

## 3. Beispiel des Datenmodells (JSON)

Jeder Labor-Standort wird folgendermaßen gespeichert:

```json

{
  "name": "Beispiel Labor Wien",
  "category": "Blutlabor",
  "services": ["Blutuntersuchung Selbstzahler"],
  "address": {
    "street": "Musterstraße 1",
    "postal_code": "6300",
    "city": "Wien",
    "country": "AUT"
  },
  "coordinates": {
    "lat": 52.3759,
    "lng": 9.7320
  },
  "contact": {
    "phone": "+43 511 123456",
    "website": "https://www.beispiel-labor.at"
  },
  "self_payer": true,
  "price": "ab 30 €",
  "source": "Website"
}

```

Dieses Datenmodell ist erweiterbar und kann problemlos um weitere Kategorien, Regionen
oder zusätzliche Felder (z. B. Öffnungszeiten) ergänzt werden.

### Hinweis zu Selbstzahler-Daten

- Für DXA Body Composition Scans wird das Feld `"self_payer"` standardmäßig auf `true` gesetzt. 
Grund: Diese Untersuchung wird in der Regel nicht von der gesetzlichen Krankenkasse übernommen und muss vom Kunden selbst bezahlt werden (als Wahlleistung oder Privatleistung). 
- Für Blutuntersuchungen wird das Feld `"self_payer"` abhängig von den Angaben der Praxis bzw. des Labors gesetzt.
- Falls Preise oder Selbstzahler-Details nicht öffentlich angegeben sind, werden diese Felder als null geführt.
- Anbieter werden als `"self_payer" = true` markiert, wenn Leistungen ohne ärztliche Überweisung privat in Anspruch genommen werden können.

## 4. Projektaufbau

Das Projekt laborsuche-dach ist übersichtlich strukturiert und besteht aus wenigen, klar getrennten Komponenten:

- Der Ordner `data` enthält die manuell recherchierten und verifizierten Standortdaten im JSON-Format.
In der Datei `labs_österreich.json` sind alle Labore und Praxen mit Adresse, Koordinaten, Leistungen und Selbstzahler-Informationen gespeichert.

- Der Ordner `src` beinhaltet das Python-Skript `main.py`.
Dieses Skript liest die JSON-Daten ein, verarbeitet sie und erzeugt daraus eine interaktive Karte mithilfe der Bibliothek **Folium**.

- `images`: Enthält Bilder, die in der Readme oder der interaktiven Karte verwendet werden.

- Die Datei `interaktive_karte_österreich.html` ist die generierte Ausgabe und befindet sich aktuell im Ordner `src`.
Sie stellt die interaktive Karte dar und kann direkt im Browser geöffnet werden (auch auf mobilen Geräten), ohne dass Python ausgeführt werden muss.

- Die Datei `README.md` beschreibt das Projekt, den Aufbau, die verwendeten Technologien sowie die Nutzung.

Bei der Ausführung von `main.py` wird die HTML-Karte automatisch aus den Daten im `data`-Ordner erstellt bzw. aktualisiert.

## 5. Lokale Ausführung

### 5.1 Voraussetzungen

- Python 3.9+
- pip
- Python-Bibliothek: `folium`


### 5.2 Installation


Ein Klonen des Repositories ist nicht zwingend erforderlich, da die Anwendung als statische HTML-Datei bereitgestellt wird.  
Das Repository kann über den [Repository-Link](https://github.com/armanyildiz/laborsuche-dach.git) als ZIP-Datei heruntergeladen werden.  
Falls das Repository dennoch geklont werden soll:

- Erstelle zunächst einen leeren Ordner, in dem das Projekt abgelegt werden soll
- Wechsle mit dem Befehl `cd pfad_zum_ordner` in diesen Ordner
- Klone anschließend das Repository mit:

```bash
git clone https://github.com/<dein-username>/laborsuche-dach.git
```

### 5.3 Nutzung

1. Stelle sicher dass Python installiert ist.
2. Installiere die benötigte Bibliothek:

```bash
python -m pip install folium

```
3. Wechsle in den `src`-Ordner und führe das Skript aus:

```bash
python main.py
```

4. Nach der Ausführung wird die Datei
`interaktive_karte_österreich.html` erstellt oder aktualisiert.

5. Öffne die HTML-Datei in einem beliebigen Browser (Desktop oder Mobilgerät)

## 6. Entscheidungen und Begründungen

### 6.1 Daten beschaffen

Bei der Datensammlung lag mein Fokus auf hoher Datenqualität statt auf möglichst vielen Einträgen. Da ich wenig Zeit hatte, mich intensiv mit Webscraping auseinanderzusetzen, habe ich die Daten manuell recherchiert. Die manuelle Suche reduziert potenzielle Fehler und stellt sicher, dass die erfassten Informationen korrekt und zuverlässig sind, auch wenn es etwas aufwändiger ist. Webscraping hätte zwar theoretisch mehr Daten liefern können, birgt aber die Gefahr, dass die gesammelten Daten unvollständig, fehlerhaft oder im falschen Format vorliegen, was eine aufwendige Bereinigung notwendig gemacht hätte.

Ich habe mich auf Österreich konzentriert, da die kleinere Region überschaubar ist und sich besser für eine qualitative Datensammlung eignet. Zur Effizienzsteigerung habe ich Google-Suchoperatoren genutzt, um relevante Webseiten gezielt zu finden:

- Für Anbieter von DXA Body Composition Scans:

```bash
((dexa OR dxa) AND (Bodyscan OR "Body Composition" OR Körperzusammensetzung)-Knochendichte) AND ("Selbstzahler" OR "Wahlleistung" OR "Privatpatient" OR "Privatleistungen" OR "ohne Kassenüberweisung" OR "ohne Krankenschein" OR "Selbstzahlung") site:.at
```
- Für Blutlabore (Selbstzahler):

```bash
(praxis OR labor) AND Blutuntersuchung AND ("Selbstzahler" OR "Wahlleistung" OR "Privatpatient" OR "Privatleistungen" OR "ohne Kassenüberweisung" OR "ohne Krankenschein" OR "Selbstzahlung") site:.at
```
Dadurch konnte ich auf eine schnelle Weise die gewünschte Webseiten zugreifen die die gewollte Infos enthalten könnten. Und die waren alle sehr relevant gewesen. 

### 6.2 Interaktive Karte

Für die Kartenerstellung habe ich Python verwendet, da ich damit Erfahrung habe und es mir ermöglicht, die Anwendung effizient umzusetzen. Als Bibliothek kam folium zum Einsatz, da sie speziell für die Erstellung interaktiver Karten entwickelt wurde und auf der populären leaflet.js-Bibliothek basiert. Dadurch ist die Karte sowohl desktop- als auch mobilfähig.

Die Bibliothek erlaubt es, Marker farblich nach Kategorie zu unterscheiden, Popups mit detaillierten Informationen einzufügen und Layer-Filter einzusetzen. Durch vorhandene Dokumentation und Community-Beiträge konnte ich mich schnell einarbeiten und die Funktionalitäten erfolgreich umsetzen.
Wichtige Referenzen, die mir bei der Umsetzung geholfen haben, waren unter anderem:


- [Folium Quickstart](https://python-visualization.github.io/folium/version-v0.11.0/quickstart.html)

- [Marken Farben auf Kaggle](https://www.kaggle.com/code/aungdev/colors-available-for-marker-icons-in-folium)

- [StackOverflow-Map Koordinaten](https://stackoverflow.com/questions/75172069/folium-initial-map-coordinates-location-not-working)

- [HTLM PopUp Syntax](https://www.w3schools.com/tags/ref_attributes.asp)

- [Layer Control Filterung](https://python-visualization.github.io/folium/latest/user_guide/ui_elements/layer_control.html)


### 6.3 Datenstruktur

Als Datenformat habe ich JSON gewählt, da es die Informationen übersichtlich, erweiterbar und leicht maschinenlesbar speichert.

- Die einzelnen Labore oder Praxen sind als Objekte (Dictionaries) strukturiert.

- Mehrere Standorte werden in einem Array abgelegt, was eine einfache Iteration in Python ermöglicht.

- JSON eignet sich besonders gut für zukünftige Erweiterungen oder Schnittstellen (API).

Ich finde JSON besonders geeignet, weil es flexibel und leicht verständlich ist, sowohl für die Verarbeitung im Code als auch für die Dokumentation der Daten. 

## 7. Mögliche Erweiterungen bei mehr Zeit

Wenn mehr Zeit zur Verfügung stünde, würde ich gerne Web Scraping ausprobieren, um die Datensammlung effizienter zu gestalten und in kürzerer Zeit eine größere Anzahl an Einträgen zu erfassen. Damit habe ich bisher keine praktische Erfahrung, möchte mich aber intensiv damit beschäftigen und meine Fähigkeiten in diesem Bereich erweitern.

Zudem plane ich, die visuelle Darstellung der Karte weiter zu verbessern:

- Hinzufügen einer Kartenüberschrift

- Eigene Icons gestalten oder alternative Marker verwenden

- Verschiedene Kartenstile ausprobieren, z. B. Stamen Terrain oder Mapbox Bright

Derzeit habe ich Popups zur Anzeige der Standortinformationen verwendet. Eine Sidebar wäre eine interessante Alternative, um die Nutzerinteraktion zu verbessern. Außerdem könnte ein Klick auf einen Standort die Karte weiter hineinzoomen und zusätzliche Bilder oder Informationen im Popup anzeigen, um die Orientierung zu erleichtern und den interaktiven Effekt zu verstärken.

Ich habe die Arbeit an der Karte sehr genossen und würde mich auch gerne den Bonusaufgaben widmen. Dabei konnte ich bereits viel Neues lernen und mich schnell in die Bibliothek und die Möglichkeiten der Umsetzung einarbeiten.

Für eine bessere Projektstruktur könnte ich zukünftig einen separaten Ordner, z. B. `Output`, für die generierten Dateien einrichten, um Übersichtlichkeit und Ordnung zu gewährleisten.



