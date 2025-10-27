# Get user input
size = input("Size (S/M/L): ").upper()
bubble = input("Add bubble? (Y/N): ").upper()
ownglass = input("Use own glass? (Y/N): ").upper()

# Initialize price
price = 0

# Size and bubble pricing
if size == "M":
    price += 65
    if bubble == "Y":
        price += 10
elif size == "L":
    price += 80
    if bubble == "Y":
        price += 15
else:
    print("Invalid size input. Please choose M or L.")
    exit()

# Discount for own glass
if ownglass == "Y":
    price -= 5

# Output the final bill
print(f"Your bill is: {price} THB")
