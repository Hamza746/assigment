# Write a Python function to check whether a number is completely divisible by another number.
# Accept two integer values form the user
a = int(input("put numerator:"))
b = int(input("put denuminator:"))
c = a%b
print(c)
if c==0:
    print("both numbers are completely divisible")
else:
    print("both numbers are not completely divisible")
