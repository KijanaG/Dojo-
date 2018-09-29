def selection_sort(list):
    for i in range(len(list)):
        min = list[i]
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < min:
                min = list[j]
                min_index = j
        if list[min_index] == list[i]:
            continue
        list[min_index] = list[i]
        list[i] = min
        print(list)
selection_sort([532,621,12,-300,6,28,1960])
 