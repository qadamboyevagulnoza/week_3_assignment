PRICE_STUDENT = 2.00
PRICE_REGULAR = 4.00
PRICE_PREMIUM = 6.00
DISCOUNT_THRESHOLD = 15.00
DISCOUNT_AMOUNT = 2.50
STOP_WORD = 'done'

current_subtotal = 0.00

print("\n=== Book Rental System ===")
print("Enter membership type: student, regular, or premium")
print(f"Type '{STOP_WORD}' when finished selecting books\n")

while True:
    membership_type = input("Enter membership type: ")

    if membership_type == STOP_WORD:
        break

    price = 0.00
    if membership_type == 'student':
        price = PRICE_STUDENT
    elif membership_type == 'regular':
        price = PRICE_REGULAR
    elif membership_type == 'premium':
        price = PRICE_PREMIUM
    else:
        print("Invalid membership type. Please enter 'student', 'regular', or 'premium'.")
        continue

    current_subtotal += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${current_subtotal:.2f}\n")

print("\n=== Rental Summary ===")

bulk_discount = 0.00
if current_subtotal >= DISCOUNT_THRESHOLD:
    bulk_discount = DISCOUNT_AMOUNT

final_total = current_subtotal - bulk_discount

print(f"Subtotal: ${current_subtotal:.2f}")

if bulk_discount > 0:
    print(f"Bulk Rental Discount: -${bulk_discount:.2f}")
else:
    print("Bulk Rental Discount: $0.00")

print(f"Final Total: ${final_total:.2f}")
print("Thank you for your rental!\n")