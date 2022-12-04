from math import fabs
fileContent = open("liczby.txt", 'r')
data = []
for line in fileContent:
    data.append(line.strip())

biggestDifference = 0
answerIndex = 0
for value in data:
    reverse = value[::-1]
    difference = abs(int(value) - int(reverse))
    if difference > biggestDifference:
        biggestDifference = difference
        answerIndex = data.index(value)
print(data[answerIndex], biggestDifference)