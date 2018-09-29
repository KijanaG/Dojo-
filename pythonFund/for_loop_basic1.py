#1) BASIC
for i in range(151):
    print(i)

#2) Multiples of Five
for elem in range(5,1000001,5):
    print(elem)

#3) Counting, the Dojo Way
for i in range(1,101):
    if i%5 == 0:
        print("Coding")
        if i%10 == 0:
            print("Dojo")
    else:
        print(i)

#4) Whoa. That Sucker's Huge
sum = 0
for i in range(500001):
    sum+=i
print(sum)

#5) Countdown By Fours
for i in range(2018,0,-4):
    print(i)

#6) Flexible Countdown
def flexible_countdown(lowNum, highNum, mult):
    while lowNum%mult != 0:
        lowNum+=1
    for i in range(lowNum,highNum+1,mult):
        print(i)
flexible_countdown(4,21,7)

list = [3,5,1,2]
for i in list:
    print(i)

