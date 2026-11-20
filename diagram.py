import matplotlib.pyplot as plt
import random as ran

def show_histogram(data):
    plt.hist(data, bins=10)
    plt.title("Fördelning av slumpmässiga värden")
    plt.xlabel("Värde")
    plt.ylabel("Antal")
    plt.show()