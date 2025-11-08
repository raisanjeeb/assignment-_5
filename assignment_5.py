# 1
#(take n input)
n = int(input("Enter number of items: "))

#(list to store the elements)
fruits = []

#(looping for n numbers of items)
for i in range(n):
    item = input("Enter item: ")
    fruits.append(item)
# Print the final list
print("Your list:", fruits)
# Ask user what they want to search
search_item = input("What do you want to search: ")
# Find and print the position using for loop and enumerate
found = False
for index, item in enumerate(fruits):
    if item == search_item:
        print(f"{search_item} is in {index} position.")
        found = True
        break
if not found:
    print("Item not found in the list.")
  




