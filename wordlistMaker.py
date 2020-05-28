import os.path

lst = []

def display(s, n, num) :
    if n != num :
        for i in lst :
            display(s+i, n+1, num)
    else :
        for i in lst :
            print(s+i)

def create(s, n, num, fh) :
    if n != num :
        for i in lst :
            create(s+i, n+1, num, fh)
    else :
        for i in lst :
            fh.write(s+i+"\n")

def cleanList() :
    i = 1
    while i < len(lst) :
        j = 0
        while j < i :
            if lst[j] == lst[i] :
                del lst[j]
                j = j - 1
                i = i - 1
            j = j + 1
        i = i + 1

def noFile(lb, ub) :
    i = lb
    while i <= ub :
        display("", 1, i)
        i = i + 1

def initiate(lb, ub, fh) :
    i = lb
    while i <= ub :
        create("", 1, i, fh)
        i = i + 1

if __name__ == "__main__" :

    slices = (input("Enter the range and elements : ").strip()).split()
    print(slices)
    
    for i in slices[2] :
        lst.append(i)
    
    cleanList()
    print(lst)

    print("Enter the name of the file you wish the output to be stored.\nIf you do not wish to create a file just leave it blank, in doing so the output generated will be displayed here.")
    f = input("Enter file name : ")

    if f == "" :
        print("Writing in file...")
        noFile(int(slices[0]), int(slices[1]))

    else :

        f = f + ".txt"

        if os.path.isfile(f) :

            choice = input("Do you want to overwrite the file ? (y/n) : ")

            if choice == "y" or choice == "Y" :
                fh = open(f, "w")
            else :
                fh = open(f, "a")

        else :
            fh = open(f, "w")

        print("Writing in file...")
        initiate(int(slices[0]), int(slices[1]), fh)

        print("Done")
