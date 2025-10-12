# app.py

def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    It's a simple, well-defined function.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers (integer or float).")
    return a + b

def get_user_greeting(user_data):
    """
    Generates a greeting for a user using the safer .get() method
    to prevent KeyErrors, satisfying AI best-practice checks.
    """
    # First, check if user_data is a dictionary. If not, it's a TypeError.
    if not isinstance(user_data, dict):
        return "Hello, Guest! Invalid user data provided."

    # Use .get() to safely access keys. It returns None if the key is missing,
    # which we can check for to provide a complete default message.
    name = user_data.get("name")
    city = user_data.get("city")

    # If either name or city is missing, return the default greeting.
    if not name or not city:
        return "Hello, Guest! User data is incomplete."
    
    # If both are present, return the personalized greeting.
    return f"Hello, {name} from {city}!"


# --- FOR TESTING THE PIPELINE FAILURE ----
# Uncomment the function below to introduce a "CRITICAL" issue
# that the AI reviewer should flag, causing the pipeline to fail.

# def insecure_add(a, b):
#     """
#     This is a terribly insecure function that uses eval().
#     An AI reviewer should immediately flag this as a critical security risk.
#     """
#     # Using eval() on unvalidated input is a major security vulnerability.
#     # result = eval(f"{a} + {b}") 
#     # return result

