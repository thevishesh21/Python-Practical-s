n=int(input("Enter The No. Of Rows : "))
for i in range(n):
    for _ in range(n - i - 1):
        print(" ", end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)    
    print()