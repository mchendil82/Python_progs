import time
start_time = time.time()
#ms=[4,2,7,3,6,1,5,3.5,2.1,2.9,2.6,0]
#ms=[15,1777,99,555,1,232,905]
#ms=[76, 23, 45, 12, 54, 9]
ms=[50, 31, 21, 28, 72, 41, 73, 93, 68, 43, 45, 78,5, 17, 97, 71, 69, 61, 88, 75, 99, 44, 55 ]
sortsbs=[ms[0]]

for msi in range(1,len(ms)):
    print(ms[msi])
    for sortsbsi in range(0,len(sortsbs)):        
        if ms[msi] < sortsbs[sortsbsi]:
            print("***")
            #sortsbs.insert(sortsbsi,ms[msi])
            #sortsbs[sortsbsi]=ms[msi]
            sortsbs.insert(sortsbsi,ms[msi])
            #sortsbs[sortsbsi+1]=sortsbs[sortsbsi]
            print(sortsbs)
            break
        elif sortsbsi == len(sortsbs)-1:
            sortsbs.insert(sortsbsi+1,ms[msi])

print("--- %s seconds ---" % (time.time() - start_time))
print(sortsbs)

#0.0002980232238769531 seconds
#--- 0.002730846405029297 seconds ---












    
#[5, 17, 21, 28, 31, 41, 43, 44, 45, 50, 55, 61, 68, 69, 71, 72, 73, 75, 78, 88, 93, 97, 99]
#[5, 17, 21, 28, 31, 41, 43, 44, 45, 50, 55, 61, 68, 69, 71, 72, 73, 75, 78, 88, 93, 97, 99]











    

    



   

