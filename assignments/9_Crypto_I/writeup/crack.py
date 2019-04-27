#!/usr/bin/env python2

import hashlib
import string

def crack():
    hashes_file = "/home/389Rspring19/assignments/9_Crypto_I/hashes.txt"
    passwords_file = "/home/389Rspring19/assignments/9_Crypto_I/passwords.txt"
    characters = string.ascii_lowercase

    hashes = open(hashes_file, "r")
    passwords = open(passwords_file, "r")
    
    passwords = [p.strip() for p in passwords]
    hashes = [h.strip() for h in hashes]
    
    for c in characters:
        for p in passwords:
            # crack hashes
            test = c + p
            has = hashlib.sha256(test).hexdigest()
            for h in hashes:
                if h == has:
                    print(test+":"+h);
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
