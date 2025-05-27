text = input()

st = []
rev = ""

for i in text:
    st.append(i)

for i in range(0, len(text)):
    rev += st.pop()

print(rev)