import socket
import time

class CTFSocket():
	def __init__(self, host, port):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((host, port))
	def read(self):
		return self.socket.recv(4096)
	def send(self, message):
		return self.socket.send(str(message) + "\n")
	def readbig(self, timeout=2):
		self.socket.setblocking(0)
		total_data = []
		data = ''
		begin = time.time()
		while True:
			if(total_data and time.time()-begin > timeout):
				break
			elif(time.time()-begin > timeout * 2):
				break
			try:
				data = self.socket.recv(4096)
				if(data):
					total_data.append(data)
					begin = time.time()
				else:
					time.sleep(0.1)
			except:
				pass
		return ''.join(total_data)
	def close(self):
		return self.socket.close()

answers = []

while True:
	conn = CTFSocket("crypto.n0l3ptr.com", 10002)
	print conn.read()

	for i in range(10001):
		print "****** " + str(i) + " ******"
		conn.send('o')
		time.sleep(0.5)
		print conn.read()
		conn.send('8')
		time.sleep(0.5)
		output = conn.read()
		output = output.split('\n')[0]
		conn.send('g')
		time.sleep(0.5)
		print conn.read()
		print "****** " + output + " ******"
		if(len(answers) == i):
			answers.append('1')
		conn.send(answers[i])
		time.sleep(0.5)
		result = conn.read()
		if('False' in result):
			answers[i] = '0'
			print result
			break
		else:
			print result

conn.close()
