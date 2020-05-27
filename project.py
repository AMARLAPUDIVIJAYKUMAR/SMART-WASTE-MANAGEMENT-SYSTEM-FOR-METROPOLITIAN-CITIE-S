import requests
import time
import sys
import ibmiotf.application
import ibmiotf.device
import random



def dustbin(Rangea,Rangeb,Rangec,Ranged,longa,lata,longb,latb,longc,latc,longd,latd):
    #Provide your IBM Watson Device Credentials
    organization = "dr398o"
    deviceType = "dustbin"
    deviceId = "123456"
    authMethod = "token"
    authToken = "9381864282"

    # Initialize GPIO

    def myCommandCallback(cmd):
            print("Command received: %s" % cmd.data)
        

    try:
            deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
            deviceCli = ibmiotf.device.Client(deviceOptions)
            #..............................................
	
    except Exception as e:
        print("Caught exception connecting device: %s" % str(e))
        sys.exit()

    # Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
    deviceCli.connect()

    
        
    #hum=random.randint(10,50)
    #print(hum)
    #temp = random.randint(10,80)
    #Send Temperature & Humidity to IBM Watson
    data = { 'rangea':Rangea,'longa':longa,'lata':lata,'rangeb':Rangeb,'longb':longb,'latb':latb,'rangec':Rangec,'longc':longc,'latc':latc,'ranged':Ranged,'longd':longd,'latd':latd }
    #print (data)
    def myOnPublishCallback():
        print ("Published siccessfully")

    success = deviceCli.publishEvent("DHT11", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(2)
        
    deviceCli.commandCallback = myCommandCallback

    # Disconnect the device and application from the cloud
    deviceCli.disconnect()



def message(r,lo,l):
    r=r
    lo=lo
    l=l
    for i in range(len(r)):
        t=r[i]
        if t>=90:
            x=requests.get(f'https://www.fast2sms.com/dev/bulk?authorization=djP1xTyHp0v7fB6ADm32ut4ZbqRSUg8FwMECnJXkGhLIOeWso5TZGwdyC9c1hLle6uaxptAbnQ5qokig&sender_id=FSTSMS&message=dustbin%20at%20longitude:{lo[i]}%20and%20latitude{l[i]}%20is%20full%20and%20is%20filled%20upto%20{r[i]}percent&language=english&route=p&numbers=9381864282,9398619482,9494468005')
            print(x.status_code)

Rangea=97
#Rangea=random.randint(0,100)
longa="5.54"
lata="6.75"
Rangeb=random.randint(0,100)
longb="10.58"
latb="9.55"
Rangec=random.randint(0,100)
longc="120.36"
latc="55.56"
Ranged=random.randint(0,100)
longd="78.99"
latd="44.22"
r=[Rangea,Rangeb,Rangec,Ranged]
lo=[longa,longb,longc,longd]
l=[lata,latb,latc,latd]
message(r,lo,l)
print(r)
dustbin(Rangea,Rangeb,Rangec,Ranged,longa,lata,longb,latb,longc,latc,longd,latd)
