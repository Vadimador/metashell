
def ipbloc(ip: str):
    print("\n========== ipbloc funcion ==========")
    print("ip receive : " + ip)
    base = "beip4881ee11111111"
    ip = "0x" + ip
    hex_ip = hex(int(ip,16) + int("0x11111111",16))
    print("my new ip ! : " + str(hex_ip))
    hex_ip = str(hex_ip)[2:]
    tempip = ""
    for i in range(6,-1,-2):
        tempip += hex_ip[i]
        tempip += hex_ip[i+1]

    base = base.replace("ip",tempip)
    print("my final ip bloc : " + base)
    print("=============== end ================\n")
    return base