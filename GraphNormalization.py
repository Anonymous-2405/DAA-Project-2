def normalize_values(values):
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) for x in values]

def main():
    theory_values = [9954.38, 9965.78, 132862.39, 132877.12, 1660945.99, 1660964.05, 19931547.20, 19931568.57]
    experimental_values = [3436000, 2967000, 33549000, 33973000, 471685000, 476321000, 9670140000, 9127986000]

    theory_normalized = normalize_values(theory_values)
    experimental_normalized = normalize_values(experimental_values)

    print("Normalized Theoretical Values:")
    for value in theory_normalized:
        print(value)

    print("--------")

    print("Normalized Experimental Values:")
    for value in experimental_normalized:
        print(value)

if __name__ == "__main__":
    main()
    