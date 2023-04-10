import bz2
import codecs

def ToBinary(letters):
    binaryFromText = ""
    for i in letters:
        x = ord(i)
        y = bin(x)
        binaryFromText += y.replace("0b", (18 - len(y)) * "0")
    binaryFromText += (4 * "0") if(len(binaryFromText) % 6 == 2) else (2 * "0")
    return binaryFromText

def ToBase64(text):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
                '/']

    chars = list(text)
    output = ""
    binletters = ToBinary(chars)

    for k in range(0, len(binletters), 6):
        x = binletters[k:k + 6]
        output += alphabet[int(x, 2)]

    output += "=" * (len(chars) % 3)
    return output

filePath1 = "D:/Dania/1.txt"
with codecs.open(filePath1, "r", encoding='utf-8') as file:
    text = file.read()

path = filePath1.replace(".txt", "_base.txt")
with open(path, "w") as file1:
    file1.write(ToBase64(text))

# filePath2 = "D:/Dania/3_base.txt.bz2"
# with bz2.open(filePath2, "rt") as bz_file:
#     bzText = bz_file.read()
#
# path = filePath2.replace("_base.txt.bz2", "bz2_base.txt")
# with open(path, "w") as bz_file2:
#     bz_file2.write(ToBase64(bzText))

# path1 = "G:/Dania/1.txt"
# path2 = "G:/Dania/2.txt"
# path3 = "G:/Dania/3.txt"
