import numpy as np
import random as ran

def analyze_prices(prices):
    average = np.mean(prices)
    middle = np.median(prices)
    return average, middle