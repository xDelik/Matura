fileContent = open("liczby.txt", 'r')
data = []
for line in fileContent:
    data.append(int(line.strip()))

trojki = []
piatki = []
for i in range(0, len(data)):
    liczba1 = data[i]
    for j in range(0, len(data)):
        if i == j:
            continue

        liczba2 = data[j]
        if liczba2 % liczba1 != 0:
            continue

        for k in range(0, len(data)):
            if i == k or j == k:
                continue

            liczba3 = data[k]
            if liczba3 % liczba2 != 0:
                continue

            trojki.append([liczba1,liczba2,liczba3])

            for l in range(0, len(data)):
                if i == l or j == l or k == l:
                    continue

                liczba4 = data[l]
                if liczba4 % liczba3 != 0:
                    continue

                for w in range(0, len(data)):
                    if i == w or j == w or k == w or l == w:
                        continue

                    liczba5 = data[w]
                    if liczba5 % liczba4 != 0:
                        continue
                    piatki.append([liczba1, liczba2, liczba3, liczba4, liczba5])

        
print("Zadanie 4.3")
print("a)", len(trojki))
print("b)", len(piatki))

print("trojki.txt")
for trojka in trojki:
    print(trojka[0], trojka[1], trojka[2])