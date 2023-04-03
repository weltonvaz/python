# Python 3 implementation of the above approach
 
from math import pow
 
# Function to print the smallest and largest
# palindrome with N digits
def printPalindrome(n):
    if (n == 1):
        print("Smallest Palindrome: 0")
        print("Largest Palindrome: 9")
    else:
        print("Smallest Palindrome:", int(pow(100000001, n - 1))+1)
        print("Largest Palindrome:", int(pow(100000001,n))-1)
     
 
# Driver Code
if __name__ == '__main__':
    n = 9
    printPalindrome(n)
 
# This code is contributed by
# Surendra_Gangwar