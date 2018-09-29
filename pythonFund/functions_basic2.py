#Countdown
def countdown(val):
    arr = []
    for i in range(val,-1,-1):
        arr.append(i)
    return arr 
a = countdown(7)
print(a)

#Print&Return
def print_and_return(list):
    print(list[0])
    return list[1]
b = print_and_return([5,6])
print(b)

#First Plus Length
def plus_length(list):
    return list[0] + len(list)
c = plus_length([3,4,5,6])
print("c is:", c)

#Values Greater Than Second
def values_greater2nd(list):
    newlist = []
    count = 0
    if len(list) == 1:
        return False
    for i in list:
        if i > list[1]:
            count+=1
            newlist.append(i)
    print(count)
    return newlist
a = values_greater2nd([4,5,6,7])
print(a)

#This Length, That Value
def this_length(val1, val2):
    newarr = []
    for i in range(val1):
        newarr.append(val2)
    if val1 == val2:
        print("Jinx!")
    return newarr
arr = this_length(8,8)
print(arr)

