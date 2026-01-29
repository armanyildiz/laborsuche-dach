import folium
import json
from pathlib import Path


# Projekt-Root bestimmen
BASE_DIR = Path(__file__).resolve().parent.parent

# Pfad zur JSON-Datei
data_pfad_json = BASE_DIR / "data" / "labs_österreich.json"

# JSON-Datei einlesen
with open(data_pfad_json, 'r', encoding='utf-8') as f:
    daten = json.load(f)
    

#Karte initialisieren (Zentrum Österreich)
map_austria = folium.Map(location=[47.59397, 14.12456], zoom_start=7)

# Feature Groups für Filter
dexa_group = folium.FeatureGroup(name="DEXA Body Composition")
blut_group = folium.FeatureGroup(name="Blutlabor (Selbstzahler)")

# Marker hinzufügen
for data in daten:

    ##### Data-Infos aus dem JSON extrahieren #######
    ############################################

    lat = data["coordinates"]["lat"]
    lng = data["coordinates"]["lng"]

    name = data["name"]
    category = data["category"]
    city = data["address"]["city"]
    contact_tel= data["contact"]["phone"]
    contact_website=data["contact"]["website"]
    self_payer_info=data["self_payer"]
    price_info=data["price"]

    #############################################3##
    ################################################

    # Selbstzahler-Information aufbereiten
    # Wenn self_payer == True dann Objekt auf True setzen ansonsten auf Nein  
    if self_payer_info:
        self_payer='Ja'
    else:
        self_payer='Nein'

    # Preis-Information aufbereiten
    # Wenn der Preis null ist bedeutet 'nicht angegeben'
    if not price_info:
        price = 'nicht angegeben'
    else:
        price=price_info


    # Preis-Information aufbereiten
    # DEXA= blau, BLUTLABOR= rot
    if category == 'DEXA':
        color='blue'
    else:
        color='darkred'

    # Pop-Up Inhalt (HTML)
    popup_text = f"""
    <b>{name}</b><br>
    Kategorie: {category}<br>
    Stadt: {city}<br>
    Selbstzahler möglich?: {self_payer}<br>
    Preis: {price}<br>
    Tel: {contact_tel}<br>
    Website: <a href="{contact_website}" target="_blank">Zur Website</a>
    """

    # Breite des Pop-up Fensters anpassen
    popup = folium.Popup(popup_text, max_width=300)

    marker=folium.Marker(
        location=[lat, lng],
        popup=popup, 
        icon=folium.Icon(color=color, icon="info-sign"),
        tooltip=f"{name} ({category})"
    )

    # Marker der richtigen Gruppe hinzufügen
    if category == "DEXA":
        marker.add_to(dexa_group)
    else:
        marker.add_to(blut_group)

# die erstellten Featuregruppen der Karte hinzufügen        
dexa_group.add_to(map_austria)
blut_group.add_to(map_austria)

folium.LayerControl(collapsed=False).add_to(map_austria)

# Karte speichern
map_austria.save('interaktive_karte_österreich.html')

# Prüfen
print("Succesfull!")


