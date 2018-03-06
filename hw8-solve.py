from pwn import *

context(arch='amd64')

conn = process('./number')
conn.recvline()
conn.sendline('1152')
numberFlag = conn.recv()
conn.close()
print numberFlag

cmps = [0x51, 0x35, 0x57, 0x5a, 0x9c, 0x42, 0x62, 0x8c, 0x5c, 0x26, 0xaa, 0x3c, 0x1d, 0xa1, 0x45, 0xa3, 0x1b, 0x45, 0x93, 0x2b, 0x3b, 0x92, 0x56, 0x2c, 0x43, 0x59, 0x4b, 0x75, 0x7d, 0x7d]
arrgsFlag = ''
for i in range(0, len(cmps), 3):
    arrgsFlag = arrgsFlag + chr((cmps[i] + cmps[i + 1]) / 2)
    arrgsFlag = arrgsFlag + chr((cmps[i] + cmps[i + 2]) / 2)
    arrgsFlag = arrgsFlag + chr((cmps[i + 1] + cmps[i + 2]) / 2)
print arrgsFlag
