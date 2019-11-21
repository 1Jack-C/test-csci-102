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


