import os

# 1. SECURITY RISK: Hardcoded 'password' (SonarCloud will flag this)
SECRET_KEY = "admin123" 

# Jenkins will pass these as environment variables
a = int(os.getenv('VAL_A', 10))
b = int(os.getenv('VAL_B', 5))

# 2. CODE SMELL: Unused variable (SonarCloud will flag this)
unused_calculation = a + b + 100 

print("--- Jenkins Math Result ---")

# 3. BAD PRACTICE: Using a broad Exception (SonarCloud will flag this)
try:
    print(f"Adding {a} + {b} = {a + b}")
    print(f"Dividing {a} / {b} = {a / b}")
except Exception as e:
    print("Something went wrong")

print(f"Multiplying {a} * {b} = {a * b}")
print("--- Build Successful ---")v