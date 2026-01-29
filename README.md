# laborsuche-dach
Interaktive Karte mit Anbietern von DEXA-Body-Composition-Scan und selbst zu zahlenden Bluttests in der DACH-Region

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
    5.1 Voraussetzungen
    5.2 Installation
    5.3 Nutzung

## 1. Features der Kartenansicht 
- Karte zentriert auf die gewählte Region
- Marker pro Standort, farblich unterschieden nach Kategorie
- Popup oder Sidebar mit Details beim Klick auf einen Marker
- Filtermöglichkeit (Alle / nur DEXA / nur Blutlabor)
- Responsive (Desktop + Mobil nutzbar)

## 2. Technologien
- **Programmiersprache**: Python: Version 3.11.5
- **Interaktive Karte**: Folium: Version 0.20.0
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

- Die Datei `interaktive_karte_österreich.html` ist die generierte Ausgabe.
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
pip install folium
```
3. Wechsle in den `src`-Ordner und führe das Skript aus:

```bash
python main.py
```

4. Nach der Ausführung wird die Datei
`interaktive_karte_österreich.html` erstellt oder aktualisiert.

5. Öffne die HTML-Datei in einem beliebigen Browser (Desktop oder Mobilgerät)





