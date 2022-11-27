# str1 = input()
# str2 = input()
# print(str1.count(str2) or str2.count(str1))

str1 = input()
str2 = input()
if str1 < str2:
    str2, str1 = str1, str2
i = 0
c = 0
while i < len(str2):
# for i in range(len(str1) - len(str2) + 1):
    if str1[i: i + len(str2)] == str2:
        c += 1
        i += len(str2)
    else:
        i += 1
print(c)