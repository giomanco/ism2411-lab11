"""
Reflection:

1. In real work, you would use bracket notation (dict[key]) when a key is mandatory
   and its absence shows corrupted data or a critical bug that should stop execution
   immediately. On the other hand, .get() is used when a field is optional and a graceful fallback default prevents the script from crashing.
   My rule of thumb is to use brackets if missing data should trigger an alarm, and use .get()
   if missing data is an expected condition with a fallback.

2. This loop-and-accumulate pattern reminds me of a PivotTable in Excel, grouping transactions by category and summing their numeric values. 
   The Python version might be more useful because for larger datasets because it scales to millions of records without crashing spreadsheet software, can be automated inside backend data pipelines, and integrates
   seamlessly with APIs, databases, and scheduled batch jobs.
"""

# Exercise 1: One Customer
print("--- Exercise 1 ---")
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD Spend:", customer["ytd_spend"])
print("Full Dict:", customer)


# Exercise 2: Update and Add
print("\n--- Exercise 2 ---")
customer["phone"] = "555-0199"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# Exercise 3: Safe Lookup
print("\n--- Exercise 3 ---")

email_lookup = customer.get("email", "no email on file")
print("Lookup using .get():", email_lookup)

try:
    print(customer["email"])
except KeyError as e:
    print(f"KeyError caught successfully: key {e} not found")


# Exercise 4: Iterate
print("\n--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

# Comment explanation: Iterating directly over `customer` only loops through the dictionary's
# keys, not the values. To access each value without .items(),
# you have to manually look it up using bracket notation: customer[key].
print("Iterating without .items():")
for key in customer:
    print(f"{key} -> {customer[key]}")


# Exercise 5: Lookup Table
print("\n--- Exercise 5 ---")
tier_discounts = {
    "bronze": 0.0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

current_tier = customer.get("tier", "bronze")
discount_rate = tier_discounts.get(current_tier, 0.0)
purchase_amount = 200.00
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier}")
print(f"Discount Rate: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

# Exercise 6: List of Dicts
print("\n--- Exercise 6 ---")
customers = [
    {"name": "Alice Smith", "tier": "platinum"},
    {"name": "Bob Jones", "tier": "silver"},
    {"name": "Charlie Brown", "tier": "bronze"}
]

purchase_price = 300.00

for c in customers:
    rate = tier_discounts.get(c["tier"], 0.0)
    discount_amount = purchase_price * rate
    print(f"Customer: {c['name']} | Tier: {c['tier']} | Discount: ${discount_amount:.2f}")

# Exercise 7: Nested Catalog
print("\n--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} (Only {details['stock']} remaining)")


# Exercise 8: Sales by Region
print("\n--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

regional_sales = {}

for txn in transactions:
    region = txn["region"]
    amount = txn["amount"]
    regional_sales[region] = regional_sales.get(region, 0) + amount

for region in sorted(regional_sales.keys()):
    print(f"{region}: {regional_sales[region]}")
