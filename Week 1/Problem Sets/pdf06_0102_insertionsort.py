import random
import time
import matplotlib.pyplot as plt

def insertionSort(list_of_numbers):
   for i in range(1,len(list_of_numbers)):

     currentvalue = list_of_numbers[i]
     position = i

     while position > 0 and list_of_numbers[position-1] > currentvalue:
         list_of_numbers[position] = list_of_numbers[position-1]
         position = position-1

     list_of_numbers[position] = currentvalue

test_list1 = random.sample(range(1, 100), 10)
test_list2 = random.sample(range(1, 1000), 100)
test_list3 = random.sample(range(1, 10000), 1000)
test_list4 = random.sample(range(1, 100000), 10000)
list_of_tests = [test_list1, test_list2, test_list3, test_list4]
size = [10, 100, 1000, 10000]
insertion_time_taken = []

for each_list in list_of_tests:
    start = time.time()
    insertionSort(each_list)
    print(each_list)
    end = time.time()
    insertion_time_taken.append(end - start)
    print (insertion_time_taken)

test_list5 = random.sample(range(1, 100), 10)
test_list6 = random.sample(range(1, 1000), 100)
test_list7 = random.sample(range(1, 10000), 1000)
test_list8 = random.sample(range(1, 100000), 10000)
list_of_tests = [test_list5, test_list6, test_list7, test_list8]
python_time_taken = []

for each_list in list_of_tests:
    start = time.time()
    each_list.sort()
    print(each_list)
    end = time.time()
    python_time_taken.append(end - start)
    print (python_time_taken)

plt.subplot(2,1,1)
plt.plot (size, python_time_taken, 'o-')
plt.subplot(2,1,2)
plt.plot (size, insertion_time_taken, 'o-')
plt.show()
