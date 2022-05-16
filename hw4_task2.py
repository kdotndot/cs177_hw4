with open('shadow.txt') as f:
    lines = f.readlines()


#Parsing hashes
hashes = []
for x in lines:
    temp = x.split("$")
    salt = temp[3][:22]
    hash_val = temp[3][23:]
    print(salt)
    print(hash_val)
