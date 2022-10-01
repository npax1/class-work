start=int(input("веди число і"))
end=int(input("веди число"))
if start%2!=0:
    start+=1
while start<end:
    print(f'{start}')
    start +=2