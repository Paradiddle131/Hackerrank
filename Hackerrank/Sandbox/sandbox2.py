# parts = [['h', 'a', 'v', 'e'], ['a', 'n', 'i', 'c'], ['e', 'd', 'a', 'y']]
parts = [['f', 'e', 'e', 'd'], ['t', 'h', 'e', 'd'], ['o', 'g']]
for x, y, z in zip(*parts):
    print(x, y, z)
print("-----")

string3 = ""
listPicked = []
for i in range(len(parts)+1):
    for x in parts:
        if i < len(x[i]):
            pass
        else:
            print(x[i], end ='')
            string3 += x[i]
            listPicked.append(x[i])
            if x == parts[len(parts)-1]:
                listPicked.append(x[i])
                string3 += " "
print("\nlistPicked: ", listPicked)
print("string3: ", string3)