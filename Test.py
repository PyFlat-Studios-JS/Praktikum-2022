import json
from datetime import datetime
#Die Menge der Units / Ident Points muss ohne Rest durch die Länge der Patterns teilbar sein

#Daten
#Produktname
M_SYMBOL = "SEAT"
#Menge der Ident-Points
C_IdentPoints = 10
#Ident Points Simulieren?
S_IdentPoints = True
#Ident Point Pattern
P_IdentPoints = [1,3,3,3,2]
#Ident Points Id-Startwert
IP_id = 38462
#Ident Point Basis Name
IP_NameBase = "TestNode"
#M_CARR_QUANT
M_CARR_QUANT = 1
#Part Menge
C_Parts = 10
#Part Basis Name
Part_NameBase = "TestPart"
#Unit Type Pattern
P_UnitTypes = [1,2]
#Timestamp - Start
S_Timestamp = datetime(2018, 1, 1, 20,10,5)
print(S_Timestamp)
#Timestamp - Intervall
I_Timestamp = 0
def createIdentPoints(symbol,id_start):
    commands = []
    if (C_IdentPoints % (len(P_IdentPoints)) != 0):
        return "Invalid Pattern Length"
    for i in range (0,C_IdentPoints):
        commands.append(
            {
                "SYMBOL":(symbol + str(i)),
                "NODE":str(id_start+i)
            }
        )
    return commands
def createProductionUnits(M_Symbol, M_PU_IDENT, TypePattern):
    if (C_Parts % len(P_UnitTypes) != 0):
        return "Invalid Pattern Length"
    commands = []
    for i in range (0,C_Parts):
        if (i < len(TypePattern)):
            commands.append(
                {
                "M_SYMBOL":M_Symbol,
                "M_PU_IDENT":M_PU_IDENT + str(i),
                "M_UNIT_TYPE":str(TypePattern[i])
                }
            )
        else:
            e = i
            while(e > len(TypePattern)-1):
                e -= len(TypePattern)
            commands.append(
                {
                "M_SYMBOL":M_Symbol,
                "M_PU_IDENT":M_PU_IDENT + str(i),
                "M_UNIT_TYPE":str(TypePattern[e])
                }
            )
    return commands
def simulateIdentPoints(P_Symbol, PU_Symbol, IP_Symbol, ACTION_Pattern, M_CARR_QUANT, M_TIMESTAMP):
    print("hello")
def returnJSON(IdentPoints, Parts):
    k = {
        "IdentPointCreatingCommands":IdentPoints,
        "ProductionUnitCreatingCommands":Parts
    }
    print(json.dumps(k))
a = createIdentPoints(IP_NameBase, IP_id)
b = createProductionUnits(M_SYMBOL, Part_NameBase, P_UnitTypes)
returnJSON(a,b)