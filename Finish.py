import json
import webbrowser
import requests
def main():
    file = open("Data/result4.json", "r")
    jsData = file.read()
    pyData = json.loads(jsData)
    a = pyData["IdentPointCreatingCommands"]
    b = pyData["ProductionUnitCreatingCommands"]
    c = pyData["IdentPointSimulation"]
    for i in range (0, len(a)):
        r = json.dumps(a[i])
        print(r)
    for i in range (0, len(b)):
        r = json.dumps(b[i])
        print(r)
    for i in range (0, len(c)):
        r = json.dumps(c[i])
        print(r)
#main()
webbrowser.open("https://gefasoft.de")
x = requests.get("https://gefasoft.de")
print(x.text)