# Define the total number of cars and cars per row
total_cars = 23
cars_per_row = 5
# Calculate the number of full rows using integer division (//)
full_rows = total_cars // cars_per_row
# Calculate the remaining cars using subtraction
remaining_cars = total_cars % cars_per_row
# Print the results
print(full_rows)
print(remaining_cars)
