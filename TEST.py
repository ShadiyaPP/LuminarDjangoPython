lst = [1,2,3,4]
low = 0
up = len(lst)-1
elem = int(input('Enter the sum:'))
while(low<up):
    sum = lst[low]+lst[up]
    if sum==elem:
        print(lst[up],lst[low])
        break
    elif sum>elem:
        up-=1
    else:
        low+=1
