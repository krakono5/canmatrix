import sys
import shlex

def mySplit(inLine):
    if sys.version_info > (3, 0):  # is there a clean way to to it?
        return shlex.split(inLine.strip())
    else:
        tempArray = shlex.split(inLine.strip().encode('utf-8'))
        newArray = []
        for item in tempArray:
            newArray.append(item.decode('utf-8'))
        return newArray


def mySplit2(string):
    inPhar = False
    splitted = []
    current = ""
    for char in string:
        if char == '"':
            if inPhar:
                inPhar = False
            else:
                inPhar = True
        if inPhar is False and char == ",":
            splitted.append(current)
            current = ""
        else:
            current += char

    splitted.append(current)
    return splitted