import math

input_sizes = [999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000]

def calculate_complexity(input_sizes):
    complexities = []
    for n in input_sizes:
        complexity = n * (math.log(n, 2))
        complexities.append((n, complexity))
        print(f"{n}, {complexity}")

if __name__ == "__main__":
    calculate_complexity(input_sizes)
