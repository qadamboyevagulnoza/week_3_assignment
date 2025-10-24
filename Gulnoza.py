Price_student = 2.00
Price_regular = 4.00
Price_premium = 6.00
Discount_threshold = 15.00
Discount_amount = 2.50
Stop_word = 'done'

current_subtotal = 0.00

print("\n=== Book Rental System ===")
print("Enter membership type: student, regular, or premium")
print(f"Type 'done' when finished selecting books\n")

while True:
    membership_type = input("Enter membership type: ")

    if membership_type == Stop_word:
        break

    price = 0.00
    if membership_type == 'student':
        price = Price_student
    elif membership_type == 'regular':
        price = Price_regular
    elif membership_type == 'premium':
        price = Price_premium
    else:
        print("Invalid membership type. Please enter 'student', 'regular', or 'premium'.")
        continue

    current_subtotal += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${current_subtotal:.2f}\n")

print("\n=== Rental Summary ===")

bulk_discount = 0.00
if current_subtotal >= Discount_threshold:
    bulk_discount = Discount_amount

final_total = current_subtotal - bulk_discount

print(f"Subtotal: ${current_subtotal:.2f}")

if bulk_discount > 0:
    print(f"Bulk Rental Discount: -${bulk_discount:.2f}")
else:
    print("Bulk Rental Discount: $0.00")

print(f"Final Total: ${final_total:.2f}")

print("Thank you for your rental!\n")
