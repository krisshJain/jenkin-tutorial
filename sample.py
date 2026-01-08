import os

# Jenkins will pass these as environment variables
a = int(os.getenv('VAL_A', 10))
b = int(os.getenv('VAL_B', 5))

print("--- Jenkins Math Result ---")
print(f"Adding {a} + {b} = {a + b}")
print(f"Multiplying {a} * {b} = {a * b}")
print("--- Build Successful ---")