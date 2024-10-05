import math

input_sizes = [100, 1000, 10000, 100000, 1000000]

def calculate_complexity(input_sizes):
    complexities = []
    for n in input_sizes:
        complexity = n * (math.log(n, 2))
        complexities.append((n, complexity))
        print(f"{n}, {complexity}")

if __name__ == "__main__":
    calculate_complexity(input_sizes)
