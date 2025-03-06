#!/usr/bin/env python3

from pwn import *

{bindings}

elf = ({bin_name})

context.terminal = ["tmux", "split-window", "-h"]
context.log_level = "DEBUG"
context.binary = elf

gdb_cmds = ["c"]

def conn():
    if args.GDB:
        p = elf.debug(gdbscript="\n".join(gdb_cmds))
    elif args.REMOTE:
        p = remote("addr", 1337)
    else:
        p = elf.process()
    return p

def main():
    p = conn()

    # good luck pwning :)

    p.interactive()


if __name__ == "__main__":
    main()
