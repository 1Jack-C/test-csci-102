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


def ScoreFinder(players, scores, name):
    name = name.upper()
    index = 0
    newplayers = []
    for player in players:
        newplayers.append(player.upper())
    if name in newplayers:
        for a in newplayers:
            if a == name:
                newindex = index
            index = index + 1
        print("OUTPUT", players[newindex], "got a score of", scores[newindex])
    else:
        print("OUTPUT player not found")


def Union(list1, list2):
    output = []
    for a in list1:
        output.append(a)
    for a in list2:
        output.append(a)
    return output

def Intersection(list1, list2):
    out = []
    for a in list2:
        if a in list1:
            out.append(a)
    return out

print(Intersection(['Adam','Janet','liam',"Kai"], [12,7,"Adam","Kai"]))