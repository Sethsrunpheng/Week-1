# Read the length and width of the field in feet from the user
length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

# Calculate the area of the field in square feet
area = length * width

# Convert the area from square feet to acres
acres = area / 43560

# Display the result
print("The area of the field is", acres, "acres.")
