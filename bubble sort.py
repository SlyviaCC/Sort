import random
def bubble_sort(data):
    for i in range(len(data) - 1):# The outer loop increases the ordered number by one each time
        indicator = False # For optimization (no exchange indicates ordered, end cycle)
        for j in range(len(data) - 1 - i):#The maximum value in each of the inner loops in the disordered section is placed at the top
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                indicator = True
        if not indicator:#If there is no exchange the list is already organized, end the loop
            break
# test
data = list(range(10))#Produces an ordered list
random.shuffle(data) # Call the shuffle function to disrupt the order
print(data)# sort before
bubble_sort(data)# Call the bubbling sorting algorithm
print(data)#sorted after