n = int(input("Enter the number of elements in the array: "))
numbers = []
print("Enter the elements")
for i in range(n):
 num = int(input())
numbers.append(num)
e = int(input("Enter the element to search: "))
found = False
low = 0
high = n - 1
index = -1
while low <= high:
  mid = (low + high) // 2
if numbers[mid] == e:
  found = True
  index = mid
  break
elif numbers[mid] < e:
  low = mid + 1
else:
  high = mid - 1
if found:
 print("Element", e, "found at index", index)
else:
 print("Element", e, "not found in the array.")