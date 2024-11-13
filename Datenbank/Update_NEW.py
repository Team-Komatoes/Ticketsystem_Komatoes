import json

# JSON-Datei, die bereits existiert
dateiname = 'komatoes.json'

# Variablen für die Aktualisierung
table_name = "koma"  # Name der Tabelle, die aktualisiert werden soll
id_to_update = "7"    # ID des Eintrags, der aktualisiert werden soll
field_to_update = "Abteilung"  # Name der Spalte, die aktualisiert werden soll
new_value = None  # Neuer Wert, der eingetragen werden soll

def update_field_by_id(data, table_name, id_value, field_name, new_value):
    for table in data:
        if table['type'] == 'table' and table['name'] == table_name:  # Überprüfen, ob es sich um eine Tabelle handelt
            for entry in table['data']:
                if entry['ID'] == id_value:
                    entry[field_name] = new_value  # Neuen Wert zuweisen
                    break  # Beenden, nachdem der Eintrag aktualisiert wurde

# JSON-Datei lesen
with open(dateiname, 'r') as file:
    daten = json.load(file)

# Aktualisierung durchführen
update_field_by_id(daten, table_name, id_to_update, field_to_update, new_value)

# Änderungen speichern
with open(dateiname, 'w') as file:
    json.dump(daten, file, indent=4)

print(f"Die JSON-Datei wurde erfolgreich aktualisiert! '{field_to_update}' für ID '{id_to_update}' in der Tabelle '{table_name}' wurde auf '{new_value}' gesetzt.")