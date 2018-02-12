b = bytearray(open('l33t.png', 'rb').read())
for i in range(len(b)):
	if i % 2 == 0:
		b[i] ^= 0x13
	else:
		b[i] ^= 0x37
open('done.png', 'wb').write(b)
