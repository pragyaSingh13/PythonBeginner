print("Enter  your password: ")
passw=input()
numofno = 0
numofchar = 0
numofspe =0

for x in passw:
    if x>='A' and x<='Z':
      numofchar+=1
    elif x>='a' and x<='z':
        numofchar+=1
    elif x>='0' and x<='9':
        numofno+=1
    else:
        numofspe+=1
  
print(numofno)
print(numofchar)
print(numofspe)

