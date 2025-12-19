import re

def check_password_strength(password):  # <--- Make sure this name is exact
    strength = 0
    
    if len(password) >= 8: strength += 1
    if re.search("[a-z]", password): strength += 1
    if re.search("[A-Z]", password): strength += 1
    if re.search("[0-9]", password): strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password): strength += 1

    remarks = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return remarks.get(strength, "Extremely Weak"), strength
