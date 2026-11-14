

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

sparse = {}

print("Enter the matrix elements:")
for i in range(rows):
    for j in range(cols):
        value = int(input(f"Element [{i}][{j}]: "))
        if value != 0:
            sparse[(i, j)] = value


print("\nDictionary Representation of Sparse Matrix:")
print(sparse)


print("\nSparse Matrix:")
for i in range(rows):
    for j in range(cols):
        print(sparse.get((i, j), 0), end=" ")
    print()
