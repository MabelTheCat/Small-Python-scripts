import socket
import threading

print("THIS IS THE SERVER! DO NOT CLOSE!")
#Server code
def setupServer():
    "Sets up a server"
    #Data
    global server
    server_ip, server_port = "127.0.0.1", int(input("Enter port to use:\t"))

    #Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))

def manageGameLobby(playerAmount):
    "Manages the join requests"
    global clients, playerNames, playerSymbols
    clients = []
    playerNames = []
    playerSymbols = []

    #Code for game lobby
    while len(clients) < playerAmount:
        print("Waiting for connection...")
        server.listen(0)
        client, address = server.accept()

        data = client.recv(2**8).decode("utf-8")
        playerName, playerSymbol = data[:-1], data[-1]

        clientAccepted = True if input(f"Accept {playerName} ({playerSymbol})?\t").strip().lower() == "yes" else False

        #Player was accepted
        if clientAccepted:
            try:
                client.send("AcceptedJoinRequest".encode("utf-8"))
                print(f"Player {playerName} joined the game.")
                clients.append(client)
                playerNames.append(playerName)
                playerSymbols.append(playerSymbol)

            except ConnectionResetError:
                print(f"Player {playerName} lost their connection.")
            
        else:
            try:
                client.send("RefusedJoinRequest".encode("utf-8"))
                print(f"Player {playerName} was denied entry to the game.")
            except ConnectionResetError:
                print(f"Player {playerName} lost their connection.")
    
    #Code for when the game is running
    print(f"Game started. Players are ", end="")
    for i in range(len(playerNames)):
        print(f"{playerNames[i]} ({playerSymbols[i]})", end=", ")
    print()

if __name__ == "__main__":
    setupServer()
    manageGameLobby(3)