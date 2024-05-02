###-----------ESTE-------------###

import cv2, requests, numpy as np, socket, pickle, struct, imutils
from ultralytics import YOLO

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
				