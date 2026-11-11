import diagram
import data
from data import create_data
from data import create_data
from diagram import show_histogram

data_number = create_data()
analyze_data = create_data()
RandomCount = 0
Hacker_Mode = True

def RandomNumber():
    data_number = create_data()
    print(data_number, data_number, data_number, data_number, data_number, data_number, data_number, data_number, data_number, data_number)

if Hacker_Mode == True:
    while data_number != 100.0:
        RandomNumber()
        RandomCount=RandomCount+1
    if data_number == 100.0:
        print(RandomCount)
        print(int("Stop"))
elif Hacker_Mode == False:
    print("Antal värden:", len(analyze_data))
    print("Första tio värdena:", analyze_data[:10])
    show_histogram(analyze_data)