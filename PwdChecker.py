import re

# List of common passwords (You can expand this list)
COMMON_PASSWORDS = ["123456", "password", "12345678", "qwerty", "abc123", "password1", "12345"]

# Function to check password strength
def check_password_strength(password):
    strength = {
        "length": len(password) >= 8,
        "common": password in COMMON_PASSWORDS,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "number": any(char.isdigit() for char in password),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    return strength

# Function to display feedback
def display_feedback(strength):
    print("\nPassword Strength Analysis:")
    
    if not strength["length"]:
        print("- ❌ Password should be at least 8 characters long.")
    if strength["common"]:
        print("- ❌ This password is too common!** Choose a unique one.")
    if not strength["uppercase"]:
        print("- ❌ Add at least one uppercase letter (A-Z).")
    if not strength["lowercase"]:
        print("- ❌ Add at least one lowercase letter (a-z).")
    if not strength["number"]:
        print("- ❌ Include at least one number (0-9).")
    if not strength["special"]:
        print("- ❌ Use at least one special character (!,@,#,$,%,^,&,*).")

    if (strength["length"] and strength["uppercase"] and strength["lowercase"] 
        and strength["number"] and strength["special"] and not strength["common"]):
        print("\n✅ Great job! Your password is strong.")

# Main function
def main():
    password = input("Enter a password to check: ")
    
    # Check password strength
    strength = check_password_strength(password)
    display_feedback(strength)

if __name__ == "__main__":
    main()