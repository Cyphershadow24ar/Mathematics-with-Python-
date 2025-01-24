# Let x =[11,22,33] how to multiply it by 3 to get[33,66,99] ?

x = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
result = [i * 3 for i in x]
print("Result after multiplying by 3:", result)
