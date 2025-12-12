import socket
import time
import threading

serverIp = "104.248.18.8"
serverPort = 3478
server_addr = (serverIp, serverPort)

my_username = ""#Write your own name
username_message=my_username.encode()
my_port = 5454

users={}

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",my_port))

def sendHeartBeat():
    while True:
        sock.sendto(username_message,server_addr)
        time.sleep(10)

thr1=threading.Thread(target=sendHeartBeat,daemon=True)
thr1.start()
print("Heartbeat signals are being sent in background")

def savePeers(message):
    lines=message.split("\n")
    for line in lines:
        parts=line.split(",")
        # Added a safety check to prevent crash if line is empty
        if len(parts) >= 4:
            users[parts[0]]={
                "ip":parts[1],
                "port":parts[2],
                "last_seen":parts[3]
            }

def showPeers():
    for username, data in users.items():
        print(f"Username: {username} <-> Last seen is {data['last_seen']} seconds ago.")

def recvMessage():
    while True:
        try:
            data,addr=sock.recvfrom(1024)
            message=data.decode(errors="ignore")
            if (addr[0]==serverIp):
                savePeers(message)
                showPeers()
            else:
                print(f"From {addr[0]}:{message}")
        except:
            continue

thr2=threading.Thread(target=recvMessage,daemon=True)
thr2.start()

def sendMessage():
    takenUsername = "" # Initialize variable scope
    while True:
        sock.sendto("LIST".encode(),server_addr)
        print("Please enter username of the peer you want to chat:")
        
        # Give the background thread a moment to receive the list
        time.sleep(1) 
        
        takenUsername=input()
        if takenUsername not in users:
            print("User not found. Please try again")
        else:
            # Fixed typo: takenUserName -> takenUsername
            user=takenUsername
            break
            
    # Fixed: Removed quotes around variable name users[takenUsername]
    print(f"You can start chatting with {users[takenUsername]}")
    
    while True:
        message=input()
        if message=="LIST":
            m2=message.encode()
            sock.sendto(m2,server_addr)
        else:
            m2=message.encode()
            # Fixed typo: takenUserName -> takenUsername
            target_ip = users[takenUsername]["ip"]
            target_port = int(users[takenUsername]["port"])
            sock.sendto(m2, (target_ip, target_port))

sendMessage()
