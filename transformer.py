import socket, json, time
from threading import Thread

def transformer():
  host = "localhost"
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  port = 8500
  serversocket.bind((host, port))
  serversocket.listen(5)

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  port = 9500
  s.connect((host,port))

  def carClient(clientsocket):
    while 1:
      data = clientsocket.recv(1024).decode()
      if not data: break
      data_loaded = json.loads(data)
      data_loaded["timestamp"] = int(time.time() * 1000000)
      data_loaded["vin"] = data_loaded['vin'].upper()
      data_string = json.dumps(data_loaded)
      s.send(data_string.encode()) 

  while 1:
    (clientsocket, address) = serversocket.accept()
    process = Thread(target=carClient, args=[clientsocket])
    process.start()

transformer()