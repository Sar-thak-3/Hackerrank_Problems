# Modified Kaprekar Numbers ---> Hackerrank
num1 = int(input())
num2 = int(input())
kaprekar_list= []
def kaprekar(num1,num2):
    for num in range(num1,num2):
        numlen = len(str(num))
        square_num = num**2
        reverse = (str(square_num))[::-1]
        reverse = [reverse[:numlen],reverse[numlen:]]
        act_reverse = []
        for itm in reverse:
            newitm = itm[::-1]
            act_reverse.append(newitm)
        reversed = list(map(lambda x:int(x),act_reverse))
        if sum(reversed)==num:
            kaprekar_list.append(num)
if num1<=3:
    if num1<=1: kaprekar_list.append(1)
    kaprekar(4,num2+1) 
else:
    kaprekar(num1,num2+1)            

if len(kaprekar_list)==0:
    print("INVALID RANGE")
else:
    for x in kaprekar_list:
        print(x,end=" ")
