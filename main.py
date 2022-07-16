### 


ll = [0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", ",", ";", ":", "!", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]





stbe = input("String to be encrypted: ")

code = []



def encrypt(stbe):
    for i in stbe:
        code.append(ll.index(i))
    return code
print((encrypt(stbe)))
write = input("Write to a file? (y/n)")
if write == "y":
    fname = input("Enter file name, without extension. If one of the same name is already created it will be overwritten, otherwise it will create a new file. ")
    if input == "n":
        f = open("encrypted.txt", "w")
        f.write(str(code))
        f.close()
        print("Wrote to file encrypted.txt")
    else:
        f = open(fname, "w")
        f.write(str(code))
        f.close()
        print(f"Wrote to file {input}")
else:
    print("Cancelled")
    pass


print("""
        
        
        
        Decryption:



""")


def decrypt(dcode):
    stbe = ""
    for i in dcode:
        stbe += ll[i]
    return stbe

print("Decrypted string: " + (decrypt(code)))
write = input("Write to a file? (y/n)")
if write == "y":
    fname = input("Enter file name, without extension. If one of the same name is already created it will be overwritten, otherwise it will create a new file. ")
    if input == "n":
        f = open("decrypted.txt", "w")
        f.write(str((decrypt(code))))
        f.close()
        print("Wrote to file decrypted.txt")
    else:
        f = open(fname, "w")
        f.write(str((decrypt(code))))
        f.close()
        print(f"Wrote to file {fname}")













#for i in stbe:
#    list = ({i: ll.index(i)})
#    print(list)
#    code.append({i: ll.index(i)})
#print(code)