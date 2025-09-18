def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))    
    if num1 < 0 or num2 < 0:
        raise ValueError("Negative numbers are not allowed.")    
    gcd_result = find_gcd(num1, num2)   
    print(f"The GCD of {num1} and {num2} is: {gcd_result}")
except ValueError:
    print("Invalid input. Please enter non-negative integers only.")
