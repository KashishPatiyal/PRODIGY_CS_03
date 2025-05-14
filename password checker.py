import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Strength levels
    if score == 5:
        strength = "🟢 Very Strong"
    elif score == 4:
        strength = "🟡 Strong"
    elif score == 3:
        strength = "🟠 Moderate"
    elif score == 2:
        strength = "🔴 Weak"
    else:
        strength = "🔴 Very Weak"

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("• Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("• Include at least one uppercase letter (A-Z).")
    if not lower_criteria:
        feedback.append("• Include at least one lowercase letter (a-z).")
    if not digit_criteria:
        feedback.append("• Include at least one number (0-9).")
    if not special_criteria:
        feedback.append("• Include at least one special character (!@#$ etc).")

    return strength, feedback

# Main function
def main():
    password = input("🔑 Enter a password to check: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nSuggestions:")
        for line in feedback:
            print(line)
    else:
        print("✅ Your password is very strong!")

if __name__ == "__main__":
    main()
