# This script sorts a list of numbers in ascending order using the bubble sort algorithm.

my_list = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]  #swapping values at the same time
           
            
print("Sorted list:", my_list)