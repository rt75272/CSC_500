num_years = int(input("Enter the number of years: "))

years = []

rain_info = {
    "January" : 0,
    "Febuary" : 0,
    "March" : 0,
    "April" : 0,
    "May" : 0,
    "June" : 0,
    "July" : 0,
    "August" : 0,
    "September" : 0,
    "October" : 0,
    "November" : 0,
    "December" : 0
}

for i in range(num_years):
    for month in rain_info:
        rain_info[month] = int(input(f"Enter the rainfall amount for {month}: "))
        print(rain_info[month])
    years.append(rain_info) # Adds entire year of rain info as one entry each.

print(years)


# Total number of months recorded. 
def num_months():
    return 0

# Total rainfall for all months recorded.
def total_rainfall():
    return 0

# Average rainfall over the course of all recorded months.
def avg_rainfall():
    return 0

def main():
    return 0