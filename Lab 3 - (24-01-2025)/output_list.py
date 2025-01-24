# Input for nested list `a`
print("Enter the nested list row by row. Type 'end' to stop:")
a = []
while True:
    row = input()
    if row.lower() == 'end':
        break
    a.append(list(map(int, row.split())))

# Input for list `b`
b = list(map(int, input("Enter the flat list of numbers separated by spaces: ").split()))

# Calculations
print("Number of sublists in a:", len(a))
print("Number of elements in b:", len(b))
print("Sum of elements in b:", sum(b))
