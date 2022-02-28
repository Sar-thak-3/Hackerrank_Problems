from tkinter import N


time = int(input())
n = time
for i in range(0,n):
    for m in range(3*(2**i),0,-1):
        print(m)
        time-=1
        if time==0:
            val = m
            break
    if time==0:
        break
print(val)