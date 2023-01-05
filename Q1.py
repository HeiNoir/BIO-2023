def genFibo():
    x = 1
    y = 2
    finalList = [1,1,2]
    while x+y < 1000001:
        finalList.append(x+y)
        temp = x
        x = y
        y = temp + y
    return finalList


def genMaxZeck(num, fibolist):
    if num in fibolist:
        return num
    for i in range(len(fibolist)):
        if fibolist[i] < num:
            maxNum = fibolist[i]
        else:
            return maxNum


def findRemainingSum(num, inp):
    finalList = []
    while num > 0:
        finalList.append(inp[-1])
        num -= inp[-1]
        counter = len(inp)
        if num > 0:
            while True:
                if inp[counter-1] > num:
                    inp.pop()
                    counter-=1
                elif counter == len(inp)-1:
                    inp.pop()
                    break
                else:
                    break
    return finalList


if __name__ == "__main__":
    print("Yuri Zykov - Brighton College")
    inp = genFibo()
    choice_inp = int(input(">> "))
    out = genMaxZeck(choice_inp, inp)
    if out == choice_inp:
        print(out)
    else:
        newNum = choice_inp - out
        counter = len(inp)
        while True:
            if inp[counter-1] > newNum:
                inp.pop()
                counter-=1
            else:
                break
        out2 = findRemainingSum(newNum, inp)
        out2 = [str(x) for x in out2]
        newout = " ".join(out2)
        print(out, newout)
