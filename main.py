#import ray
import socket


"""ray.init() # необязательно

@ray.remote # объявление, что функция выполняется удаленно
def square(x):
    return x * x"""

#делаем сервер
sock = socket.socket() # создание сокета
sock.bind(('', 9090)) # с помощью метода bind связываем сокет
# с хостом (оставим строку пустой, чтобы наш сервер был доступен для всех интерфейсов)
# и портом (от 0 до 65535, но обычно для прослушивания 0-1023 особые привелегии)
sock.listen(1) # прослушивание, в скобках - макс. кол-во подключений в очереди
conn, addr = sock.accept() # принятие подключения

while True:
    data = conn.recv(1024) # получение данных, в скобках кол-во байт для чтения
    if not data:
        break
    conn.send(data.upper())

conn.close() # закрываем соединение
# сервер готов
# клиент

sock = socket.socket()
sock.connect(('localhost', 9090)) # подключение к серверу
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print (data)

"""futures = [square.remote(i) for i in range(4)] # все функции вызываются через .remote, а не как обычно

print(ray.get(futures)) # получение результата с помощью ray.get
"""