sale_amount=float(input("Enter the sale amount: "))

if sale_amount >=5000:
    discount_rate=0.20
elif sale_amount >=3000:
    discount_rate=0.15
elif sale_amount >=2000:
    discount_rate=0.10
else:
    discount_rate=0.05
    
#cal the discount amount

discount_amount=sale_amount*discount_rate
#cal the total amount after discount
final_price=sale_amount-discount_amount

#display the results
print("\n---------------Discount Calculation---------------")
print(f"Original sale Amount : ₹{sale_amount:.2f}")
print(f"Discount Rate applied : {discount_rate*100:.0f}%")
print(f"Discount Amount : ₹{discount_amount:.2f}")
print(f"Final Price after discount : ₹{final_price:.2f}")