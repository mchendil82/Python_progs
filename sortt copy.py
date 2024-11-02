
#Python program to print a list 
# without using the sort() function
# without an extra variable
import time
start_time = time.time()

#l1=[4,2,7,3,6,1,5,3.5,2.1,2.9,2.6,0]
#l1=[76, 23, 45, 12, 54, 9] 
l1=[50, 31, 21, 28, 72, 41, 73, 93, 68, 43, 45, 78,5, 17, 97, 71, 69, 61, 88, 75, 99, 44, 55 ]
print("Original List:", l1)


# sorting list using nested loops
for i in range(0, len(l1)):
    print(l1[i])
    print("-----")
    for j in range(i+1, len(l1)):
        print(l1[j])
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
            print(l1)
    print("======")        
print("--- %s seconds ---" % (time.time() - start_time))