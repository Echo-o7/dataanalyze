import diagram
import data
import matplotlib.pyplot as plt
from data import create_data
from data import create_randint_data
from diagram import show_histogram

analyze_data = create_data()
analyze_randint_data = create_randint_data()

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