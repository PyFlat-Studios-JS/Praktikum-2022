import json
import matplotlib.pyplot as plt
import numpy as np
def main():
    file = open("log.json", "r")
    x = file.read()
    data = json.loads(x)
    Logs = data["Log"]
    AmountSuccess = 0
    AmountTooMuchData = 0
    AmountTooLittleData = 0
    AmountInvalidPattern = 0
    AmountInvalidProcuctAmount = 0
    AmountTimeOut = 0
    AmountCriticalTimeout = 0
    for i in range (0, len(Logs)):
        if (Logs[i][0:8]=="Finished"):
            AmountSuccess += 1
        else:
            if (Logs[i][18:31] == "Too much Data"):
                AmountTooMuchData += 1
            elif (Logs[i][18:30] == "No Parts/IPs"):
                AmountTooLittleData += 1
            elif (Logs[i][18:27] == "Timed out"):
                AmountTimeOut += 1
            elif (Logs[i][18:32] == "Invalid Action"):
                AmountInvalidPattern += 1
            elif (Logs[i][18:40] == "Invalid Product Amount"):
                AmountInvalidProcuctAmount += 1
            else:
                AmountCriticalTimeout += 1
    x = [AmountSuccess, AmountTooMuchData, AmountTooLittleData, AmountInvalidPattern, AmountInvalidProcuctAmount, AmountTimeOut, AmountCriticalTimeout]
    labels = 'Finished ' + str(AmountSuccess), "Too much Data " +str(AmountTooMuchData), "No Parts/Ips " +str(AmountTooLittleData), "Invalid Action " + str(AmountInvalidPattern), "Invalid Products " + str(AmountInvalidProcuctAmount), "TimeOut " +str(AmountTimeOut), "Critical Timeout "+str(AmountCriticalTimeout)
    fig1, ax1 = plt.subplots()
    ax1.pie(x,labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


main()