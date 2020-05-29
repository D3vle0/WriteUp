from pwn import *
context.log_level = 'debug'
p=remote('p1.tjctf.org', 8003)

p.recvuntil('what is ')
math=p.recvuntil('?')[:-1]
p.sendline(str(eval(math)))

p.interactive()