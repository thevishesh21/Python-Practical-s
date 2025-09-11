# Fibonacci Series Using While
limit = int(input("Enter The Limit : "))
a ,b = 0 , 1
print("Fibonacci Series Up to", limit ,":")
while a <= limit:
    print(a ,end=" ")
    a , b = b , a+b