
pal=int(input("Enter a number:"))
temp=pal
rev=0
while(pal>0):
    dig=pal%10
    rev=rev*10+dig
    pal=pal//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")

