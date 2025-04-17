
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent/100)
        
    else:
        return price
    
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values.")