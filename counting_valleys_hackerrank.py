steps = int(input("Enter number of steps: "))
path = input("D->Down & U->Up: ")
upstep = 0
downstep = 0
final_upstep = 0
valley = 0
# for num,step in enumerate(path):
#     if step=="D":
#         downstep+=1    
#     if step=="U" and 'D' not in path[:num]:
#         final_upstep += 1
#     elif step=='U':
#         upstep +=1
#         if upstep-downstep==1:
#             final_upstep += 1
#             upstep=0
#             downstep=0
# print(final_upstep)  

for num,step in enumerate(path):
    if step=="U":
        upstep+=1
        if upstep-downstep==0:
            valley += 1
            upstep = 0
            downstep = 0
    if step=="D" and upstep>0:
        upstep-=1
    elif step=="D":
        downstep+=1  
print(valley)        