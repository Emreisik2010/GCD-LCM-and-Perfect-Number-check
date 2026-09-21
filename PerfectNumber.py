number=int(input("writing number for perfect number game"))
perfect_divisor_list=[]
total=int(0)


for i in range((number-1),0,-1):
    if(number%i == 0 ):
        perfect_divisor_list.append(i)

for x in (perfect_divisor_list):
    totaly=total+x


if number==totaly:
    print(f"this number is perfect number {number} ")

else:
    print("this not a perfect number")

