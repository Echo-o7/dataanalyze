import matplotlib.pyplot as plt

def show_histogram(data):
    plt.hist(data, bins=10)
    plt.title("Fördelning av slumpmässiga värden")
    plt.xlabel("Värde")
    plt.ylabel("Antal")
    plt.show()