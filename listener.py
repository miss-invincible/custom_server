import socket
from thread import *
import threading
 
client_lock = threading.Lock()
MAX_DATA_ALLOWED = 1024	

def get_server_ip():
	return socket.gethostbyname('www.google.com')
	 
def get_server_port():
	return 5004

def get_max_conn():
	return 100

class Server:
	total_servers = 0
	def __init__(self, ip, 	port, max_conn):
		self.ip = ip
		self.port = port
		self.host = ""
		Server.total_servers += 1
		self.max_conn = max_conn

	def get_server(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((self.host, self.port))	

	def start_listening(self):
		self.server.listen(self.max_conn)

	def accept_conn(self):
		return self.server.accept()

	def close_conn(self):
		self.server.close()

		

def process_request(c):
	while True:
		request = c.recv(MAX_DATA_ALLOWED)
		request = request.decode('ascii');
		response = "Thread id : " + str(threading.currentThread())
		c.send(response)
		if not request:
			print "closing the connection"
			break
	c.close()



def main():
	server = Server(get_server_ip(), get_server_port() ,get_max_conn())
	server.get_server()
	server.start_listening()
	clients = 0
	while True:
		clients += 1
		print "client number : " + str(clients)
		(c, addr) = server.accept_conn()
		print c,addr
		print('Connected to :', addr[0], ':', addr[1])
		start_new_thread(process_request, (c,))
	server.close_conn()

main()
