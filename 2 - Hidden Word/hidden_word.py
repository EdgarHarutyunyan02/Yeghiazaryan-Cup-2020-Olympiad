import csv

letters = [(17, 32), (23, 50), (29, 59), (35, 64),
           (42, 77), (48, 86), (56, 92), (62, 100)]

table = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i, col in enumerate(csv_reader):
        row_own = []
        for j, row in enumerate(col):
            row_own.append(row)
        table.append(row_own)


for letter_index in letters:
    print(table[letter_index[0]-1][letter_index[1]-1], end='')
