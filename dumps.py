import json
x={
"name": "sakshi",
"age":22,
"country":"India",
"fav_colors":[{1:"Blue"},{2:"Pink"},{3:"White"},{4:"Black"}]
}
print(json.dumps(x));

#Parameters which are used in dumps function
#Dumps function converts object to the string
#4 parameters are used syntax is: dumps(name of the object,indent,separators,sort_key)
#indent defines the number of indents
#separators is used to separates the key form values by using separator symbol
#sort_key is used to ensure that the result is in sorting order or not

print(json.dumps(x,indent=4,separators=(". ", " = "),sort_keys=True))