# Praktikum-2022
Automated generation of data used for testing

Konfigurierbare Erzeugung von den Nötigen Befehlen, um Testdaten zu erzeugen
Geplant: Automatische Ertzeigung der Daten
Probleme: 
- Jede Produktionseinheit muss jeden IdentPoint einmal durchlaufen. So ergeben sich Datenmengen nach dem Muster Partmenge * Punktmenge
  kann sehr groß werden
- Daten müssen noch manuell eingegeben werden

Parameter:
- M_SYMBOL (str) --> Name des Produkts, ein gültiger name muss vom Nutzer festgelegt werden
- C_IdentPoints (int) --> Menge der ScanIdent Points punkte 
- S_IdentPoints (boolean) --> gibt an, ob das durchlaufen Scanstellen simuliert werden soll oder nicht
- P_IdentPoints (int Array) --> Regelmäßige Folge von Aktionen eines Prdouktes an Ident Points -- C_IdentPoints muss ohne Rest durch die Länge von P_IdentPoints teilbar sein
- IP_id (int) --> Startwert für Ident Points (Id wird für jeden IP um 1 erhöht)
- IP_NameBase (str) --> Grundname, wird für jeden IP mit der Nummer des IP ergänzt: bsp.(TestPoint1, TestPoint2, TestPoint3, TestPoint4, ...)
- C_CARR_QUANT (int) --> Anzahl der Produkte, die auf einmal transportiert werden
- C_Parts (int) --> Anzahl der ProductionUnits
- Part_NameBase (str) --> Grundname, wird für jeden Part mit der Nummer des Parts ergänzt: bsp.(TestPart1, TestPart2, TestPart3, ...)
- P_UnitTypes (int Array) --> Einheitentypen - müssen vom Nutzer festgelegt werden - sonst gleiche Funktion wie P_IdentPoints
- S_TimeStamp (Timestamp) --> Zeitpunkt, bei dem das erste Produkt den ersten Scannpunkt durchläuft
- I_TimeStamp (int) --> Anzahl in Sekunden, um den die Zeit erhöht wird
- globalTime (boolean) --> False: die Zeit wird nach jedem Prdoukt auf den Startwert zurückgesetzt, True: die Zeit läuft nach jedem Produkt weiter
