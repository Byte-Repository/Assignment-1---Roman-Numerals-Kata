from datetime import date
from roman_numerals import arabic_to_roman

# Print a message to check if this code is executed
print("Code is running")

# Print an empty line for spacing
print()

# Convert Arabic numerals from 1 to 10 to Roman numerals and print them side by side
for num_in_arabic in range(1, 11):
    num_in_roman = arabic_to_roman(num_in_arabic)
    print(f"{num_in_arabic} ----> {num_in_roman}")