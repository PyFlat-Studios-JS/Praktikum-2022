import json
import requests
import base64
def main():
    #Username
    usr = "js"
    #Password
    pas = "js"
    usr_pas = usr + ":" + pas
    up_bytes = usr_pas.encode('ascii')
    b64_bytes = base64.b64encode(up_bytes)
    b64_up = b64_bytes.decode('ascii')
    
    file = open("Data/result4.json", "r")
    jsData = file.read()
    pyData = json.loads(jsData)
    a = pyData["IdentPointCreatingCommands"]
    b = pyData["ProductionUnitCreatingCommands"]
    c = pyData["IdentPointSimulation"]
    from requests.structures import CaseInsensitiveDict
    Headers = CaseInsensitiveDict()
    Headers["Authorization"] = "Basic " + b64_up
    Headers["Content-Type"] = "application/json"
    for i in range (0, len(a)):
        f = {
            "jsonrpc": "2.0",
            "id": (i+37937),
            "method": "/de/gefasoft/sapient/db/pus/IdentPoint/create",
            "params": a[i]
            }
        r = json.dumps(f)
        x = requests.post("http://172.31.37.10:9010/call", headers=Headers, data=r)
        if (x.status_code == 401):
            print("Incorrect Username or Password")
            return 0
        else:
            print(x.text)
    for i in range (0, len(b)):
        f = {
            "jsonrpc": "2.0",
            "id": (i+37037),
            "method": "/de/gefasoft/sapient/db/pus/ProductionUnit/create",
            "params": b[i]
            }
        r = json.dumps(f)
        x = requests.post("http://172.31.37.10:9010/call", headers=Headers, data=r)
        print(x.text)
    for i in range (0, len(c)):
        f = {
            "jsonrpc": "2.0",
            "id": (i+31937),
            "method": "/de/gefasoft/sapient/db/pus/ProductionUnit/ident",
            "params": c[i]
            }
        r = json.dumps(f)
        x = requests.post("http://172.31.37.10:9010/call",headers=Headers, data=r)
        print(x.text)
main()