#basic questions in strings

#Program to Find Length of a String (Without len())
s=input("enter the string : ")
count=0
for ch in s:
 count+=1

print("lenght",count)
#output
enter the string : IUEFWUIBVKJBHKKHKBJKJNJBKDHHKUHKIFBJBK BBJKHJBKJFFBHJZ,,.YYYYYYYUIOKJNV BYHB FVHJNM SDYHJN XYUHJNSDYJHN
lenght 103

#Program to Reverse a String
s=input("Enter the string : ")
rev=""
for ch in s:
    rev=ch+rev
    
print("reverse",rev)

#output
Enter the string : syamapal
reverse lapamays

#Program to Check Palindrome
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#output
Enter a string: syampal
Not Palindrome

#Program to Count Vowels in a String
s = input("Enter a string: ")

count=0
for ch in s:
    if ch in 'aeiouAEIOU':
     count+=1
    
print("no of vowels",count)

#output
Enter a string: syampal
no of vowels 2


