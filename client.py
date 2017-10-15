import socket
MAX_DATA_ALLOWED = 1024

def main():
	server_ip = "127.0.0.1"
	port = 5004
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
	s.connect((server_ip,port))
	request = "Hello looser"
	while True:
		s.send(request.encode('ascii'))
		response = s.recv(MAX_DATA_ALLOWED)
		print "response : ",str(response.decode('ascii'))
		ans = raw_input("enter message")
		if ans=='y' or ans=='Y':
			continue
		else:
			break
main()



