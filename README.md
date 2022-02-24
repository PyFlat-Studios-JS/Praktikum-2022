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
- P_IdentPoints (int Array) --> Regelmäßige Folge von Aktionen eines Prdouktes an Ident Points -- C_IdentPoints muss ohne Rest durch die Länge von P_IdentPoints teilbar sein
- IP_id (int) --> Startwert für Ident Points (Id wird für jeden IP um 1 erhöht)
- IP_NameBase (str) --> Grundname, wird für jeden IP mit der Nummer des IP ergänzt: bsp.(TestPoint1, TestPoint2, TestPoint3, TestPoint4, ...)
- C_CARR_QUANT (int) --> Anzahl der Produkte, die auf einmal transportiert werden (Hat keine Auswirkungen auf das Programm, der Parameter wird 1:1 übergeben)
- C_Parts (int) --> Anzahl der ProductionUnits
- Part_NameBase (str) --> Grundname, wird für jeden Part mit der Nummer des Parts ergänzt: bsp.(TestPart1, TestPart2, TestPart3, ...)
- P_UnitTypes (int Array) --> Einheitentypen - müssen vom Nutzer festgelegt werden - sonst gleiche Funktion wie P_IdentPoints
- S_TimeStamp (Timestamp) --> Zeitpunkt, bei dem das erste Produkt den ersten Scannpunkt durchläuft
- I_TimeStamp (int) --> Anzahl in Sekunden, um den die Zeit erhöht wird
- globalTime (boolean) --> False: die Zeit wird nach jedem Prdoukt auf den Startwert zurückgesetzt, True: die Zeit läuft nach jedem Produkt weiter
- DoTimeOuts (boolean) --> Gibt an, ob Timeouts überprüft werden sollen -- Sehr zu empfehlen, um zu lange Laufzeiten zu vermeiden. Die Begrenzung C_Parts * C_Identpoints < 1000000) besteht weiterhin.
- LimitTimeOut (int) --> Zeit in Sekunden nach der ein Timeout durchgeführt werden soll. (~Maximale Laufzeit: <3min; Erzwungender Timeout: 5min;Normale Laufzeiten <30sek)
Mögliche Rückmeldungen:
- Finished after <Time> ==> Wird ausgegeben, wenn der PRozess erfolgreich war. In diesem Fall wird das Json gespeichert
- Too much Data ==> Wird ausgegeben, wenn C_Parts * C_Identpoints > 1000000 ist, um zu lange Rechenzeit oder Dateigröße zu vermeiden
- No Parts/IPs ==> Wird ausgegeben, wenn C_Parts oder C_Identpoints <= 0 ist.
- Timed out ==> Wird ausgegeben, wenn die Prozesszeit > LimitTimeOut ist
- Critical Timeout ==> Wird nach 5 min Prozessdauer ausgegeben und Taucht nur auf, wenn LimitTimeOut > 300 oder DoTimeOuts = False gesetzt ist. Sollte aber nie auftauchen, es sei denn, die Too much Data-Grenze wird über 1000000 erhöht. Die Normale Prozessdauer bei maximaler Länge beträgt 2-3 min
- Invalid Pattern length ==> Wird ausgegeben, wenn C_Parts oder C_IdentPoints nicht ohne Rest durch P_UnitTypes bzw. P_IdentPoints teilbar ist #TODO: Ausschaltbar machen
- Invalid Product Amount ==> Wird ausgegeben, wenn M_CARR_QUANT <= 0 ist.
