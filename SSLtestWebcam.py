import socket, ssl, pprint, sys

def get_bytes_from_file(filename):
    return (open(filename, "rb")).read()

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipnathan = '139.78.71.59'
    portnathan = 10024
    #req cert from server
    ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)

    ssl_sock.connect((ipnathan, portnathan))

    print repr(ssl_sock.getpeername())
    print ssl_sock.cipher()
    print pprint.pformat(ssl_sock.getpeercert())

    #simple http request-- use httplib in actual
    #ssl_sock.write(get_bytes_from_file(str(sys.argv)))
    ssl_sock.write(get_bytes_from_file('webcam/toSend.jpg'))
    #read a data chunk, not necessarily all returned by server
    #data = ssl_sock.read()

    #note that closing the SSLSocket will also close underlying socket
    ssl_sock.close()
    exit()
