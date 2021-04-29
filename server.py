import socket
import threading
import datetime


users = []

def open_file():
    file = open("index.html","r") 

    data = file.read()

    return data

def create_socket():
   
    soc = socket.socket()  
    soc.bind(("127.0.0.1",8000))

    return soc


def handle_each_user(conn,addr):  
    while True:
        msg = conn.recv(2048)
       
        data = open_file()

        response = ""

        if(len(msg) != 0):
            print(msg.decode("utf-8"))
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type : text/html; charset = utf-8\r\n"
            response += "\r\n"
            response += data       
            response += "\r\n\r\n"
            conn.sendall(response.encode())
            conn.shutdown(socket.SHUT_WR)
        
    
def main_server_loop(): 
    soc = create_socket()
    soc.listen()

    while True:
        conn,addr = soc.accept()
        users.append([conn,addr])
        print(conn)
        t1 = threading.Thread(target = handle_each_user,args = (conn,addr))
        t1.start()


        

        
        
main_server_loop()
        



    