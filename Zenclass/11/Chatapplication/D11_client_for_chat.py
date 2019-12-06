import time,socket,sys
print("\nWELCOME TO CHAT ROOM")
print("Intialsing......!")
time.sleep(1)
s=socket.socket()
host=socket.gethostname()
ip=socket.gethostbyname(host)
port=1234
print(host,"(",ip,")\n")
host= input("enter the server address to connect: ")
name=input("enter your name: ")
port=1234
print("trying to connect",host)
time.sleep(1)
s.connect((host,port))
print("connected")
s.send(name.encode())
s_name=s.recv(1024)
s_name=s_name.decode()
print(s_name,"has joined the chat room")
while True :
    message=s.recv(1024)
    message=message.decode()
    print(s_name,":",message)
    message=input("me: ")
    s.send(message.encode())
    
