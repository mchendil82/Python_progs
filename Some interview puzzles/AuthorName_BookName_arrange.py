#Create dict by author name from existing list

bookslist={'A' : 'chendil', 'C': 'mani', 'D': 'chendil', 'F': 'sathya', 'E': 'chendil'}
newbooklist={}

for booknamekey, authornamevalue in bookslist.items():
    try:
        newbooklist[authornamevalue]= newbooklist[authornamevalue]+","+booknamekey
    except KeyError:
        newbooklist.update({authornamevalue: booknamekey})    


print(newbooklist)    