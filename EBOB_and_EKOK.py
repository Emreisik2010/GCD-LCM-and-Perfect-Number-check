number1=int(input("giving a number for GCD  and LCM : "))
number2=int(input("giving a number for GCD  and LCM : "))

smaller_number=min(number1,number2)

for i in range(smaller_number,0,-1):
    if(number1%i == 0 and number2%i == 0):
        gcd=i
        break

lcm=(number1*number2)//gcd
print("greatest common divisor is:")
print(gcd)
print("least common multiple is:")
print(lcm)
