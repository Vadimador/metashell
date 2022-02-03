'''
;---------------- port : 1024 (hex: 0004)
mov r14w,0x1114
mov r13w,0x2221
sub r13w,0x1111
sub r14w,r13w
push r14w
;----------------
'''

def portbloc(port: str):
    print("\n========= portbloc funcion =========")
    base = "6641beport6641bdminus664181ed1111664529ee664156"
    print("port receive : " + port)
    minus = ""
    if(len(port) == 3):
        port = "0" + port
    port = port[2:4] + port[0:2]
    newport = port.replace("0","1")

    print("new port receive : " + newport)
    for i in range(0,len(newport)):
        if port[i] == "0" and newport[i] == "1":
            minus += "2"
        else :
            minus += "1"

    base = base.replace("port",newport)
    base = base.replace("minus",minus)
    
    print("my final ip bloc : " + base)
    print("=============== end ================\n")
    return base