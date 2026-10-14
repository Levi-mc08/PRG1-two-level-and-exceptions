scores = [[78, 81, 84],
          [55, 54, 62],
          [89, 71, 90],
          [80, 75]]

print(scores[1][2])
print(len(scores))
print(len(scores[0]))

print("---")

for row in scores:
    print(row)

print("---")

for row in scores:
    for mark in row:
        print(mark)

print(scores[1])
for row in scores:
    print(row[0])
total_second_row = 0
for mark in scores[1]:
    total_second_row += mark
print(total_second_row)