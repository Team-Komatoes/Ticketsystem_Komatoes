CREATE TABLE IF NOT EXISTS abteilungen (
ID INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
Abteilung VARCHAR(255)
);

INSERT INTO abteilungen (ID, Abteilung) VALUES ('1', 'Buchhaltung');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('2', 'Chefarzt_Buero');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('3', 'Chirurgie');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('4', 'Facility_Management');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('5', 'Intensivstation');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('6', 'Kinderstation');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('7', 'Krebsstation');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('8', 'Kreissaal');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('9', 'Kueche');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('10', 'Lager');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('11', 'Neugeborenenstation');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('12', 'OP');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('13', 'Pneumologie');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('14', 'Psychatrie');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('15', 'Radiologie');
INSERT INTO abteilungen (ID, Abteilung) VALUES ('16', 'ZNA');

CREATE TABLE IF NOT EXISTS fehler (
ID INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
Fehler VARCHAR(255)
);

INSERT INTO fehler (ID, Fehler) VALUES ('1', 'Defekte_Geraete');
INSERT INTO fehler (ID, Fehler) VALUES ('2', 'Internet');
INSERT INTO fehler (ID, Fehler) VALUES ('3', 'Klimaanlage');
INSERT INTO fehler (ID, Fehler) VALUES ('4', 'Lagerbestaende');
INSERT INTO fehler (ID, Fehler) VALUES ('5', 'Medikamente');
INSERT INTO fehler (ID, Fehler) VALUES ('6', 'Pager');
INSERT INTO fehler (ID, Fehler) VALUES ('7', 'Pc_Tablet_Probleme');
INSERT INTO fehler (ID, Fehler) VALUES ('8', 'Server');
INSERT INTO fehler (ID, Fehler) VALUES ('9', 'Telefon_Kommunikation');
INSERT INTO fehler (ID, Fehler) VALUES ('10', 'TV_Probleme');

CREATE TABLE IF NOT EXISTS prioritaet (
ID INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
Fehler VARCHAR(255),
Prio VARCHAR(255)
);

INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('1', 'Defekte_Geraete', 'Hoch');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('2', 'Internet', 'Hoch');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('3', 'Klimaanlage', 'Hoch');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('4', 'Lagerbestaende', 'Hoch');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('5', 'Medikamente', 'Mittel');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('6', 'Pager', 'Mittel');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('7', 'Pc_Tablet_Probleme', 'Mittel');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('8', 'Server', 'Gering');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('9', 'Telefon_Kommunikation', 'Gering');
INSERT INTO prioritaet (ID, Fehler, Prio) VALUES ('10', 'TV_Probleme', 'Gering');

CREATE TABLE IF NOT EXISTS Status (
ID INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
Status VARCHAR(255)
);

INSERT INTO Status (ID, Status) VALUES ('1', 'offen');
INSERT INTO Status (ID, Status) VALUES ('2', 'geschlossen');
INSERT INTO Status (ID, Status) VALUES ('3', 'in Bearbeitung');

CREATE TABLE IF NOT EXISTS koma (
ID INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
Mitarbeiter VARCHAR(255),
Abteilung VARCHAR(255),
Fehler VARCHAR(255),
Ticket VARCHAR(255),
Uhrzeit datetime NOT NULL DEFAULT current_timestamp(),
Prio VARCHAR(255)
);

