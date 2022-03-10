print("PyCharm and Python")
a = [10,3,4,16,8]

print(a[:])
print(a[:3])
print(a[2])
print(a[-2])

# Update
b= [1,2,3,4]
b[1] = "One"

print("Value of array B : ",b)
"""
This is called random indexing: indexes starts with 0
This is called linear search O(N)
"""
maximum = a[0]

for num in a:
    if num > maximum:
        maximum = num

print(maximum)