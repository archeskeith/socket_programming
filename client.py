import socket

#declares global variables
#variables match with the server variable values to initiate compatibility
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.5"
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#connect to the server

client.connect(ADDR)

#uses send function to send to server
def send(msg):
	#encodes the message according to the format (to ensure that the server can be able to read it)
	message = msg.encode(FORMAT)
	msg_length = len(message)

	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER-len(send_length))
	client.send(send_length)
	client.send(message)
	#receives the pig latin word from the server
	print(client.recv(2048).decode(FORMAT))

#uses while loop to loop input statements
#added initial input for initial statement
send(input("Input your statement here: \t"))
while(1):
	variable = input("[!] Do you still want to send messages? [1 if yes. Else, you'll be disconnected]: \t")
	if(variable == "1"):
		send(input("Input your statement here: \t"))
	else:
		send(DISCONNECT_MESSAGE)
		print("[!] Client Disconnected.")
		break


#REFERENCES:
#A quick Guide for translating to Pig Latin with Examples: https://bunnystudio.com/blog/library/translation/a-quick-guide-for-translating-to-pig-latin-with-examples/#:~:text=Pig%20Latin%20is%20a%20pseudo-language%20or%20argot%20where,word%20%E2%80%98pig%E2%80%99%20would%20become%20igp%2Bay%20which%20becomes%20igpay.
#Python Socket Programming Tutorial: https://www.youtube.com/watch?v=3QiPPX-KeSc
		