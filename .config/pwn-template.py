#!/usr/bin/env python3

from pwn import *

{bindings}

context.binary = {bin_name}
context.log_level = "DEBUG"
context.terminal = ["tmux", "split-window", "-h"]
r = ROP({bin_name})

gs = '''
'''

def conn():
    if args.GDB:
        return gdb.debug({proc_args}, gdbscript=gs)
    elif args.REMOTE:
        return remote('addr',1337)
    else:
        return process({proc_args})


def main():
    p = conn()



    p.interactive()


if __name__ == "__main__":
    main()
