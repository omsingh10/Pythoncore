# remove all the punctuation from the text
import string
text = "self love is , ? is hsus, self"
txt = ""
for i in text:
    txt.replace(" ")
    if i not in string.punctuation:
        txt += i
print(txt)

