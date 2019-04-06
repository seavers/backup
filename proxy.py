import  socket

def recv_basic(the_socket):
    total_data=[]
    while True:
        data = the_socket.recv(102)    
        if not data: break
        total_data.append(data)
    return ''.join(total_data)

def handle_request(client):
    buf = recv_basic(client)    ##client.recv(1024)
    
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send('<h1>Hello World</h1>')
    client.send(buf)

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('0.0.0.0',8008))
    sock.listen(1)
    while True:
         connection,address = sock.accept()
         handle_request(connection)
         connection.close()
if __name__ == '__main__':
    main()
