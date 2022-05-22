'''
Flaws: Symbols, FortifyFortified
Security: PIE enabled, NX enabled, Canary, Full RELRO

Challenge consists of finding a String that xored with 0x30 gives you access

0x55c4b80007ca --> sys.win()

$ key = b'y\x17FU\x10S_]U\x10XUBU\x10D_:'
$ xor(key, b'\x30')
Out[3]: b"I've come here to\n"

'''
from pwn import *

p = process("./chall_09")
#elf = ELF("./chall_09")
#l1 = xor(elf.string(elf.sym.key), b'\x30')
l1 = b"I've come here to\n"

p.send(l1)
p.interactive()