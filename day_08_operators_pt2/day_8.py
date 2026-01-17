# Logic in Real-World Systems

# Example: Phone Unlock Logic
has_correct_pin = True
face_id_recognised = False

# Both must be true for the phone to open
can_unlock_phone = has_correct_pin and face_id_recognised

print("Security Check Passed", can_unlock_phone)
# Result will be fault because one is missing!

# -- REFLECTION ---

# I kept it quite simple for a code today but I sure did learn a lot.
# I explored Logic Operators through the lens of security systems.
# I learned that the and operator is essential for a multi-step verification.
# Now I am focusing on how the code could apply to real-world technology!

