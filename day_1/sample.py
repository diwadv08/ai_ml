# print("Diwakar")
# b="Hello"
# print(b)
# b=1
# print(b)
# b=False
# print(b)

name="Hari"
# age=25
# mobile_number=9489460029
# place="Trichy"
# print(name,place)
# print(name+" from "+place)

# myint = 7
# print(myint)
# myfloat = 7.0
# print(myfloat)
# myfloat2 = float(myint)
# print(myfloat2)
# mystring = 'hello'
# print(mystring)
# mystring = "hello"
# print(mystring)
# mystring = "Don't worry about apostrophes"
# print(mystring)

# one = 1
# two = 2
# three = one + two
# print(three)
# hello = "hello"
# world = "world"
# helloworld = hello + " " + world
# print(helloworld)

#Insted of this
# a=3
# b=5
# print(a,b)

#Use This
# a, b = 3, str(5)
# print("A"+b)

# one = 1
# two = 2
# hello = "hello"
# print(str(one) +"--"+ str(two) +"--"+hello)

# mystring = "hello"
# myfloat = None
# myint = None

# # testing code
# if mystring == "hello":
#     print("String: %s"%mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float: %f"%myfloat)
# if isinstance(myint, int) and myint == 20:
#     print("Integer: %d"%myint)
# print("String") if isinstance(mystring,str) else print("Not a String")


# new_list=[name,"Ajay","Karun"]
# new_list.append("Arun")
# new_list.append("Akash")
# myString="--".join(new_list)
# new_list[0]
# print(new_list)
# print(myString)
# print(f"Hello World My name is '{new_list[0]}'")


# empty_list = []
# numbers = [1, 2, 3]
# mixed = [1, "apple", True, 3.14]
# nested = [[1, 2], [3, 4]]
# list_from_range = list(range(5))  # [0, 1, 2, 3, 4]
# list_from_string = list("python")  # ['p','y','t','h','o','n']
# print(mixed)
# print(nested[0])
# print(list_from_range)
# print(list_from_string)



# List Methods
# nums = [10, 20, 30, 40, 50]
# print(nums[0])      # 10 (first element)
# print(nums[-1])     # 50 (last element)
# print(nums[1:4])    # [20, 30, 40] From 1 Position Excluding 4 th Position so 1,2,3
# print(nums[::-3])   # [50, 40, 30, 20, 10] (reversed)
# lst = [1, 2]
# print(lst)
# lst.append(3)           
# print(lst)
# lst.insert(2, 15)        
# print(lst)
# lst.extend([7, 8]) 
# print(lst)
# lst.remove(15)           
# print(lst)
# lst.pop()               
# print(lst)
# lst.pop(2)
# print(lst)              
# del lst[1]              
# print(lst)
# lst.clear()            
# print(lst)
# lst = [1, 2, 3]
# print(lst)
# lst.insert(0,29)
# lst[1] = 10              # [1, 10, 3]
# print(lst)
# lst[0:2] = [7, 8]        # [7, 8, 3]
# print(lst)

# nums = [3, 1, 4, 2]
# print(nums)
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)

# lst = [1, 2, 3, 2]
# print(lst.count(2))       
# print(lst.index(1))       
# print(lst)
# copy_lst = lst.copy() 
# print(copy_lst)
# for x in range(100,1001,100):
#     print(str(x)) if x==1000 else print(str(x),end=",")
# # squares =[x for x in range(100,1000+1,100)]     
# # print(squares)
# # even = [x for x in range(1,5,2) if x % 2 == 0]
# # print(even)
# nested = [[i+j*2 for j in range(5)] for i in range(3)]
# print(nested)

# lotsofhellos = "hello" * 3
# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = [even_numbers] + [odd_numbers]
# print(all_numbers)
# print(lotsofhellos)
# print([1,2,3] * 3)


x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")