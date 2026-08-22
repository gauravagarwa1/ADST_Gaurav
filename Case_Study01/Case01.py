print("Enter Order Details")

#Input Taken 

amount=float(input("Enter the amount"))
distance=float(input("Enter the distance in km"))
customer_type=input("Enter the customer type (Regular/Gold/VIP): ").upper()
customer_rating=float(input("Enter the customer rating (1-5): "))
resturant_rating=float(input("Enter the restaurant rating (1-5): "))
perparation_time=int(input("Enter the preparation time in minutes: "))
payment_method=input("Enter the payment method (Cash/Card): ")
weather=input("Enter the weather condition (Sunny/Rainy/Cold): ")
demand_level=input("Enter the demand level (High/Medium/Low): ")
peak_hours=input("Enter the peak hours (Yes/No): ").lower()
previous_cancelation_count=int(input("Enter the previous cancellation count 1-5: "))

#2 Risk Assessment for Resturant

if resturant_rating < 3  or perparation_time > 60:
    rest_status = "High Risk"
elif resturant_rating < 4  or perparation_time > 30:
    rest_status = "Medium Risk"
else:
    rest_status = "Low Risk"

#3 Risk Assesment for Customer

if customer_rating < 3 or previous_cancelation_count > 3:
    canl_risk="High Risk"
elif customer_rating <3 or previous_cancelation_count > 1:
    canl_risk="Medium Risk"
else :
    canl_risk="Low Risk"


# 4 Customer Priority Delivery Status

if customer_type == "VIP" or amount>=1499:
    priority_status="Premium"
elif customer_type == "Gold" or amount>=799:
    priority_status="Standard"
else:
    priority_status ="low"

# 5 Order Acceptance
order_status="Accepted"
manual_review="Not Required"

if weather.lower()=="storm":
    order_status = "Rejected"
    rejection_reason = "Bad weather order cannot accpeted"

elif canl_risk == "High Risk" and amount>1500:
     order_status = "Rejected"
     rejection_reason = "High risk because of order value in cash"

elif rest_status =="High Risk":
    order_status="Rejected"
    rejection_reason="Rating low to accept"

elif customer_rating <3 and payment_method.lower() == "cash":
    order_status="Manual Review"
    manual_review="Red Flagged"

# 6 Delivery 

if distance <=3:
    delivery_charge=20
elif distance <=7:
    delivery_charge=50
elif distance <=15:
    delivery_charge=100
else:
    delivery_charge=120+ (distance-15)*10

# 7 Weather Charge 

if weather.lower() == "rainy":
    delivery_charge = delivery_charge + 50

if demand_level.lower()=="high" or peak_hours=="Yes":
    delivery_charge = delivery_charge + 50  

# 8 Discount Calculation and Free Delivery
discount=0.0
if customer_type == "VIP" and amount >= 1499:
    discount = amount * 0.11
    delivery_charge = 0
elif customer_type == "Gold" and amount >= 699:
    discount = amount * 0.08
    delivery_charge *= 0.5
elif customer_type == "Regular" and amount >= 499:
    discount = amount * 0.05

# 9 Order category

if amount >= 1500:
    order_category = "Family meal"
elif amount >= 800:
    order_category = "Lunch Special" 
elif amount >= 500:
    order_category = "Breakfast"
else:
    order_category = "Snacks"

# Final Amount Calculation

if order_status != "Rejected":
    final_amount = amount - discount + delivery_charge
else:
    final_amount = 0

# 10 Output the Order Details

print("\n" +  "=" * 40)
print("           FINAL ORDER ")
print("=" * 40)
print("\nOrder Details:")
print("Order Status:", order_status)
if order_status == "Rejected":
    print("Rejection Reason:", rejection_reason)
print("Manual Review:",manual_review)
print("Order Category:", order_category)
print("Priority:",priority_status)
print("Restraunt Status:",rest_status)
print("Cancllation Risk:",canl_risk)
print("="* 40)
print("Order Total",amount)
print("Discount",discount)
print("Delivery Charge:",delivery_charge)
print("="*40)
print("Final Amount:", final_amount)
print("="*40)