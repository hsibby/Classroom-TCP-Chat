import socket
import threading 

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.20.23.182',8080))#Change IP


def receive():
    while True: 
        try: 
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else: 
                print(message)

        except:
            print("An error occured")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()


write_thread = threading.Thread(target=write)
write_thread.start()
