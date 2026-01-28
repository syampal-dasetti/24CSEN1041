a = 20
b = 10

# Arithmetic Operators
print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")   # Float division for clarity
print(f"{a} % {b} = {a % b}\n")

# Relational Operators
print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")

# Logical Operators
print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")

# Bitwise Operators
print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")

# Conditional (Ternary) Operator
print("\n" + ("a is greater than b" if a > b else "b is less than a"))
#output
Arithmetic Operators
20 + 10 = 30
20 - 10 = 10
20 * 10 = 200
20 / 10 = 2.00
20 % 10 = 0

Relational Operators
20 < 10 = False
20 > 10 = True
20 == 10 = False
20 != 10 = True

Logical Operators
AND 20 and 10 = True
OR 20 or 10 = True
NOT 20 = False

Bitwise Operators
20 & 10 = 0
20 | 10 = 30
Bitwise XOR 20 ^ 10 = 30
Left Shift 20 << 2 = 80
Right Shift 20 >> 2 = 5

a is greater than b

=== Code Execution Successful ===
