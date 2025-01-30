# Define the lists
a = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [1, 4, 8]

# Compute values
num_sublists = len(a)
num_elements_b = len(b)
sum_a = sum(sum(sublist) for sublist in a)  # Flatten and sum nested list
sum_b = sum(b)

# Print results with better formatting
print(f"Number of sublists in 'a': {num_sublists}")
print(f"Number of elements in 'b': {num_elements_b}")
print(f"Total sum of all elements in 'a': {sum_a}")
print(f"Total sum of all elements in 'b': {sum_b}")
