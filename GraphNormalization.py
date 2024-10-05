def normalize_values(values):
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) for x in values]

def main():
    # Theoretical values
    theory_values = [
        664.38,
        9965.78,
        132877.12,
        1660964.04,
        19931568.56
    ]
    
    # Experimental values
    experimental_values = [
        1001600,
        11001300,
        69005400,
        1262107900,
        16725886000
    ]

    # Normalize the values
    theory_normalized = normalize_values(theory_values)
    experimental_normalized = normalize_values(experimental_values)

    # Print normalized theoretical values
    print("Normalized Theoretical Values:")
    for value in theory_normalized:
        print(value)

    print("--------")

    # Print normalized experimental values
    print("Normalized Experimental Values:")
    for value in experimental_normalized:
        print(value)

if __name__ == "__main__":
    main()
