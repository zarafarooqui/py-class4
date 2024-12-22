num=20
print("Table of 20")
for i in range(1,11):
    mul=num*i

    print(f"20 x {i}={mul}")

    #STAR PATTERN

n=int(input("enter number of rows:"))
for i in range(0,n):
  for i in range(0,i+1):
            print("*",end="")
  print("\n")

  #Natural Numbers Sum
num=1
sum=0
while(num <=10):
       sum=sum+num
       num=num+1

print("sum of first 10 natural numbers:",sum)

#PRIME NUMBERS

num=int(input("Enter number to be checked:"))
flag=False
if num>1:
      #check for factors
 for i in range(2,num):
   if(num %i)==0:
       flag=True 

if flag:
     print(num,"is not a prime number")
else:
     print(num,"is a prime number")