
def chkPallin(s):
    a=s
    rev=a[::-1]
    if(s==rev):
        print(s," is a palindrome")
    else:
        print(s," is not a palindrome")

a=input("Enter String to check: ")
chkPallin(a)