from nltk.corpus import words
with open('shadow.txt') as f:
    lines = f.readlines()



import base64
#Parsing hashes
hashes = {
            "08": {},
            "09": {},
            "10": {},
            "11": {},
            "12": {},
            "13": {}
          }

salts = ["M9xNRFBDn0pUkPKIVCSBzu", "xGKjb94iwmlth954hEaw3O", "/8UByex2ktrWATZOBLZ0Du", "rMeWZtAVcGHLEiDNeKCz8O", "6ypcazOOkUT/a7EwMuIjH." ]


#Ind: 0 = Name, 1 = Algorithm, 2 = WF, 3= Salt, 4 = HashVal
for x in lines:
    temp = x.split("$")
    salt = temp[3][:22]
    hash_val = temp[3][22:]
    hash_val = hash_val[:len(hash_val) - 1]
    hash_val = (str("$") + str(temp[1]) + str("$") + str(temp[2]) + str("$") + str(salt) + str(hash_val)).encode("ascii")
    
    hashes[str(temp[2])][hash_val] = temp[0]
    
    """ print(len(salt))
    print(len(hash_val))
    print("") """

print(hashes)

import bcrypt


""" SALTS
8: J9FW66ZdPI2nrIMcOxFYI.
9: M9xNRFBDn0pUkPKIVCSBzu
10: xGKjb94iwmlth954hEaw3O
11: /8UByex2ktrWATZOBLZ0Du
12: rMeWZtAVcGHLEiDNeKCz8O
13: 6ypcazOOkUT/a7EwMuIjH.  
"""

import datetime
a = datetime.datetime.now().replace(microsecond=0)
#Realized that we can crack passwords w same salt simultaneously
for y in range(2,len(salts)):
    if y == 0:
        index = "09"
        encoded_salt = ("$2b$09$M9xNRFBDn0pUkPKIVCSBzu").encode("ascii")
    if y == 1:
        index = "10"
        encoded_salt = ("$2b$10$xGKjb94iwmlth954hEaw3O").encode("ascii")
    if y == 2:
        index = "11"
        encoded_salt = ("$2b$11$/8UByex2ktrWATZOBLZ0Du").encode("ascii")
    if y == 3:
        index = "12"
        encoded_salt = ("$2b$12$rMeWZtAVcGHLEiDNeKCz8O").encode("ascii")
    if y == 4:
        index = "13"
        encoded_salt = ("$2b$13$6ypcazOOkUT/a7EwMuIjH.").encode("ascii")
    
    for x in words.words():
        if 6 <= len(x) <= 10:
            password = str(x).encode("ascii")
            #Turning salt we have into an encoded salt of format b'$2b$WORKFACTOR$SALT'
            hashed = bcrypt.hashpw(password, encoded_salt)
            if hashed in hashes[index].keys():
                print("MATCH")
                print("password is " + str(x))
                print(hashes[index][hashed])
                b = datetime.datetime.now().replace(microsecond=0)
                print("Time took: " + str(b-a))
                a = datetime.datetime.now().replace(microsecond=0)
                print(" ")
                break
            
        
       
       
       
            
    




