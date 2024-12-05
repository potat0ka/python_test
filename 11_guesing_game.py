i=0
top:
if(i<100):
    print(i+1)
    i=i+1
    print("\n")
    goto top



i = 0
while i < 100:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1
