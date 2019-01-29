import requests
import os 

# requests.delete("http://localhost:8000/api/data/cars/")
requests.delete("https://testing-894c8.firebaseio.com/.json")
os.remove("carStatus.db")