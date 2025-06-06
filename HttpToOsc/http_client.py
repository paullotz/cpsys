# client_py2.py
import socket

HOST = '10.42.0.1'  # IP-Adresse des Python 3 Servers anpassen
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Nachricht senden
message = "Hallo vom Python 2 Client!"
client_socket.sendall(message.encode('utf-8'))

# Antwort empfangen
data = client_socket.recv(1024)
print("Antwort vom Server:", data.decode('utf-8'))

client_socket.close()