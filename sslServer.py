import socket, ssl

def deal_with_client(connstream):

   data = connstream.read()
   # null data means the client is finished with us
   f = open('testImage.png', 'wb')
   while data:
      # print bytearray(data)
      f.write(data)
      data = connstream.read()
   # finished with client
   image = bytearray(data)
   f.write(data)
   f.close()
   connstream.close()

def do_something(connstream, date):
    return False

if __name__ == '__main__':

    bindsocket = socket.socket()
    bindsocket.bind(('10.198.117.48', 10023))
    bindsocket.listen(5)

    while True:
       newsocket, fromaddr = bindsocket.accept()
       connstream = ssl.wrap_socket(newsocket,
                                    server_side=True,
                                    certfile="server.crt",
                                    keyfile="server.key",
                                    ssl_version=ssl.PROTOCOL_TLSv1)
       deal_with_client(connstream)