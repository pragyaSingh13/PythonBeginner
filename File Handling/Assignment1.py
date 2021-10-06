myFile = open("newFile.txt","a+")

def fun():
    str=""
    print("Write about yourself, write stop in new line to quit and save: ")
    while str!="stop":
        str = input()
        if(str=="stop"):
            break
        myFile.write(str+"\n")
    myFile.close()


fun()