import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
s.bind(("127.0.0.1", 9090))
print("Socket bound")
s.listen()
print("Socket listening")
print()
clients = []


def brodcast(message):
    print(message)
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


def receive():
    while True:
        client, address = s.accept()
        print("Connected with {}".format(str(address)))
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
