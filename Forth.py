# dict = {
#      "name" : "Falsi",
#      "sub" : ["c","python","java"],
#      "topic " : ("set","tuple"),
#      "age" : 20,
#      "is_adult" : True
# }
# print(dict)
# print(dict["age"])
# print(dict["is_adult"])
# print(dict["sub"])
# dict["name"] = "aayu"
# dict["surname"] = "vadaliya"
# print(dict)

# null_dict = {}
# null_dict["name"] = "falsi"
# print(null_dict)

#nested dic
# student = {
#      "name" :  "shivu",
#      "sub" : {
#           "maths" : 99,
#           "science" : 92,
#           "english" : 90
#      }
# }
# print(student)
# print(student["sub"]["maths"])
# print(list(student.keys()))
# print(list(student.values()))
# print(tuple(student.items()))

# print(student["name1"])      #error
# print(student.get("name1"))       #give the none as output

# student.update({"city":"rajkot"})
# print(student)


#set 
# collection = {1,2,3,"hello","world"}
# print(collection)
# print(type(collection))
# print(len(collection))

#empty set
# collection = set()
# print(type(collection))

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add(3)
# collection.add("hello")
# collection.remove(3)
# # collection.clear()
# collection.pop()         #random pop thai 
# print(collection)

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))


#practice
# dict = {
#      "table" : ["a piece of furniture","a list of facts"],
#      "cat" : "a small animal "
# }
# print(dict)

# subjects = {"python","java","c++","python","js","python","java","java","c++","c"}
# print(subjects)

# mark = {}
# x = input("enter maths:")
# y = input("enter phy:")
# z = input("enter che:")
# mark.update({"maths": x})
# mark.update({"phy": y})
# mark.update({"che": z})
# print(mark)

# value = {9,"9.0"}
# print(value)                                                                        

# value = { ("int",9), ("float",9.0)}
# print(value)
