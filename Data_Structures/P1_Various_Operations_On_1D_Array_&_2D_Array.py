# Initialize a 1D array
arr = [4, 2, 7, 1, 9, 5]
# Traversing/Displaying the array
for element in arr:
    print(element, end=' ')
# Adding elements
arr.append(8)  # Adds 8 at the end
arr.insert(2, 3)  # Inserts 3 at index 2
# Deleting elements
arr.remove(7)  # Removes the first occurrence of 7
del arr[3]  # Removes element at index 3
# Searching for an element
element_to_search = 9
if element_to_search in arr:
    print(f'{element_to_search} found at index {arr.index(element_to_search)}')
else:
    print(f'{element_to_search} not found')
# Output: 9 found at index 4
# Sorting
arr.sort()  # Sorts in ascending order
# Updated array: [1, 2, 3, 4, 5, 8, 9]
# Merging arrays
arr2 = [6, 0, 11]
merged_arr = arr + arr2

#b) various operations on 2D array .
# Initialize a 2D array
arr_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Traversing/Displaying the 2D array
for row in arr_2d:
    for element in row:
        print(element, end=' ')
    print()
# Accessing elements
element = arr_2d[1][2]  # Accessing element in 2nd row, 3rd column (6)
print(f"Element at (1, 2): {element}")  # Output: Element at (1, 2): 6
# Adding a row
new_row = [10, 11, 12]
arr_2d.append(new_row)
# Adding a column
new_column = 13
for row in arr_2d:
    row.append(new_column)
# Deleting a row
del arr_2d[2]  # Deletes the third row
# Deleting a column
for row in arr_2d:
    del row[1]  # Deletes the second element in each row
# Searching for an element
element_to_search = 6
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        if arr_2d[i][j] == element_to_search:
            print(f'{element_to_search} found at position ({i}, {j})')
            break
# Sorting rows (you can sort based on specific criteria)
arr_2d.sort(key=lambda x: x[0])  # Sorts based on first element in each row

