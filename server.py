import socket
import threading
import piglatin

HEADER = 64
PORT = 5050


#gets machine's server automatically
#declares global variables
#variables match with the server variable values to initiate compatibility
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#binds server to the address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


#uses handle client
def handle_client(conn,addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	connected = True

	#accepts the message, and converts the message according to pig latin function
	while(connected):
		#decodes the messages according to the format
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			
			#disconnects from the server
			if msg == DISCONNECT_MESSAGE:
				print("[!] Server Disconnected.")
				connected = False
				break

			#start of pig latin function
			arry = msg.split()
			newArry = []

			for x in arry:
				newArry.append(piglatin.wordperword(x))

			print(f"[{addr}]",end=" ")
			wordd = ""
			for y in newArry:
				wordd+=y
				wordd+=" "


			print(wordd)

			#sends the pig latin to the client
			conn.send(wordd.encode(FORMAT))

	conn.close()

#starts the server
def start():
	#server listens until a client tries to connect with it
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		#server accepts connections from the client
		#makes use of Threads to handle clients
		conn, addr = server.accept()
		thread = threading.Thread(target = handle_client, args=(conn,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()



#REFERENCES:
#A quick Guide for translating to Pig Latin with Examples: https://bunnystudio.com/blog/library/translation/a-quick-guide-for-translating-to-pig-latin-with-examples/#:~:text=Pig%20Latin%20is%20a%20pseudo-language%20or%20argot%20where,word%20%E2%80%98pig%E2%80%99%20would%20become%20igp%2Bay%20which%20becomes%20igpay.
#Python Socket Programming Tutorial: https://www.youtube.com/watch?v=3QiPPX-KeSc