#!/usr/bin/env python3
import sys
import argparse
from polyshell import dechex


def main():
    banner = '''
    '''

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