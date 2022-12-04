fileContent = open("liczby.txt")
data = []
for line in fileContent:
    data.append(int(line.strip()))
singleAppearances = []
doubleAppearances = []
tripleAppearances = []
for value in data:
    if value not in tripleAppearances:
        if value in doubleAppearances:
            tripleAppearances.append(value)
            doubleAppearances.remove(value)
            singleAppearances.remove(value)
    if value not in doubleAppearances:
        if value in singleAppearances:
            doubleAppearances.append(value)
    if value not in singleAppearances:
            singleAppearances.append(value)
print(len(singleAppearances))
print(len(doubleAppearances))
print(len(tripleAppearances))
