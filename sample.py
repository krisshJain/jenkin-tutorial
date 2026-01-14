import os

# CRITICAL SECURITY VULNERABILITY: Hardcoded password and token
# SonarCloud will flag this as a 'Blocker' or 'Critical' issue
db_password = "password123"
api_token = "5d804cee13ef534913c5f4e815ffd900bcd7fa72" 

def calculate():
    a = 10
    b = 0
    # CRITICAL BUG: Guaranteed Division by Zero
    # This is a logic error that SonarCloud flags as a Bug
    print(a / b)

# CODE SMELL: Identity comparison with a literal
if "admin" is "admin":
    calculate()

# Vulnerable use of exec (Security Risk)
exec("print('Dangerous Code')")