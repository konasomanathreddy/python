import random
import string

def generate_otp(length=6):
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

def verify_otp(generated_otp, user_otp):
    return generated_otp == user_otp

otp = generate_otp()
print(f"Your OTP is: {otp}")  # In real use, this would be sent via SMS/email

user_input = input("Enter the OTP: ")
if verify_otp(otp, user_input):
    print("OTP verified successfully!")
else:
    print("Invalid OTP. Try again.")