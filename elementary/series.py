sum = 0
for i in range(2, 1000001):
    temp =  pow(-1, i+2)/(2*(i-1))
    sum += temp
print(sum)