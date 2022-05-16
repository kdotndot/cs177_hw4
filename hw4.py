import hashlib
from string import ascii_lowercase
import random

import itertools

from numpy import place


def hamming(string1, string2):
    count = 0
    if len(string1) != len(string2):
        print("UNEQUAL LENGTH")
        return
    
    for x in range(0,len(string1)):
        if string1[x] != string2[x]:
            count += 1
            
    return count

def truncate(string1, length):
    return string1[:length]


dict = {}


def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)

import datetime
a = datetime.datetime.now().replace(microsecond=0)
import binascii



for x in range(8,52, 2):
    dict = {}
    inputs = 0
    for s in iter_all_strings():
        hashed = hashlib.sha256(s.encode('utf-8')).hexdigest()
        hashed = int(hashed, 16)
        hashed = str(bin(hashed)[2:])
        hashed = truncate(hashed, x)
        
        if hashed in dict:
            print("Digest size: " + str(x))
            print(dict[hashed])
            print(s)
            b = datetime.datetime.now().replace(microsecond=0)
            print("NUM INPUTS = " + str(inputs))
            print("Time took: " + str(b-a))
            a = datetime.datetime.now().replace(microsecond=0)
            print("")
            break
        else:
            dict[hashed] = s
            inputs += 1
    
    


    



    
        