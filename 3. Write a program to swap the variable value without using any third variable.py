a = int(input("Enter any value a: "))
b = int(input("Enter any value b: "))

print("Original value is: ", a)
print("original value is: ", b)

a = a + b
b = a - b
a = a - b

# a, b = b, a

print("Swapped value is: ", a)
print("Swapped value is: ", b)
