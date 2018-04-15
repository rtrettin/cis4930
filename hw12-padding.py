import socket
import time
import sys

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

conn = CTFSocket("crypto.n0l3ptr.com", 10004)
conn.read()
conn.send('u')
time.sleep(0.5)
output = "206f732e7572616e646f6d28313629208f793169efcbf025c9c9b1bc2061ff9b"
known = "580e40195d001b0058018b920f6118d7"
output = output.split('\n')[0][:-2]

for i in range(256):
    print str(i)
    conn.send('d')
    time.sleep(0.5)
    hexstr = str(hex(i).split('x')[-1])
    if(len(hexstr) == 1):
        conn.send(output + '0' + hexstr + known)
    else:
        conn.send(output + hexstr + known)
    time.sleep(0.5)
    result = conn.read()
    if('Incorrect' not in result):
        print str(hex(i))
        sys.exit()

conn.close()
