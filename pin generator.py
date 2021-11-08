digits = int(input())
ceiling = ""
for i in range(1,digits+1) :
    ceiling = "9" + ceiling
ceiling = int(ceiling)
print(ceiling)
with open("pin.txt","a") as file :
    file.truncate(0)
    for i in range(0,ceiling+1) : 
        print(str(i).zfill(digits))
        file.writelines(str(i).zfill(digits) + '\n')
        i += 1
    file.close()
