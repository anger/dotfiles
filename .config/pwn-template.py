#!/usr/bin/env python3

from pwn import *

{bindings}

elf = ({bin_name})
context.binary = elf
context.terminal = ["tmux", "split-window", "-h"]
context.log_level = "DEBUG"
gdb_cmds = ["c"]

def sla(x : bytes | str, y : bytes | str): p.sendlineafter(x, y)
def sa(x: bytes | str, y: bytes | str): p.sendafter(x, y)
def sl(x: bytes | str): p.sendline(x)
def s(x: bytes | str): p.send(x)
def rl() -> bytes: return p.recvline()
def ru(x: bytes | str) -> bytes: return p.recvuntil(x)
def rv(n: int) -> bytes: return p.recv(n)

if args.GDB:
    p = elf.debug(gdbscript="\n".join(gdb_cmds))
elif args.REMOTE:
    p = remote("addr", 1337)
else:
    p = elf.process()

# good luck buddy



p.interactive()
