# # Shopping_list = []
# # print(type(Shopping_list))

# list = []
# list.append("5")

# list.insert(0, "1")
# print(list)

# list.insert(0, "6")

# list.sort()
# print(list)

# a =list(range(0 , 10))
# print(a)

a =list(range(1 , 10))
b =list(range(11  , 20))

#how to join the lists
# c = a + b
# print(a+b)
a.extend(b)
print(a) # b didn't change a change
print(b)