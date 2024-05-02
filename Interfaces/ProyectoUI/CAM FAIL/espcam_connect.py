import cv2, requests, numpy as np, socket, pickle, struct, imutils
from ultralytics import YOLO

pre_model = r'C:\Users\jpha\Documents\Arquitecturas\Raspberry\Interfaces\ProyectoUI\best.pt'
model = YOLO(pre_model)

rasp = '192.168.50.192'
jplaptop = '192.168.50.19'
client_socket = None

# ESP32 URL
URL = "http://192.168.50.254"
AWB = True

# # Socket Create
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

def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

if __name__ == '__main__':
    while True:
        if client_socket is None:
            client_socket,addr = server_socket.accept()
            print('GOT CONNECTION FROM:',addr)
        if client_socket:
            # CV2 START
            #vid = cv2.VideoCapture(URL + ":81/stream")
            #set_resolution(URL, index=8)
            vid = cv2.VideoCapture(0)
            print(vid.isOpened())
            if vid.isOpened():
                ret, frame = vid.read()
                if ret:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    gray = cv2.equalizeHist(gray)
                #resized_frame = cv2.resize(frame, (640, 640))
                #results = model(resized_frame, conf=0.6)
                #annotated_frame = results[0].plot()
                #cv2.imshow("frame", annotated_frame)
            # while(vid.isOpened()):
            #     img,frame = vid.read()
                #send_frame = imutils.resize(annotated_frame,width=320)
                send_frame = imutils.resize(frame,width=320)
                a = pickle.dumps(send_frame)
                message = struct.pack("Q",len(a))+a
                client_socket.sendall(message)
                
                cv2.imshow('TRANSMITTING VIDEO',send_frame)
                key = cv2.waitKey(1) & 0xFF
                if key ==ord('q'):
                    client_socket.close()
                    break
            
            # key = cv2.waitKey(1)
            # if key == ord('r'):
            #     idx = int(input("Select resolution index: "))
            #     set_resolution(URL, index=idx, verbose=True)
            # elif key == ord('q'):
            #     val = int(input("Set quality (10 - 63): "))
            #     set_quality(URL, value=val)
            # elif key == ord('a'):
            #     AWB = set_awb(URL, AWB)
            # elif key == 27:
            #     break
cv2.destroyAllWindows()
vid.release()