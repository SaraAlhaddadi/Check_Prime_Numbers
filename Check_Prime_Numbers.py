#Prepared by:Shvm-k

print("\t\tWelcome\n","This program will help you to check if the number you will enter it prime or not\n")

x=1#these lines to chech if user enter a number or not and make him try agian
while(x==1):
 s=input("Please,enter a number>>>")
 if(s.isdigit()):#if user enter a number
  n=int(s)#change user's number to integer
  i=2
  
  if(n>1):#becaus prime numbers are always >0 and 0,1 are not prime numbers
   while(i<n):
    if(n%i==0):   
     print(n,"is not a prime number\n","because",n,"/",i,"=",n//i)
     x=2
     break
    i=i+1
  
   else:
     print(n,"is a prime number")
     x=2
     
          
  else:#if n=0 or n=1 or any negative number
    print(n,"is not a prime number because prime number is a positive number greater than 1")
    x=2
  
 else:
  print("Sorry,you have to enter a number\n","try again")



 