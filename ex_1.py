num=[]
num1=int(input("start"))
num2=int(input("end"))
while num1<=num2:
    num.append(num1)
    num+=1
    for i in num[::-1]:
        print(i)