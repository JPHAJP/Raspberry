###-----------ESTE-------------###
import cv2, requests, numpy as np, socket, pickle, struct, imutils, firebase_admin
from ultralytics import YOLO
from firebase_admin import credentials, firestore

# Firebase
cred=credentials.Certificate('Interfaces\ProyectoUI\pan-oramico-firebase.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
cam_ref=db.collection('cam').document('P1xd33ke4RiCYFu9G75C')

pre_model = r'C:\Users\jpha\Documents\Arquitecturas\Raspberry\Interfaces\ProyectoUI\best.pt'
model = YOLO(pre_model)

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
	#Socket Message
	client_socket,addr = server_socket.accept()
	print('GOT CONNECTION FROM:',addr)
	if client_socket:
		vid = cv2.VideoCapture(0)
		
		while(vid.isOpened()):
			img,frame = vid.read()
			resized_frame = cv2.resize(frame, (640, 640))
			results = model(resized_frame, conf=0.6)
			annotated_frame = results[0].plot()
			#cv2.imshow("frame", annotated_frame)

			frame = imutils.resize(annotated_frame,width=320)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			
			cv2.imshow('TRANSMITTING VIDEO',frame)
			key = cv2.waitKey(1) & 0xFF
			if key ==ord('q'):
				client_socket.close()
	#Detection and firebase save
	data = cam_ref.get().to_dict()
	if data['status'] == True and data['capture'] == True:
		cam_ref.update({'capture':False})



		# results = model(frame, conf=0.6)
		# annotated_frame = results[0].plot()
		# cv2.imwrite('frame.jpg',annotated_frame)
		# cam_ref.update({'status':False})