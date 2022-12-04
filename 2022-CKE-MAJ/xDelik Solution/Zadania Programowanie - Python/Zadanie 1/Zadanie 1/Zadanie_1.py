fileContent = open("liczby.txt", 'r')
data = []
for line in fileContent:
    data.append(line.strip())

firstValue = "";
count = 0
for value in data:
    if value[0] == value[-1]:
        if firstValue == "":
            firstValue = value
        count += 1
print(count, firstValue)