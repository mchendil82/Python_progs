l=[1,2,4,5]
out=[[]]

#Under performance solution
#for each_element in l:
    #for each_subset in out:
        #out=out+ [each_subset+[each_element]]

#print(out)

#performance optimzed solution
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sset)
    
    def subsetsRecur(self, current, sset):
        if sset:
            print(current)
            print("**")
            print(sset)
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        print("---")
        print([current])  
        print("====") 
        return [current]


print(py_solution().sub_sets([1,2,3,4]))

#chendil's solution