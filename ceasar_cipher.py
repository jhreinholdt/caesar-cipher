# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:33:33 2017

@author: jhreinholdt

Caesar cipher - Implement a Caesar cipher, both encoding and decoding. 
The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). 
The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). 
So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". 
This simple "monoalphabetic substitution cipher" provides almost no security, 
because an attacker who has the encoded message can either use frequency analysis to guess the key, 
or just try all 25 keys.
"""
from types import *

import string

def encode(key, plaintext):
    assert type(key) is int, "key is not an integer: %r" % key
    ciphertext = ''
    for char in plaintext:
#        print((ord(char)+key)-97)
        cipherchr = chr((((ord(char) + key) - 97) % 26) + 97)
        ciphertext += cipherchr
#        print("Plaintext: ", char, " Ciphertext: ", cipherchr)
#    print("Ciphertext: ", ciphertext)
    return ciphertext

def decode(key, ciphertext):
    assert type(key) is int, "key is not an integer: %r" % key
    plaintext = ''
    for char in ciphertext:
        plainchr = chr((((ord(char) - key) - 97) % 26) + 97)
        plaintext += plainchr
#    print("Plaintext: ", plaintext)   
    return plaintext 
    
    
def main():
    ciphertext = encode(25, input("Enter plaintext: "))
    print("Ciphertext: ", ciphertext)
    for key in range(1,26):
        plaintext = decode(key, ciphertext)
        print("Decoded plaintext with key#", key, ":", plaintext)

if __name__ == '__main__':
    main()