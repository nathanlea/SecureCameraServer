import socket, ssl, pprint, sys, picamera
from time import sleep

def get_bytes_from_file(filename):
    return (open(filename, "rb")).read()

if __name__ == '__main__':

   # camera=picamera.PiCamera()
   # camera.start_preview()
   # sleep(5)
   # camera.capture("/home/pi/SecureCameraServer/webcam/toSend.jpg")
   # camera.stop_preview()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipnathan = '139.78.71.59'
    portnathan = 10023
    #req cert from server
    ssl_sock = ssl.wrap_socket(s, ca_certs="/home/pi/SecureCameraServer/server.crt", cert_reqs=ssl.CERT_REQUIRED)

    ssl_sock.connect((ipnathan, portnathan))

    print repr(ssl_sock.getpeername())
    print ssl_sock.cipher()
    print pprint.pformat(ssl_sock.getpeercert())

    #simple http request-- use httplib in actual
    #ssl_sock.write(get_bytes_from_file(str(sys.argv)))
    ssl_sock.write(get_bytes_from_file("/home/pi/SecureCameraServer/webcam/toSend.jpg"))
    #read a data chunk, not necessarily all returned by server
    #data = ssl_sock.read()

    #note that closing the SSLSocket will also close underlying socket
    ssl_sock.close()
    exit()
