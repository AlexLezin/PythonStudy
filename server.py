import socket
import sys

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    ms.bind(("", 80))
except socket.error:
    print("Failed to bind")
    sys.exit()
ms.listen(5)
while True:
    conn, addr = ms.accept()
    data = conn.recv(1000)
    if data:
        print("Got a request!")

    outdata = b"Hello World!"
    
    conn.sendall(outdata)
  
conn.close()
ms.close()
