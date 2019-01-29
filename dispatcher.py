import csv, socket, requests, json, os.path
import sqlite3, threading
from threading import Thread

dataSQL = []
committedResults = 0

def dispatcher():
  
  with sqlite3.connect('carStatus.db', check_same_thread=False, timeout = 10) as db_conn:
    db_conn.execute('''CREATE TABLE IF NOT EXISTS carstatus (
      id	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      vehicleSpeed	NUMERIC NOT NULL,
      vin	varchar ( 1000 ) NOT NULL,
      fuelLevelInput	REAL NOT NULL,
      acceleration	REAL NOT NULL,
      longitude	REAL NOT NULL,
      latitude	REAL NOT NULL,
      timestamp	NUMERIC NOT NULL,
      predictedLat	REAL NOT NULL,
      predictedLng	REAL NOT NULL,
      eventID	smallint NOT NULL)''')
  

  def sendRequest(data_loaded, data):
    # r = requests.post("http://localhost:8000/api/data/cars/", data)
    # print(r.json())
    vin = {}
    vin[str(data['vin'])] = 1
    requests.patch("https://testing-894c8.firebaseio.com/Status/" + data['vin'] + "/" + str(data['timestamp']) + ".json", data_loaded)
    r = requests.patch("https://testing-894c8.firebaseio.com/Vin.json", json.dumps(vin))

  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = "localhost"
  port = 9600
  serversocket.bind((host, port))
  serversocket.listen(5)
  (clientsocket, address) = serversocket.accept()

  file_exists = os.path.isfile('database.csv')
  

  while 1:
    data = clientsocket.recv(1024).decode()
    if not data: break
    dataJs = json.loads(data)
    process = Thread(target=sendRequest, args=[data, dataJs])
    process.start()
    dataSQL.append(dataJs)
  
  with sqlite3.connect('carStatus.db', check_same_thread=False, timeout = 10) as db_conn:
    for i in range(committedResults, len(dataSQL)):
      t = (dataSQL[i]['vehicleSpeed'],dataSQL[i]['vin'],dataSQL[i]['fuelLevelInput'],dataSQL[i]['acceleration'],dataSQL[i]['longitude'],dataSQL[i]['latitude'],dataSQL[i]['timestamp'],dataSQL[i]['predictedLat'],dataSQL[i]['predictedLng'],dataSQL[i]['eventID'])
      db_conn.execute('INSERT INTO carstatus (vehicleSpeed,vin,fuelLevelInput,acceleration,longitude,latitude,timestamp,predictedLat,predictedLng,eventID) VALUES (?,?,?,?,?,?,?,?,?,?);', t)
      committedResults = committedResults + 1
    db_conn.commit()
  conn.close()


def timerSQL(sec):
  def func_wrapper():
    global committedResults
    global dataSQL
    timerSQL(sec)
    with sqlite3.connect('carStatus.db', check_same_thread=False, timeout = 10) as db_conn:
      for i in range(committedResults, len(dataSQL)):
        t = (dataSQL[i]['vehicleSpeed'],dataSQL[i]['vin'],dataSQL[i]['fuelLevelInput'],dataSQL[i]['acceleration'],dataSQL[i]['longitude'],dataSQL[i]['latitude'],dataSQL[i]['timestamp'],dataSQL[i]['predictedLat'],dataSQL[i]['predictedLng'],dataSQL[i]['eventID'])
        db_conn.execute('INSERT INTO carstatus (vehicleSpeed,vin,fuelLevelInput,acceleration,longitude,latitude,timestamp,predictedLat,predictedLng,eventID) VALUES (?,?,?,?,?,?,?,?,?,?);', t)
        committedResults = committedResults + 1
      db_conn.commit()
  t = threading.Timer(sec, func_wrapper)
  t.start()
  return t

Thread(target=dispatcher, args=[]).start()
Thread(target=timerSQL, args=[5]).start()
