number = int(input())
length = number
sum = 0
for i in range(length):
    sum += number%10
    number //= 10
    if(number == 0):
        break
print(sum)
