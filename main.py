import json
from datetime import datetime
#Die Menge der Units / Ident Points muss ohne Rest durch die Länge der Patterns teilbar sein

#Daten
#Produktname
M_SYMBOL = "SEAT"
#Menge der Ident-Points
C_IdentPoints = 1
#Ident Points Simulieren?
S_IdentPoints = True
#Ident Point Pattern
P_IdentPoints = [1]
#Ident Points Id-Startwert
IP_id = 38462
#Ident Point Basis Name
IP_NameBase = "TestNode"
#M_CARR_QUANT
M_CARR_QUANT = 1
#Part Menge
C_Parts = 1
#Part Basis Name
Part_NameBase = "TestPart"
#Unit Type Pattern
P_UnitTypes = [1]
#Timestamp - Start format: datetime(year,month,day,hour,minute,second)
S_Timestamp = datetime.now()
#Timestamp - Intervall in s!!!
I_Timestamp = 10
#global Time: Zeit wird nicht für jede PU zurükgesetzt
globalTime = False


def setGlobals(a,b,c,d,e,f,g,h,i,j,k,l,m):
    global M_SYMBOL, C_IdentPoints, S_IdentPoints, P_IdentPoints, IP_id, IP_NameBase, M_CARR_QUANT, C_Parts, Part_NameBase, P_UnitTypes, S_Timestamp, I_Timestamp, globalTime
    M_SYMBOL = a
    C_IdentPoints = b
    S_IdentPoints = c
    P_IdentPoints = d
    IP_id = e
    IP_NameBase = f
    M_CARR_QUANT = g
    C_Parts = h
    Part_NameBase = i
    P_UnitTypes = j
    S_Timestamp = k
    I_Timestamp = l
    globalTime = m
def TEST_A():
    global M_SYMBOL, C_IdentPoints, S_IdentPoints, P_IdentPoints, IP_id, IP_NameBase, M_CARR_QUANT, C_Parts, Part_NameBase, P_UnitTypes, S_Timestamp, I_Timestamp, globalTime
    M_SYMBOL
    b = [10,100,1001,500, 2000, 0,1000,2000,2001,2000]
    h = [10,100,1101,2010, 501, 0,1000,500,400,501]
    e = ["Finished", "Finished", "Too much Rekursion", "Too much Rekursion","Too much Rekursion", "No Parts/IPs", "Finished","Finished","Too much Rekursion", "Too much Rekursion"]
    for i in range (0,10):
        setGlobals(M_SYMBOL, b[i], S_IdentPoints, P_IdentPoints, IP_id, IP_NameBase, M_CARR_QUANT, h[i], Part_NameBase, P_UnitTypes, S_Timestamp, I_Timestamp, globalTime)
        x = main()
        print("Exspected: " + e[i])
        print("Recieved:  " + x)
        if (x == e[i]):
            print("Test Passed")
        else:
            print("Test Failed")
def TEST_B():
    global M_SYMBOL, C_IdentPoints, S_IdentPoints, P_IdentPoints, IP_id, IP_NameBase, M_CARR_QUANT, C_Parts, Part_NameBase, P_UnitTypes, S_Timestamp, I_Timestamp, globalTime
    e = "Too much Rekursion"
    p = 0
    for i in range (1000,3000):
        if (i%100 == 0):
            print(i)
        setGlobals(M_SYMBOL, i, S_IdentPoints, P_IdentPoints, IP_id, IP_NameBase, M_CARR_QUANT, 1, Part_NameBase, P_UnitTypes, S_Timestamp, I_Timestamp, globalTime)
        x = main()
        if (x == e):
            p += 1
    print("Exspected: 1000")
    print("Recieved:  "+ str(p))
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
                if (ACTION_Pattern[i] == 1 or ACTION_Pattern[i] == 2 or ACTION_Pattern[i] == 3):
                    dummy = 4
                else:
                    return "Invalid Action at Part " + str(c) + " and IdentPoint " + str(i)
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
                if (ACTION_Pattern[e] == 1 or ACTION_Pattern[e] == 2 or ACTION_Pattern[e] == 3):
                    dummy = 8
                else:
                    return "Invalid Action at Part " + str(c) + " and IdentPoint " + str(i)
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
    
    #if (checkErrors(k) == "0"):
        #file = open("Data/result4.json", "w")
        #file.write(json.dumps(k))
    #else:
        #print(checkErrors(k))
def checkErrors(data):
    data
    n = type(["n","d"])
    if (type(data["IdentPointCreatingCommands"]) != n):
        print("WARNING " + data["IdentPointCreatingCommands"])
        return "Error in Ident Point creation"
    elif (type(data["ProductionUnitCreatingCommands"]) != n):
        print("WARNING " + data["ProductionUnitCreatingCommands"])
        return "Error in PU creation"
    elif (type(data["IdentPointSimulation"]) != n):
        print("WARNING " + data["IdentPointSimulation"])
        return "Error in IP Simulation"
    else:
        return "0"
def main():
    time_start = datetime.now()
    global IP_NameBase, IP_id, M_SYMBOL, Part_NameBase, P_UnitTypes, IP_NameBase, P_IdentPoints, M_CARR_QUANT, S_Timestamp, C_IdentPoints, I_Timestamp, C_Parts, globalTime, S_IdentPoints
    if ((C_IdentPoints > 1000) and (C_Parts > 1000)):
        return "Too much Rekursion"
    if (C_IdentPoints * C_Parts > 1000000):
        return "Too much Rekursion"
    if ((C_IdentPoints > 2000) or (C_Parts > 2000)):
        return "Too much Rekursion"
    if ((C_IdentPoints < 1) or (C_Parts < 1)):
        return "No Parts/IPs"
    a = createIdentPoints(IP_NameBase, IP_id)
    b = createProductionUnits(M_SYMBOL, Part_NameBase, P_UnitTypes)
    c = simulateIdentPoints(M_SYMBOL, Part_NameBase, IP_NameBase, P_IdentPoints, M_CARR_QUANT, S_Timestamp, C_IdentPoints, I_Timestamp, C_Parts, globalTime, S_IdentPoints)
    returnJSON(a,b,c)
    time_end = datetime.now()
    diff = time_end - time_start
    return "Finished"# + str(diff)
#print(main())
#TEST_A()
TEST_B()