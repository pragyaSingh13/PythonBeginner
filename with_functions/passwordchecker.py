def countChar(password):
    counterList = [0,0,0,0]
    for ch in password:
         if ch>='A' and ch<='Z':
             counterList[0]+=1
         elif ch>='a' and ch<='z':
             counterList[1]+=1
         elif ch>='0' and ch<='9':
             counterList[2]+=1
         else:
              counterList[3]+=1
    return counterList

print("Please Enter Your Password:")

password = input()
counterList = countChar(password)

print(counterList[0], ", Capital Letters")
print(counterList[1], ", Small Letters")
print(counterList[2], ", Numbers")
print(counterList[3], ", Special Characters")

    

