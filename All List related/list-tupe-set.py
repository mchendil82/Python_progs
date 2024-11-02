#tupleas are hetrogenous, immutable(CANNOT add or detele or change it another type),allows, duplicate element. symbol(), ordered collections- i.e. isreturn how we passed
t=tuple()

t=("1","3","4",5)
print(t)

s=set()
s=("1",2)
print(s)
#sets are hetrogenous, mutable(CAN add or detele or change it another type),allows, Doesn't allow uplicate element. symbol{}, Un-ordered collections-i.e. is returns baed on sorting
s1={1,3,4,5}
s2={1,2,3,4,5}
s3=s2-s1
print(s3.__len__())
#lists are hetrogenous, mutable(CAN add or detele or change it another type),allows, allows uplicate element. symbol[],  ordered collections-return how we passed
l=['1','2']
#to get index use enumerate function for list
for index, valure in enumerate(l):
    print("index is {} and the value {}".format(index, valure))

#Dict are key pari values and obvisouly, they are hetrogenous, mutable(CAN add or detele or change it another type),allows, allows duplicate element. symbol{},  ordered collections-i.e. is return how we passed
d = {'key1': 1, 'key2': 2, 'key3': 3}
for k in d.keys():
    print(k)
for v in d.values():
    print(v)

for k,v in d.items():
    print("Keys:{} and its value:{}".format(k,v))