import socket
import time
from OSC import OSCClient, OSCMessage

# MDCX Configuration
MDCX_HOST="127.0.0.1" #This is the DEFAULT MDC-X IP on the LAN Port
MDCX_OSC_PORT=7475
# HTTP TCP Configuration
HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8080

# MDCX Function
def oscsender(obj,topic,msg):
	try:
		if msg is None:
			obj.send(OSCMessage(topic))
			print ("OSC LOG: TOPIC("+str(topic)+")")
		else:
			obj.send(OSCMessage(topic,msg))
			print ("OSC LOG: TOPIC("+str(topic)+") MSG("+str(msg)+")")
	except:
		print ("OSC ERROR - failed to send!")

# OSC socket for MDC Show control
mdcx_osc = OSCClient()
mdcx_osc.connect((MDCX_HOST, MDCX_OSC_PORT))

# HTTP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HTTP_HOST, HTTP_PORT))
server_socket.listen(1)

print("Warte auf Verbindung...")
conn, addr = server_socket.accept()
print("Verbunden mit:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode('utf-8')
    print("Received from client:", message)
    oscsender(mdcx_osc, "/mdc_layer1_preset1",1.0)
    time.sleep(5)
    oscsender(mdcx_osc, "/mdc_layer1_preset2", 1.0)

    # Sent reply
    reply = "Hello from the http server!"
    conn.sendall(reply.encode('utf-8'))

conn.close()
server_socket.close()

