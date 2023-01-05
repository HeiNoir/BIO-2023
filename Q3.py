from collections import deque


def check(startPos, endPos):
    maxDistance = 0
    checker = set()
    queue = deque([(startPos, 0)])
    while True:
        position, distance = queue.popleft()
        if distance > maxDistance:
            maxDistance = distance

        newPositions = findPossibleMoves(position)

        for i in range(len(newPositions)):
            if newPositions[i] == endPos:
                return maxDistance + 1
            joinedPosition = " ".join(newPositions[i])
            if joinedPosition not in checker:
                checker.add(joinedPosition)
                queue.append((newPositions[i], maxDistance+1))


def swapPegs(l, fromX, toY):
    finDigit = (l[fromX])[-1:]
    l[fromX] = (l[fromX])[:-1]
    l[toY] += finDigit
    for j in range(4):
        if "0" in list(l[j]):
            l[j] = list(l[j])
            l[j].remove("0")
            l[j] = "".join(l[j])
    for i in range(4):
        if l[i] == "":
            l[i] = "0"
    return l


def findPossibleMoves(l):
    finalList = []
    origList = []
    for a in range(len(l)):
        origList.append(l[a])
    for i in range(len(l)):
        for j in range(len(l)):
            if len(l[j]) != 4 and i != j:
                newList = swapPegs(origList, i, j)
                if newList not in finalList:
                    finalList.append(newList)
                origList = []
                for b in range(len(l)):
                    origList.append(l[b])

    return finalList


if __name__ == "__main__":
    print("Yuri Zykov - Brighton College")
    inp = input(">> ")
    inp2 = input(">> ")
    split_inp = inp.split(" ")
    split_inp2 = inp2.split(" ")
    if inp == inp2:
        print(0)
    elif len(inp) >= 19:
        print(0)
    else:
        out = check(split_inp, split_inp2)
        print(out)

