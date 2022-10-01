start= int(input("start"))
end= int(input("end"))
temp=start
start=end
end=temp
while start>end:
    start-=1
    print(f"{start}")