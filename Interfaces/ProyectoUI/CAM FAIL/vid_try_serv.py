import socket,cv2,pickle,struct,imutils
rasp = '192.168.50.192'
jplaptop = '192.168.50.19'
client_socket = None

trying=True
# Socket Create
# PROCCES WITH YOLO AND RETURN TO DEVICE TO SHOW
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    host_ip = rasp  # Ensure the IP is accessible in your network
    print('HOST IP:', host_ip)
    port = 9999
    socket_address = (host_ip, port)
    # Socket Bind
    server_socket.bind(socket_address)
    # Socket Listen
    server_socket.listen(5)
    print("LISTENING AT:", socket_address)
except:
    print('Cant transmit stream')

def recv_video(data, client_socket, payload_size):
    try:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        return frame
    except Exception as e:
        print("Connection closed or error occurred whlie recv:", e)
        #client_socket.close()  # Make sure we close the socket on error

def send_video(client_socket):
    vid = cv2.VideoCapture(0)
    try:
        if vid.isOpened():
            ret, frame = vid.read()
            frame = imutils.resize(frame, width=320)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

            # cv2.imshow('TRANSMITTING VIDEO', frame)
            # key = cv2.waitKey(1) & 0xFF
            # if key == ord('q'):
            #     break
    except Exception as e:
        print("Connection closed or error occurred while send:", e)
        #client_socket.close()  # Make sure we close the socket on error

try:
    while True:
        print(client_socket)
        if client_socket is None:
            client_socket, addr = server_socket.accept()
            print('GOT CONNECTION FROM:', addr)
        try:
            print('Trying to send stream')
            send_video(client_socket)
        except Exception as e:
            print("Connection closed or error occurred AAAA:", e)
            client_socket.close() # Make sure we close the socket on error
        try:
            print('Trying to get return stream')
            while trying==True:
                try:
                    print(trying)
                    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    host_ip = jplaptop
                    port = 8888
                    my_socket.connect((host_ip, port))  # a tuple
                    data = b""
                    payload_size = struct.calcsize("Q")
                    trying=False
                except:
                    trying=True
                    print('Cant get return stream')
            frame = recv_video(data,my_socket,payload_size)
            if frame is not None:
                print('Frame received')
            #cv2.imshow("RECEIVING VIDEO", frame)
            #key = cv2.waitKey(1) & 0xFF
            #if key == ord('q'):
            #    break
        except Exception as e:
            print("Connection closed or error occurred BBBB:", e)
            client_socket.close()
finally:
    server_socket.close()