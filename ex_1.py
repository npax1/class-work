num1=int(input("ddtlb xbckj"))
num2=int(input("ddtlb xbckj 2"))
if num1>num2:
    num1,num2 = num2, num1
    while num1<=num2:
        if num1%2==1:
            print(num1)
        num1 += 1