import json

#parse json - convert from json to python

#some json
x = '{"name":"John","age":30,"city":"New York"}'
#parse x:
y = json.loads(x) #json -> dictionary

#the result is a python dictionary:
print(y["age"])

x = json.dumps(y,indent=1, separators=(". "," = "),sort_keys=True) #dictionary(any py datatype) -> json

print(x)