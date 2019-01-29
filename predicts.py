import socket, json, random

def predicts():
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = "localhost"
  port = 9500
  serversocket.bind((host, port))
  serversocket.listen(5)
  (clientsocket, address) = serversocket.accept()

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  port = 9600
  s.connect((host,port))

  while 1:
    data = clientsocket.recv(1024).decode()
    if not data: break
    data_loaded = json.loads(data)
    data_loaded['predictedLat'] = random.randrange(-90*(1/0.000001), 90*(1/0.000001), 1)/(1/0.000001)
    data_loaded['predictedLng'] = random.randrange(-180*(1/0.000001), 180*(1/0.000001), 1)/(1/0.000001)
    if float(data_loaded['latitude']) > 31.4170436:
      data_loaded['passed'] = True
    else:
      data_loaded['passed'] = False      
    data_string = json.dumps(data_loaded)
    s.send(data_string.encode())

predicts()

