#some basic knowledge...
#what is a dictionary

#a dictionary is multiple datasets filled between a {} parenthesis

#defined in the format of key:value

# > cannot have two seperate values with the same key
# > cannot be duplicated using functions


#defining a dictionary
dict = {
  "brand": "Ford", #string
  "model": True, #bool
  "year": 1964, #int
  "cost": 500.5 #float
}
#printing all the contents in a dictionary

print(dict)

#empty dictionary
dict = {}
#usually used in init areas and data to be filled in later processes

#same like str() and int(), a dictionary variable can be created using the dict() function

dictionary = dict(name = "John", age = 36, country = "Norway")
print(dictionary)

#accessing items
x = dict["model"]
y = dict.get("model")
print(x)
print(y)

#getting keys
#method 1
keys_array = list(dict.keys())
print(keys_array)

#method 2
keys_array = []
for key in dict:
    keys_array.append(key)
print(keys_array)

#printing all the values
#method 1
x = list(dict.values())
print(x)

#method 2
values = []
for value in dict.values():
    values.append(value)
print(values)

#changing a specific value
dict["brand"] = "BMW"

#check if a key exists in a dictionary
if "model" in dict:
  print("Yes, 'model' is one of the keys in the dict dictionary")

#check if a value exists in a dictionary
if 1964 in dict.values():
  print("Yes, 'model' is one of the values in the dict dictionary")

#update value sets
thisdict.update({"year": 2020})
