def isPrime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

fileContent = open("liczby.txt")
data = []
for line in fileContent:
    data.append(line.strip())
for value in data:
    reverse = value[::-1]
    if isPrime(int(value)) and isPrime(int(reverse)):
        print(value)