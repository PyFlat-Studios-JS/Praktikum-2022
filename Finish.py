import json

def main():
    file = open("Data/result4.json", "r")
    jsData = file.read()
    pyData = json.loads(jsData)
    a = pyData["IdentPointCreatingCommands"]
    b = pyData["ProductionUnitCreatingCommands"]
    c = pyData["IdentPointSimulation"]
    for i in range (0, len(a)):
        r = json.dumps(a[i])
        #Load Command goes here
    for i in range (0, len(b)):
        r = json.dumps(b[i])
        #Load Command goes here
    for i in range (0, len(c)):
        r = json.dumps(c[i])
        #Load Command goes here
main()