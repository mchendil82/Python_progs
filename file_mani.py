import requests, json

f='https://searchconsole.googleapis.com/$discovery/rest?version=v1'
response=requests.get(f)
#print(response.content.decode(encoding='UTF-8'))
resp_dict=json.loads(response.content.decode(encoding='UTF-8'))
methods=resp_dict["resources"]["sites"]["methods"]
methods_ser=json.dumps(methods)
print(type(methods_ser))








#with open(f, 'r') as content:
 #   print(content)Hi D