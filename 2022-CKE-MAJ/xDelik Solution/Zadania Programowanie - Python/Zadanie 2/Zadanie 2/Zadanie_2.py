def findFactors(value):
    factors = []
    currentFactor = 2
    while value != 1:
        if value % currentFactor == 0:
            factors.append(currentFactor)
            value /= currentFactor
        else:
            currentFactor += 1
    return factors

fileContent = open("liczby.txt", 'r')
data = []
for line in fileContent:
    data.append(line.strip())

maxFactors = 0
maxFactorsIndex = 0

maxDistinctFactors = 0
maxDistinctFactorsIndex = 0

for value in data:
    factors = findFactors(int(value))
    if len(factors) > maxFactors:
        maxFactors = len(factors)
        maxFactorsIndex = data.index(value)
    if len(list(set(factors))) > maxDistinctFactors:
        maxDistinctFactors = len(list(set(factors)))
        maxDistinctFactorsIndex = data.index(value)

print(data[maxFactorsIndex], maxFactors, data[maxDistinctFactorsIndex], maxDistinctFactors)