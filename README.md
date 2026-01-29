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

## 1. Features der Kartenansicht 
- Karte zentriert auf die gewählte Region
- Marker pro Standort, farblich unterschieden nach Kategorie
- Popup oder Sidebar mit Details beim Klick auf einen Marker
- Filtermöglichkeit (Alle / nur DEXA / nur Blutlabor)
- Responsive (Desktop + Mobil nutzbar)

## 2. Technologien
- **Programmiersprache**: Python
- **Interaktive Karte**: Folium
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





