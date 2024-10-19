def main():
    # Initialize a list to store all entered values
    all_entered_values = []

    # Input loop for user to enter year, state name, and population
    while True:
        year = input("Enter the year (or 'done' to finish): ")
        if year.lower() == 'done':
            break
        
        state = input("Enter the name of the state: ")
        
        while True:
            try:
                population = int(input("Enter the population: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the population.")

        # Append the entered values as a list
        all_entered_values.append([int(year), state, population])

    # Now have the user enter a year to sum populations
    year_to_sum = int(input("Enter the year to sum populations: "))
    
    # Call the function to sum populations for the specified year
    sum_population_for_year(all_entered_values, year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0
    
    # Loop through the list and sum the populations for the specified year
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_population += entry[2]
    
    # Print the total population for the specified year
    print(f"Total population for the year {year_to_sum}: {total_population}")

# Call the main function
if __name__ == '__main__':
    main()
