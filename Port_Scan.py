from socket import *

ip = input("Enter The IP : ") 

print

ports = [13,21,22,23,53,80,445,443,3389]

for i in ports :

    sock = socket(AF_INET , SOCK_STREAM)
    sock.settimeout(1)
    r = sock.connect_ex((ip , i))

    if r == 0:
        print( "open : " ,i, " " , getservbyport(i))

