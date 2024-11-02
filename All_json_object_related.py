#https://www.educative.io/edpresso/what-is-the-difference-between-jsonloads-and-jsondumps
#Example json.loads()
#In this example, a *****string is converted into a json object, USING JSON LOADS**** and the key age is accessed in that json object:
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y)

#Example json.dumps()
#In this example, *****a json object is passed in the json.dumps() function******, and its data is extracted and returned in the form of a string:
import json
a = {'lalalala': 3}
myString = json.dumps(a)
print (type(myString))
print (myString)


####Json loads vs load
#json.load() takes a FILE
#json.load() expects a file (file object) - e.g. a file you opened before given by filepath like 'files/example.json'.

#json.loads() takes a STRING
#json.loads() expects a (valid) JSON string - i.e. {"foo": "bar"}

with open("./jsonload_loads.txt", "r") as  content:
    print(json.load(content))
    #print(json.loads(content.read())) #Note: YOU CAN'T DOUBLE SERLIAZE AN FILE OBJECT WHICH ALREADY OPENED IN READ ONLY AND IT IS ALREADY DESRIALIZED 

with open("./jsonload_loads.txt", "r") as  content:
    print(json.loads(content.read()))


#json.load actually calls json.loads and use fp.read() as the first argument.

#So if your code is:

file="./jsonload_loads.txt"

with open (file) as fp:
    content = fp.read()
    print(json.loads(content))

###It's the same to do this:

with open (file) as fp:
    print(json.load(fp))

