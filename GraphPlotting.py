import matplotlib.pyplot as plt

def normalize_values(values):
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) for x in values]

def plot_graph(theory_values, experimental_values):
    theory_normalized = normalize_values(theory_values)
    experimental_normalized = normalize_values(experimental_values)

    input_sizes = [999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000]

    plt.plot(input_sizes, theory_normalized, label="Normalized Theoretical Values", marker='o')
    plt.plot(input_sizes, experimental_normalized, label="Normalized Experimental Values", marker='s')

    plt.xlabel("Input Size (n)")
    plt.ylabel("Normalized Time")
    plt.title("Comparison of Normalized Theoretical vs Experimental Times")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')  # Optional: Use logarithmic scale for better visualization
    plt.show()

def main():
    theory_values = [9954.38, 9965.78, 132862.39, 132877.12, 1660945.99, 1660964.05, 19931547.20, 19931568.57]
    experimental_values = [3436000, 2967000, 33549000, 33973000, 471685000, 476321000, 9670140000, 9127986000]

    plot_graph(theory_values, experimental_values)

if __name__ == "__main__":
    main()
