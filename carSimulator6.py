import csv, time, socket, json

def carSimulator3():  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = "localhost"
  port = 8500
  s.connect((host,port))

  with open('data6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      data = {"eventID":int(row[0]), "vehicleSpeed":int(row[1]), "vin":row[2], "fuelLevelInput":int(row[3]), "acceleration":float(row[4]), "longitude":float(row[5]), "latitude":float(row[6])}
      data_string = json.dumps(data)
      s.send(data_string.encode())
      time.sleep(2)

  s.close()

carSimulator3()