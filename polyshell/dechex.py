from ipaddress import ip_address

def iphex(ip: str, endianness: str) -> str:
    
    """
    Convert ip address to hexadecimal value

    Args:
        ip (str): IPv4 Address to convert
        endianness (str): Endianness of the system

    Returns:
        string: IPv4 address in hexadecimal format
    """

    try:
        # Testing if ip address is valid
        ip_address(ip)
        
        # VARIABLES
        decimal_result = int()
        dec_array = []

        ip_splitted = ip.split('.')
        last_octet = int(ip_splitted[-1])
        ip_splitted.pop()

        i = 3
    
        # Calculate the decimal value of the ip address given
        print(f"[debug] {ip_splitted}")
        for octet in ip_splitted: 
            oct_part = int(octet) * 256**i  
            dec_array.append(oct_part)
            i -= 1

        dec_array.append(last_octet)
        for elt in dec_array:   
            decimal_result += elt
        # Convert the decimal value of the ip address to hexadecimal and remove the 0x
        hexadecimal_result = hex(decimal_result)
        if len(hexadecimal_result) <= 10:
            hexadecimal_result = hexadecimal_result.replace("0x", "0x0")
        hexadecimal_result = str(hexadecimal_result)[2:]
        #Revert the element of the ip address if the endianness is little
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
        
        return hexadecimal_result
    
    except:
        return False

def porthex(port: str, endianness: str) -> str:
    
    """
    Convert a port to hexadecimal format

    Args:
        port (str): Port to convert
        endianness (str): Endianness of the system

    Returns:
        string: Port in hexadecimal value
    """

    if port.isdigit():
        if ((int(port) > 0) and (int(port) < 65535)):
            if endianness == 'little':
                intport = int(port)
                hexport = hex(intport)[2:]
                hexport_elts = [elt for elt in hexport]
                little_array = []
                
                if len(hexport_elts) % 2 != 0:
                    hexport_elts.insert(0, '0')
                    j = len(hexport_elts)
                    i = j - 2
                    
                else:
                    j = len(hexport_elts)
                    i = j - 2
                
                while i >= 0:
                    little_array.append(''.join(hexport_elts[i:j]))
                    i -= 2
                    j -= 2

                hexadecimal_result = ''.join(little_array)

            else:
                hexadecimal_result = hex(int(port))[2:]

            return hexadecimal_result
        
    else:
        return False