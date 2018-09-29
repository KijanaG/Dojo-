#Biggie Size
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "Biggie"
    return list
a = biggie_size([5,1,-2,-3,0])
print(a)

#Count Positives
def countplus(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count +=1
    list[len(list)-1] = count
    print(list)
    return list
countplus([-2,3,-5,3,1])

#Sum Total
def sum_total(list):
    sum = 0
    for i in list:
        sum+=i
    print(sum)
    return sum
sum_total([5,4,3,2,1])

#Average
def average(list):
    sum = 0
    for i in list:
        sum+=i
    avg = sum/len(list)
    print(avg)
    return avg
average([5,4,3,2,1])

#Length
def length(list):
    return len(list)
print(length([4,5,6,7]))

#Minimum
def mini(list):
    print(min(list))
    return min(list)
mini([4,3,2,1,6,0])

#Maximum
def maxi(list):
    print(max(list))
    return max(list)
maxi([4,3,2,1,6,0])

#UltimateAnalyze
def ultimate(list):
    sum = 0
    for i in list:
        sum+=i
    avg = sum/len(list)
    return {
        "sumTotal": sum,
        "average": avg,
        "minimum": min(list),
        "maximum": max(list),
        "length": len(list)
    }
A = ultimate([1,2,3,4,5,6,7,8,9])
print(A)

#Reverse List
def reverse(list):
    list.reverse()
    print(list)
    return list
reverse([1,2,3,4,5,6])
