def getFileName():
    x=True
    try:
      FileName = input("Enter file name")
      File = open(FileName+".txt","r")
    except:
        x=False
    if(x==True):
        readFile(File)
    else:
        print("Invalid File")
    
def readFile(fileObj):
    print(fileObj.read())

getFileName()