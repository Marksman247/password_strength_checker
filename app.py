# Import necessary libraries
import streamlit as st
import re

def password_strength(password: str) -> (str, int):
    """
    Evaluate the strength of a password and assign a score (0-5).
    Returns the strength category and score.
    """
    # Get the length of the password
    length = len(password)
    
    # Check for presence of uppercase letters
    has_upper = bool(re.search(r"[A-Z]", password))
    # Check for presence of lowercase letters
    has_lower = bool(re.search(r"[a-z]", password))
    # Check for presence of digits
    has_digit = bool(re.search(r"\d", password))
    # Check for presence of special characters
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Initialize password strength score
    score = 0

    # Increment score based on password features
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Determine strength category based on length and score
    if length == 0:
        return "", 0
    elif length < 6:
        return "Very Weak", 1
    elif score <= 2:
        return "Weak", 2
    elif score == 3:
        return "Medium", 3
    elif score == 4:
        return "Strong", 4
    elif score == 5 and length >= 12:
        return "Very Strong", 5
    else:
        return "Strong", 4

def password_advice(password: str) -> str:
    """
    Provide advice to improve password strength.
    """
    # List to store password improvement suggestions
    advice = []

    # Check for different password strength criteria
    if len(password) < 12:
        advice.append("Use at least 12 characters.")
    if not re.search(r"[A-Z]", password):
        advice.append("Add uppercase letters.")
    if not re.search(r"[a-z]", password):
        advice.append("Add lowercase letters.")
    if not re.search(r"\d", password):
        advice.append("Include numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        advice.append("Add special characters.")

    # Return advice or a positive message if no improvements needed
    if not advice:
        return "Your password looks great!"
    return "Tips to improve your password:\n- " + "\n- ".join(advice)

def main():
    # Custom styled title using Markdown and HTML
    st.markdown("<h1 style='color: darkgreen;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
    # Short description
    st.write("Enter a password to check its strength based on common criteria.")

    # Password input field (masked)
    password = st.text_input("Password", type="password")

    # If user enters a password
    if password:
        # Get strength and score
        strength, score = password_strength(password)
        # Get password advice
        advice = password_advice(password)

        # Display password strength result
        st.markdown(f"**Strength:** {strength}")

        # Display a progress bar as a visual strength meter
        st.progress(score / 5)

        # Show advice if password isn't 'Very Strong'
        if strength != "Very Strong":
            st.markdown(f"💡 {advice}")

        # Provide a code block displaying the password (for copying)
        st.write("✅ Copy your password (if it's secure):")
        st.code(password)

    # App footer
    st.markdown("\n---\n🔒 Built with Streamlit and Python")

# Run the main function when script is executed
if __name__ == "__main__":
    main()

# 👑 Built by MAX
