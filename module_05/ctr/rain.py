num_years = int(input("Enter the number of years: "))

years = [] # TODO: Add rain info dictionaries as a single entry for each year. 

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