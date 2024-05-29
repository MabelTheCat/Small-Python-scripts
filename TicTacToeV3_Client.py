import socket

def setupClient(): #TODO: Add GUI code. Sets up the client.
    global client

    #Client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectClient(serverIp, serverPort, data="NullName!"): #TODO: Add GUI code. Tries to connect to a server.
    global client
    try:
        client.connect((serverIp, serverPort))
        #TODO: Add GUI code for sucessful connection here
        pass

    #Connection failed
    except ConnectionRefusedError:
        #TODO: Add code for failed connection here
        print("Connection failed. Trying again...")
        return False
    
    print("Connection to server succeeded.")
    #Send player data
    client.send(data.encode("utf-8"))

    try:
        accept = client.recv(2**8).decode() == "AcceptedJoinRequest"
    except ConnectionResetError:
        print("Server crashed.")
        return False
    
    if accept:
        #Add code and for sucessful connection here
        print("Connection to game allowed")

        #Message from server
        inputData = client.recv(2**8).decode("utf-8")
    
    else:
        #Add code for failed connection code here
        print("Connection to game refused.")
        client.close()

    return True

if __name__ == "__main__":
    data = input("Enter you name and symbol, without any spaces. Ex: (Owen,O)\n->\t")
    data = f"{data[:-2]}{data[-1]}"
    serverIp = input("Enter server IP:\t")
    serverPort = int(input("Enter server port:\t"))
    setupClient()
    while not connectClient(serverIp=serverIp, serverPort=serverPort, data=data):
        None