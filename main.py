import os

def findLine():
    a=input("enter a song: ")
    b=".txt"
    song=a+b
    try:
        f = open(song, "r")
        n=input("Enter a line: ")
        if n.isnumeric():
            n=int(n)
            for i in range(0,n-1):
                f.readline()
            print(f.readline())
        else:
            os.system('cls')
            print("wrong input, try again")
            findLine()
    except:
        print("not defined, try again")
        findLine()


def restart():  
    start=input("do you wont to search another line? y/n: ")
    if start=="y":
        os.system('cls')
        main(start)
    elif start=="n":
        exit()
    else:
        print("wrong input, try again")
        restart()



def main(start):
    while start=="y":
        findLine()
        restart()
        

os.system('cls')
main("y")


