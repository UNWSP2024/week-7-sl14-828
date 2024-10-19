# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def main():
    # Initialize a list to hold the monthly rainfall amounts
    monthlyRainfall = []

    # Input the rainfall for each month
    for month in range(1, 13):
        while True:
            try:
                rainfall = float(input(f"Enter the rainfall for month {month}: "))
                monthlyRainfall.append(rainfall)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    #total and average rainfall
    totalRainfall = sum(monthlyRainfall)
    averageRainfall = totalRainfall / 12

    #highest and lowest rainfall
    highestRainfall = max(monthlyRainfall)
    lowestRainfall = min(monthlyRainfall)
    highestMonth = monthlyRainfall.index(highestRainfall) + 1
    lowestMonth = monthlyRainfall.index(lowestRainfall) + 1

    # Display results
    print("\n--- Rainfall Statistics ---")
    print(f"Total rainfall for the year: {totalRainfall:.2f} units")
    print(f"Average monthly rainfall: {averageRainfall:.2f} units")
    print(f"Month with highest rainfall: Month {highestMonth} ({highestRainfall:.2f} units)")
    print(f"Month with lowest rainfall: Month {lowestMonth} ({lowestRainfall:.2f} units)")

if __name__ == "__main__":
    main()
