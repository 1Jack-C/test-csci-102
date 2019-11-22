#Jack Chapman
#CSCI 102 sec C
#Week 12 Utility


def PrintOutput(string):
    print("OUTPUT", string)


def LoadFile(filename):
    file = open(filename)
    output = file.read()
    output = output.split("\n")
    return output


def UpdateString (string, char, index):
    output = ""
    for a in range(0,len(string)):
        if a == index:
            output = output + char
        else:
            output = output + string[a]
    return output


def FindWordCount(list, word):
    count = 0
    for words in list:
        if words == word:
            count = count + 1
    return count



a = LoadFile("test.txt")
PrintOutput(str(FindWordCount(a, 'adam')))