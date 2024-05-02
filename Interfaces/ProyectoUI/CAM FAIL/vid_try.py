import socket,cv2, pickle,struct
from ultralytics import YOLO

pre_model = r'C:\Users\jpha\Documents\Arquitecturas\Raspberry\Interfaces\ProyectoUI\best.pt'
model = YOLO(pre_model)

rasp = '192.168.50.192'
jplaptop = '192.168.50.19'
my_socket = None

# Create socket
try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_ip = rasp # paste your server ip address here
    port = 9999
    client_socket.connect((host_ip,port)) # a tuple
    data = b""
    payload_size = struct.calcsize("Q")
    print("Socket Created")
except:
    print('Cant create reciving socket')

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    host_ip = jplaptop  # Ensure the IP is accessible in your network
    print('HOST IP:', host_ip)
    port = 8888
    socket_address = (host_ip, port)
    # Socket Bind
    server_socket.bind(socket_address)
    # Socket Listen
    server_socket.listen(5)
    print("LISTENING AT:", socket_address)
except:
    print('Cant transmit stream')

def recv_video(data, payload_size, client_socket):
    try:
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024) # 4K
            if not packet: break
            data+=packet
            print("Recieving data")
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        
        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        frame_data = data[:msg_size]
        data  = data[msg_size:]
        frame = pickle.loads(frame_data)
        resized_frame = cv2.resize(frame, (1020, 720))
        results = model(resized_frame, conf=0.6)
        annotated_frame = results[0].plot()
        return annotated_frame
    except Exception as e:
        print("Connection closed or error occurred:", e)
        #client_socket.close()  # Make sure we close the socket on error

while True:
    frame = recv_video(data, payload_size, client_socket)
    if my_socket is None:
        my_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if my_socket:
        a = pickle.dumps(frame)
        message = struct.pack("Q",len(a))+a
        my_socket.sendall(message)
        my_socket.close()
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break


client_socket.close()