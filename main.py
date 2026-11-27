import diagram
import data
import statistics
import random as ran
import matplotlib.pyplot as plt
from diagram import show_histogram
from data import create_data
from data import create_randint_data
from data import price_bike
from statistics import analyze_prices

bike_prices = [ 1200, 1100, 1200, 1300, 4500 ]
price_bike()
analyze_data = create_data()
analyze_randint_data = create_randint_data()
labb_number = input("Labb number? ")

if labb_number == "1":
    #the print() make the outcome cleaner
    print()
    print()
    print("Antal värden : ", len(analyze_data))
    print("Antal randint värden : ", len(analyze_randint_data))
    print()
    print("Första tio värdena : ", analyze_data[:10])
    print("Första tio randint värdena : ", analyze_randint_data[:10])
    print()
    show_histogram(analyze_data)
    show_histogram(analyze_randint_data)
    print()
    print()

elif labb_number == "2":
    mean_price, median_price = analyze_prices(bike_prices)
    print("Medelpris:", mean_price)
    print("Medianpris:", median_price)
