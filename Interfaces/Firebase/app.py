import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
print("Firebase app initialized")

db = firestore.client()
clima_ref = db.collection("clima")
actual_ref = db.collection("actual").document("zsvSEgB2aB1LqNPMdFC0")

def create_data(t,h,p):
    data = {
        "datetime": datetime.now(),
        "temp": t,
        "hum": h,
        "pres": p
    }
    #clima_ref.document().set(data)
    print("Data added")

def read_data():
    docs = clima_ref.get()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

def update_data(id,t,h,p):
    data = {
        "datetime": datetime.now(),
        "temp": t,
        "hum": h,
        "pres": p,
    }
    clima_ref.document(id).update(data)
    print("Data updated")

def update_actuales(t,h,p,l):
    data = {
        "temp": t,
        "hum": h,
        "pres": p,
        'led': l
    }
    actual_ref.update(data)
    print("Data updated")

temp = float(input("Enter temperature: "))
hum = float(input("Enter humidity: "))
pres = input("Enter pressure: ")
led = True

#create_data(temp, hum, pres)
update_data(temp, hum, pres, led)