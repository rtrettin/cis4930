import socket
import math
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

conn = CTFSocket("crypto.n0l3ptr.com", 8001)

for i in range(100):
	data = conn.readbig()
	sdata = data[:data.find('G')].rstrip()

	binstr = ''.join(format(ord(x), 'b') for x in sdata)
	print binstr

	print "Count: " + str(i)
	num0 = (binstr.count("0") / float(len(binstr))) * 100
	num1 = (binstr.count("1") / float(len(binstr))) * 100
	print "0s: " + str(num0)
	print "1s: " + str(num1)

	if(num0 < 46.0):
		conn.send("0") # bad
	else:
		conn.send("1") # good

print conn.read()

conn.close()
