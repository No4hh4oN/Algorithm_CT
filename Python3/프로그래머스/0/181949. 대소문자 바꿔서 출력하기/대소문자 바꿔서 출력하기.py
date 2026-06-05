str = input()

listStr = list(str)

for i in range(len(listStr)):
    if listStr[i].isupper():
        listStr[i] = listStr[i].lower()
    else:
        listStr[i] = listStr[i].upper()
print(''.join(listStr))