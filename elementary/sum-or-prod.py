from subprocess import check_output


num = int(input("Give me a number\n"))

choice = input("Do you want sum or prod?\ns - sum\np - prod\n")

if choice.lower() == "s":
    sum = 0
    for i in range(1, int(num)+1):
        sum += i
    print("Sum: " + str(sum))
elif choice.lower() == "p":
    prod = 1
    for i in range(1, int(num)+1):
        prod *= i
    print("Product: " + str(prod))