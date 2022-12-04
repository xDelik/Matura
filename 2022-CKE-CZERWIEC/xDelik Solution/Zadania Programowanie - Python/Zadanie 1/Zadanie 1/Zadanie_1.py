fileContent = open("liczby.txt")
data = []
for line in fileContent:
    data.append(line.strip())

for value in data:
    reverse = value[::-1]
    if int(reverse) % 17 == 0:
        print(reverse)