import socket
import threading 

host = "172.20.23.182" #localhost
port = 8080

#Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()


clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)



def handle(client): 
    while True: 
        try: 
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nicknames = nicknames[index]
            broadcast(f"{nickname} left the chat! ".encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept() #accept clints
        print(f'Connected With {str(address)}')
        
        client.send('NICK'.encode('ascii')) #send client a code name of nick to set nickname
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname) # append nickname to the list
        clients.append(client)  # append client to the list

        print(f'Nickname of the clinet is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))


        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening....")
receive()
