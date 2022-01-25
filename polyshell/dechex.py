from configparser import ExtendedInterpolation

def iphex(ip: str, endianness: str):
    
    # VARIABLES
    decimal_result = int()
    decarray = []

    ip_splitted = ip.split('.')
    last_octet = int(ip_splitted[-1])
    ip_splitted.pop()


    i = 3
   
    for octet in ip_splitted: 
        octpart = int(octet) * 256**i  
        decarray.append(octpart)
        i -= 1


    decarray.append(last_octet)
    for elt in decarray:   
        decimal_result += elt   

    
    hexadecimal_result = hex(decimal_result)
    hexadecimal_result = str(hexadecimal_result)[2:]
    
    if endianness == 'little':
        big_array = [char for char in hexadecimal_result]
        little_array = []
        i = 6
        j = 8
        while i >= 0:
            little_array.append(''.join(big_array[i:j]))
            i -= 2
            j -= 2
        hexadecimal_result = ''.join(little_array)
    
    print(f'[+] Decimal : {decimal_result}')
    print(f'[+] Hexadecimal : 0x{hexadecimal_result}')

    return hexadecimal_result

def porthex(port: str, endianness: str):
    pass