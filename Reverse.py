num = 156
copy = num
rev = 0
while copy != 0:
    digit = copy % 10
    rev = rev * 10 + digit
    copy //= 10
print(rev)
