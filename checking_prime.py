num = int(input("Enter number: "))
i = 2
flag = 0

while i <= num // 2:
    if num % i == 0:
        flag = 1
        break
    i += 1

if flag == 0 and num > 1:
    print("Prime")
else:
    print("Not Prime")
#output
Enter number: 81
Not Prime

=== Code Execution Successful ===
