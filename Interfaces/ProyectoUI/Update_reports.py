import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from time import sleep



cred=credentials.Certificate('Interfaces\ProyectoUI\pan-orama-back.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
ordenes_ref=db.collection('ordenes')
total_ref=db.collection('totales').document('Bdak4QvaeHgGgvgcaq6O')

#updating the reports
global orders_old
orders_old = ordenes_ref.get()

def update_reports():
    global orders_old
    orders = ordenes_ref.get()
    if orders != orders_old:
        print('Updating reports...')
        orders_old = orders
        vent = 0
        asist = 0
        escan = 0
        ingre = 0
        cantidad = 0
        for order in orders:
            order = order.to_dict()
            vent += order['venta']
            asist += order['asistencia']
            escan += order['art']
            cantidad += 1
        
        print(vent)
        total_ref.update({
            'ingresos':vent,
            'asistencia':asist,
            'escaneos':escan,
            'ingresos':ingre,
            'ventas':cantidad
        })
        print('Reports updated')

while True:
    print('Checking for updates...')
    sleep(60*5)
    update_reports()