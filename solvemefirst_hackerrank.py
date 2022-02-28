alice = input()
alice = alice.split()
bob = input()
bob = bob.split()
listt = [0,0]
for n in range(len(alice)):
    if int(alice[n])>int(bob[n]):
        listt[0] += 1
    elif int(alice[n])<int(bob[n]):
        listt[1] += 1    
print(listt[0],listt[1])        