number_of_terms = int(input("Enter the number of terms (greater than 2): "))


fibonacci_1 = 0
fibonacci_2 = 1


fibonacci_3 = fibonacci_1 + fibonacci_2


print("Fibonacci Series:")
print(fibonacci_1)
print(fibonacci_2)


i = 3
while i <= number_of_terms:
    print(fibonacci_3)
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3
    fibonacci_3 = fibonacci_1 + fibonacci_2
    i += 1

#output
Enter the number of terms (greater than 2): 5
Fibonacci Series:
0
1
1
2
3

=== Code Execution Successful ===
