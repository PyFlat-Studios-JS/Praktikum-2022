import json
from datetime import datetime
#Die Menge der Units / Ident Points muss ohne Rest durch die Länge der Patterns teilbar sein

#Daten
#Produktname
M_SYMBOL = "SEAT"
#Menge der Ident-Points
C_IdentPoints = 4
#Ident Points Simulieren?
S_IdentPoints = True
#Ident Point Pattern
P_IdentPoints = [1,3,3,2]
#Ident Points Id-Startwert
IP_id = 38462
#Ident Point Basis Name
IP_NameBase = "TestNode"
#M_CARR_QUANT
M_CARR_QUANT = 1
#Part Menge
C_Parts = 4
#Part Basis Name
Part_NameBase = "TestPart"
#Unit Type Pattern
P_UnitTypes = [1,2]
#Timestamp - Start
S_Timestamp = datetime.now()
#Timestamp - Intervall in s!!!
I_Timestamp = 10
#global Time: Zeit wird nicht für jede PU zurükgesetzt
globalTime = False
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
def simulateIdentPoints(P_Symbol, PU_Symbol, IP_Symbol, ACTION_Pattern, M_CARR_QUANT, M_TIMESTAMP, C_IdentPoints, I_TIMESTAMP, C_Parts, globalTime, S_IdentPoints):
    if (C_IdentPoints % len(ACTION_Pattern) != 0):
        return "Invalid Pattern length"
    if (M_CARR_QUANT <= 0):
        return "Invalid Product Amount"
    if (S_IdentPoints == False):
        return "Ident-Point simulation not active"
    commands = []
    time = M_TIMESTAMP
    for c in range (0, C_Parts):
        if (globalTime != True):
            time = M_TIMESTAMP
        for i in range (0, C_IdentPoints):
            m = time.timestamp()
            m = m + I_TIMESTAMP
            time = datetime.fromtimestamp(m)
            if (i < len(ACTION_Pattern)):
                commands.append(
                {
                "M_SYMBOL": P_Symbol,
                "M_PU_IDENT": PU_Symbol + str(c),
                "M_IDENTPOINT_Symbol": IP_Symbol + str(i),
                "M_ACTION": ACTION_Pattern[i],
                "M_CARR_QUANT": M_CARR_QUANT,
                "M_TIMESTAMP": str(time)
                }
                )
            else:
                e = i
                while (e>len(ACTION_Pattern)-1):
                    e -= len(ACTION_Pattern)
                commands.append(
                    {
                    "M_SYMBOL": P_Symbol,
                    "M_PU_IDENT": PU_Symbol + str(c),
                    "M_IDENTPOINT_Symbol": IP_Symbol + str(i),
                    "M_ACTION": ACTION_Pattern[e],
                    "M_CARR_QUANT": M_CARR_QUANT,
                    "M_TIMESTAMP": str(time)
                    }
                )
    return commands
def returnJSON(IdentPoints, Parts, Simulation):
    k = {
        "IdentPointCreatingCommands":IdentPoints,
        "ProductionUnitCreatingCommands":Parts,
        "IdentPointSimulation": Simulation
    }
    file = open("result.json", "w")
    file.write(json.dumps(k))
    
a = createIdentPoints(IP_NameBase, IP_id)
b = createProductionUnits(M_SYMBOL, Part_NameBase, P_UnitTypes)
c = simulateIdentPoints(M_SYMBOL, Part_NameBase, IP_NameBase, P_IdentPoints, M_CARR_QUANT, S_Timestamp, C_IdentPoints, I_Timestamp, C_Parts, globalTime, S_IdentPoints)
returnJSON(a,b,c)
