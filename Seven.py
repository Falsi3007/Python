#read file
# f = open("demo.txt","a")
# data = f.read()
# print(data)
# f.close()

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)

#writing file 
# f.write("i am aayu")
# f.close()

# f = open("sample.txt","a")
# f.close()

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     data = f.write("new data")

#deleting file
# import os
# os.remove("sample.txt")


#practice
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\n we are learning file i/o\n using java\n i like programming in java.")

# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)
# new_data = data.replace("java","python")
# print(new_data)

# def find_char():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("done!!!")
#         else:
#             print("not founded")
# find_char()

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#             line_no+=1
# check_for_line()

count =0
with open("practice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count+=1
print(count)
