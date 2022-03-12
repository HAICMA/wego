i=0
while i<100:
    i=i+1
    a=i%7
    b=(i-7)%10
    if a==0:
        continue
    if b==0:
        continue
    if 70<=i<80:
        continue
    print(i)