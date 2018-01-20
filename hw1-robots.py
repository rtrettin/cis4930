def encode(codestr, xor, shift):
	return [basestr[((basestr.index(s)^xor)+shift)%64] for s in codestr]

def decode(codestr, xor, shift):
	xor = xor % 64
	shift = shift % 64
	return [basestr[((basestr.index(s)%64)-shift)^xor] for s in codestr]

basestr = ""
codestr = ""

output = open('out.txt', 'w')
for i in range(0, 64):
	for k in range(0, 64):
		output.write(''.join(decode(codestr, i, k)) + "\n")
		if(i != k):
			output.write(''.join(decode(codestr, k, i)) + "\n")
output.close()
