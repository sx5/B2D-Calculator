def b2d():
    import os
    os.system('cls & title BIN TO DEC CALCULATER BY EXOTIC (Insert "done" to exit)')
    exobin = list(input("> Binary number: "))
    num = 0

    for i in range(len(exobin)):
    	exoticpedo = exobin.pop()
    	if exoticpedo == '1':
    		num = num + pow(2, i)
    print("[+] Dec: ",num)
    input("\nPress any key to restart...")
    b2d()
b2d()
