import math
import statistics
print("--- MATH MODULE DEMONSTRATION ---")
num_sqrt = 25
print(f"The square root of {num_sqrt} is: {math.sqrt(num_sqrt)}")
base, exp = 2, 3
print(f"{base} raised to the power of {exp} is: {math.pow(base, exp)}")
num_fact = 5
print(f"The factorial of {num_fact} is: {math.factorial(num_fact)}")
num_floor = 12.7
print(f"The floor of {num_floor} is: {math.floor(num_floor)}")
num_ceil = 12.3
print(f"The ceiling of {num_ceil} is: {math.ceil(num_ceil)}")
print(f"The value of pi is approximately: {math.pi}")
print("\n--- STATISTICS MODULE DEMONSTRATION ---")
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
print(f"The sample data is: {data}")
print(f"The mean of the data is: {statistics.mean(data)}")
print(f"The median of the data is: {statistics.median(data)}")
print(f"The mode of the data is: {statistics.mode(data)}")
print(f"The standard deviation of the data is: {statistics.stdev(data)}")
