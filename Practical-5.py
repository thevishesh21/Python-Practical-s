def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // find_gcd(a, b)
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))   
    if num1 < 0 or num2 < 0:
        raise ValueError("Negative numbers are not allowed.")   
    lcm_result = find_lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is: {lcm_result}")
except ValueError as e:
    print(f"Invalid input: {e}. Please enter non-negative integers only.")
