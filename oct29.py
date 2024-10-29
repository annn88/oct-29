number =int(input("enter the number:"))
isprime =True
for i in range(2,number//2+1):
    if number % i ==0:
        isprime =False
        break
if isprime:
    print(f"the given number{number} is prime")
else:
    print(f"the given number {number} is not prime")
