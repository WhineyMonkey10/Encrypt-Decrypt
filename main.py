### 

from re import X


ll = [0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



stbe = input("String to be encrypted: ")

for i in stbe:
    list = {i: ll.index(i)}
    print(list)