import socket
from decimal import Decimal

class CTFSocket():
	def __init__(self, host, port):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((host, port))
	def read(self):
		return self.socket.recv(4096)
	def send(self, message):
		return self.socket.send(str(message) + "\n")

conn = CTFSocket("practice.n0l3ptr.com", 8889)
count = 1
while(True):
	read = conn.read()
	print "Read: " + read
	if(count == 1):
		target = read[1:5]
	else:
		target = read[len('correct!\n$'):-len('\n$10,000 bills:\n')]
	print "Target: " + target
	target = Decimal(target)

	bills_10k = target / 10000
	target = target % 10000
	bills_5k = target / 5000
	target = target % 5000
	bills_1k = target / 1000
	target = target % 1000
	bills_500 = target / 500
	target = target % 500
	bills_100 = target / 100
	target = target % 100
	bills_50 = target / 50
	target = target % 50
	bills_20 = target / 20
	target = target % 20
	bills_10 = target / 10
	target = target % 10
	bills_5 = target / 5
	target = target % 5
	bills_1 = target / 1
	target = target % 1
	cents_50 = target / Decimal('0.50')
	target = target % Decimal('0.50')
	cents_25 = target / Decimal('0.25')
	target = target % Decimal('0.25')
	cents_10 = target / Decimal('0.10')
	target = target % Decimal('0.10')
	cents_5 = target / Decimal('0.05')
	target = target % Decimal('0.05')
	cents_1 = target / Decimal('0.01')

	conn.send(int(bills_10k))
	print conn.read()
	conn.send(int(bills_5k))
	print conn.read()
	conn.send(int(bills_1k))
	print conn.read()
	conn.send(int(bills_500))
	print conn.read()
	conn.send(int(bills_100))
	print conn.read()
	conn.send(int(bills_50))
	print conn.read()
	conn.send(int(bills_20))
	print conn.read()
	conn.send(int(bills_10))
	print conn.read()
	conn.send(int(bills_5))
	print conn.read()
	conn.send(int(bills_1))
	print conn.read()
	conn.send(int(cents_50))
	print conn.read()
	conn.send(int(cents_25))
	print conn.read()
	conn.send(int(cents_10))
	print conn.read()
	conn.send(int(cents_5))
	print conn.read()
	conn.send(int(cents_1))

	count = count + 1
