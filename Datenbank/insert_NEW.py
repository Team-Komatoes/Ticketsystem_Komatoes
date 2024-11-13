import json

# JSON-Datei, die bereits existiert
dateiname = './Datenbank/komatoes.json'

# Variablen für den neuen Eintrag
table_name = "koma"  # Name der Tabelle, in die der Eintrag hinzugefügt werden soll
neuer_eintrag = {
    "ID": "",  # ID des neuen Eintrags
    "Mitarbeiter": "",  # Name des Mitarbeiters
    "Abteilung": "",  # Abteilung (kann leer sein)
    "Fehler": "",  # Fehler (kann leer sein)
    "Ticket": "",  # Ticket (kann leer sein)
    "Uhrzeit": "",  # Uhrzeit (kann leer sein)
    "Prio": ""      # Priorität
}

# JSON-Datei lesen
with open(dateiname, 'r') as file:
    daten = json.load(file)

# Neuen Eintrag zur angegebenen Tabelle hinzufügen
def add_entry_to_table(data, table_name, new_entry):
    for table in data:
        if table['type'] == 'table' and table['name'] == table_name:
            table['data'].append(new_entry)  # Neuen Eintrag hinzufügen
            break  # Beenden, nachdem der Eintrag hinzugefügt wurde

# Eintrag hinzufügen
add_entry_to_table(daten, table_name, neuer_eintrag)

# Änderungen speichern
with open(dateiname, 'w') as file:
    json.dump(daten, file, indent=4)

print(f"Die JSON-Datei wurde erfolgreich aktualisiert! Neuer Eintrag in der Tabelle '{table_name}' hinzugefügt.")