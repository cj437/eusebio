from datetime import datetime
import time

def generate_timestamps():
    with open("log.txt", "w") as file:
        while True:
            yield datetime.now()
            time.sleep(1)

# Lambda function
square = lambda x: x * x

# Using del
my_list = [1, 2, 3]
del my_list[1]  # Removes second element
