# Home Energy Dashboard using Python

appliances = []

def add_appliance():
name = input("Enter appliance name: ")
power = float(input("Enter power rating (Watts): "))
hours = float(input("Enter daily usage (hours): "))

```
energy = (power * hours) / 1000
cost = energy * 8

appliance = {
    "name": name,
    "power": power,
    "hours": hours,
    "energy": energy,
    "cost": cost
}

appliances.append(appliance)

print(f"\n{name} added successfully!")
```

def show_dashboard():
print("\n========== HOME ENERGY DASHBOARD ==========")

```
if not appliances:
    print("No appliances added.")
    return

total_energy = 0
total_cost = 0

for appliance in appliances:
    print(f"\nAppliance: {appliance['name']}")
    print(f"Power: {appliance['power']} W")
    print(f"Daily Usage: {appliance['hours']} hours")
    print(f"Daily Energy: {appliance['energy']:.2f} kWh")
    print(f"Daily Cost: ₹{appliance['cost']:.2f}")

    total_energy += appliance["energy"]
    total_cost += appliance["cost"]

print("\n------------- TOTAL ------------")
print(f"Total Daily Energy : {total_energy:.2f} kWh")
print(f"Estimated Daily Cost: ₹{total_cost:.2f}")
print(f"Estimated Monthly Energy: {total_energy * 30:.2f} kWh")
print(f"Estimated Monthly Cost : ₹{total_cost * 30:.2f}")
```

while True:
print("\n===== HOME ENERGY DASHBOARD =====")
print("1. Add Appliance")
print("2. View Energy Dashboard")
print("3. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    try:
        add_appliance()
    except ValueError:
        print("Please enter valid numerical values.")

elif choice == "2":
    show_dashboard()

elif choice == "3":
    print("Home Energy Dashboard Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
