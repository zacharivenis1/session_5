for i in range(1, 10, 2):
    print(i)

s = 0
for i in range(1, 11):
    s += i
    # s = s + i
print(s)

s = 0
i = 1
while i <= 10:
    s += i
    i += 1 # this will break the loop!!
print("sum using while is also", s)
