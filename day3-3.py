#take alist of sting 
#reverse each string and make a new list
#return a list of the reversed strings

# names =[
#     "Vaishnavi ",
#     "vishakharoy",
#     "Rani",
#     "himanshu"
# ]
# reversed_names = [name[::-1] for name in names]
# print(reversed_names)


# a =",".join(reversed("shiv"))
# print(a)

names =[
    "Vaishnavi ",
    "vishakharoy",
    "Rani",
    "himanshu"
]
# for i in names:
#     print(",".join(reversed(i)))
# print("human")

for i in range(0 , len(names)):
    # names[i] = names[i][::-1]
    names[i] = "".join(reversed(names[i]))  #//revesed in same list
print(names)