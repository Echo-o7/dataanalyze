import diagram
import data
from data import create_data

data_number = create_data()
RandomCount = 0

def RandomNumber():
    data_number = create_data()
    print(data_number)

while data_number != 100.0:
    RandomNumber()
    RandomCount=RandomCount+1
if data_number == 100.0:
    print(RandomCount)
    print(int("Stop"))

RandomNumber()