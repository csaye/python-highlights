f = open("translate.txt", "r")
content = f.read()
f.close()

val = ""
while (val != "encrypt" and val != "decrypt"):
    val = input("encrypt or decrypt?\n")

f = open("translate.txt", "w")

if (val == "encrypt"):
    for char in content:
        f.write(chr(ord(char) + 1))
else:
    for char in content:
        f.write(chr(ord(char) - 1))

f.close()
