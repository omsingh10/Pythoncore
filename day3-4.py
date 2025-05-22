# text ="self love is gay "
# words=text.split()
# words.reverse()
# print(" ".join(words))
# print(words)

#swap the first and last elements of a list
# text = [ 100 , 200 , 300 , 400 , 500 ]
# print(text)
# print(text[0] , text[-1])
# print(text[-1] , text[0])

# text[0] , text[-1] = text[-1] , text[0]
# print(text)

# Swap the  first word and last word of a string
# text = "self is love"
# words = text.split()
# print(words)
# print(words[0] , words[-1])
# words[0] , words[-1] = words[-1] , words[0]
# print(words)
# print(" ".join(words))


#input mr ding  output= rm gnid
text = "mr ding"
words = text.split()
for i in range(len(words)):
         words[i] = "".join(reversed(words[i])) 
        
print(words)
print(' '.join(words))

