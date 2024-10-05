import matplotlib.pyplot as plt

def normalize_values(values):
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) for x in values]

def plot_graph(theory_values, experimental_values):
    input_sizes = [100, 1000, 10000, 100000, 1000000]  # Corresponding input sizes

    # Plotting the normalized values
    plt.plot(input_sizes, theory_values, label="Normalized Theoretical Values", marker='o')
    plt.plot(input_sizes, experimental_values, label="Normalized Experimental Values", marker='s')

    # Adding labels and title
    plt.xlabel("Input Size (n)")
    plt.ylabel("Normalized Value")
    plt.title("Comparison of Normalized Theoretical vs Experimental Values")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')  # Use logarithmic scale for better visualization
    plt.show()

def main():
    # Normalized values (as previously calculated)
    theory_normalized = [
        0.0,
        0.00046668228977457267,
        0.00663355454453848,
        0.08330277668316,
        1.0
    ]

    experimental_normalized = [
        0.0,
        0.0005978935196706053,
        0.004066025114051013,
        0.07540299052829327,
        1.0
    ]

    plot_graph(theory_normalized, experimental_normalized)

if __name__ == "__main__":
    main()
