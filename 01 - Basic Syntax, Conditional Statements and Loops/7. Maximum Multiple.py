divisor = int(input())
bound = int(input())
output = bound

while True:
    if output <= bound and output % divisor == 0:
        print(output)
        break
    output -= 1


