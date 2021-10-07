class StudentData:
    rollList =[]
    namesList =[]
    idList=[]
    def getListData(obj):
        while 1:
            obj.rollList.append(input("Enter Roll num of student: "))
            obj.namesList.append(input("Enter student's name: "))
            obj.idList.append(input("Enter student's gmail: "))
            again = input("\nWanna make another entry? Y/N ")
            if again=="N" or again=="n":
                break

    def writeData(obj):
        try:    
            FileObj = open("newFile1.txt","a+")
        except:
            print("Invalid File")
            return
        
        dataLength  = len(obj.namesList)
        for x in range(0,dataLength):
            FileObj.write("\n"+obj.rollList[x]+" | "+obj.namesList[x]+" | "+obj.idList[x])
        FileObj.close()

        choice = input("Show data? Y/N")
        if choice == "Y" or choice=="y":
            obj.readData()

    def readData(obj):
        FileObj = open("newFile1.txt","r")
        print(FileObj.read())
        FileObj.close()

studentObj = StudentData()
studentObj.getListData()
studentObj.writeData()