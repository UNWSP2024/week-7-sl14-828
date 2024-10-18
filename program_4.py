import math

def calculate_distance(coord1, coord2):
    # Calculate the distance between two 3D points
    return math.sqrt((coord2[0] - coord1[0])**2 + 
                     (coord2[1] - coord1[1])**2 + 
                     (coord2[2] - coord1[2])**2)

def main():
    while True:
        try:
            # User input for the first coordinate
            coord1_input = input("Enter the first 3D coordinate as (x, y, z): ")
            coord1 = tuple(map(float, coord1_input.strip('()').split(',')))

            # User input for the second coordinate
            coord2_input = input("Enter the second 3D coordinate as (x, y, z): ")
            coord2 = tuple(map(float, coord2_input.strip('()').split(',')))

            # Check if both coordinates are valid 3D tuples
            if len(coord1) != 3 or len(coord2) != 3:
                raise ValueError("Each coordinate must contain exactly three values.")

            # Calculate distance
            distance = calculate_distance(coord1, coord2)
            print(f"The distance between {coord1} and {coord2} is: {distance:.2f}")
            break  # Exit the loop after successful calculation

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter coordinates in the format (x, y, z).")

if __name__ == '__main__':
    main()
