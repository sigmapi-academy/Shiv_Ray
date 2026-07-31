st = ((101, 'Aman', 98),
      (102, 'Dipak', 82),
      (103, 'Raj', 76),
      (104, 'Shiv', 99),
      (105, 'Amit', 88))

print(f'\tRoll No.\tName\tMark')
for record in st:
    print(f'\t{record[0]}\t\t{record[1]}\t{record[2]}')