from datetime import datetime
import json
file = open("Data/result4.json","r")
j = file.read()
data = json.loads(j)
def checkErrors():
    global data
    n = [2,3]
    if (type(data["IdentPointCreatingCommands"]) != type(n)):
        print("Error")
    else:
        print("Ok")
checkErrors()