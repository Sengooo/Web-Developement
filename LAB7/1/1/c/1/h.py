number = int(input())
i = 1
while i <= number:
    if number%i == 0:
        print(i, end = ' ')
    i+=1