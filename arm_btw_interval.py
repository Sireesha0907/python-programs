lb = int(input("Enter lower range: "))
ub = int(input("Enter upper range: "))
power=len(str(lb))
for num in range(lb,ub + 1):
    power=len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp = temp//10     
       
    if num == sum:
        print(num)
