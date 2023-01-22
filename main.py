def myfib():
    x = 0
    counter = 0
    myarray = []
    while -1 < x < 4920:
        print(x, end=" ")
        myarray.append(x)
        if x < 1:
            x += 1
        x += myarray[counter - 1]
        counter += 1

myfib()
