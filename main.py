import diagram
import data
from data import create_data
from data import create_data
from diagram import show_histogram

data_number = create_data()
analyze_data = create_data()

#the print() make the outcome cleaner
print()
print("Antal värden:", len(analyze_data))
print("Första tio värdena:", analyze_data[:10])
show_histogram(analyze_data)
print()